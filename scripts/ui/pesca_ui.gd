extends CanvasLayer
## Pesca (docs/ATIVIDADES.md, 4.1): 1) Lançar — segurar para escolher a distância; 2) Esperar — quando a boia afunda
## aparece "!" e tens 0,6 s para carregar; 3) Puxar — uma barra vertical com o peixe a mexer-se e a tua zona verde:
## segurar sobe a zona, largar desce. Mantém o peixe na zona até encher a barra de captura.
## A cana boa e a skill de Pesca aumentam a zona; os iscos chamam peixes raros; cada peixe tem um estilo.

signal _fim

const ALTURA := 320.0
const ICONE_PEIXE := "res://arte/icones/%s.png"

var _fundo: ColorRect
var _barra: ColorRect
var _zona: ColorRect
var _peixe: TextureRect
var _captura: ProgressBar
var _aviso: Label
var _forca: ProgressBar
var _fase := ""
var _t := 0.0
var _zona_y := 0.0
var _zona_v := 0.0
var _peixe_y := 0.0
var _peixe_alvo := 0.0
var _progresso := 0.3
var _peixe_id := ""
var _dados_peixe: Dictionary = {}
var _rng := RandomNumberGenerator.new()


func _ready() -> void:
	add_to_group("pesca_ui")
	layer = 6
	process_mode = Node.PROCESS_MODE_ALWAYS
	_rng.randomize()
	_fundo = ColorRect.new()
	_fundo.color = Color("2e222f")
	_fundo.position = Vector2(900, 160)
	_fundo.size = Vector2(110, ALTURA + 40)
	add_child(_fundo)
	_barra = ColorRect.new()
	_barra.color = Color("0b5e65")
	_barra.position = Vector2(20, 20)
	_barra.size = Vector2(40, ALTURA)
	_fundo.add_child(_barra)
	_zona = ColorRect.new()
	_zona.color = Color(0.57, 0.86, 0.41, 0.55)
	_zona.size = Vector2(40, 70)
	_barra.add_child(_zona)
	_peixe = TextureRect.new()
	_peixe.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_peixe.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_peixe.size = Vector2(32, 32)
	_peixe.position.x = 4
	_barra.add_child(_peixe)
	_captura = ProgressBar.new()
	_captura.fill_mode = ProgressBar.FILL_BOTTOM_TO_TOP
	_captura.show_percentage = false
	_captura.max_value = 1.0
	_captura.position = Vector2(72, 20)
	_captura.size = Vector2(18, ALTURA)
	var f := StyleBoxFlat.new()
	f.bg_color = Color("f9c22b")
	_captura.add_theme_stylebox_override("fill", f)
	_fundo.add_child(_captura)
	_aviso = Label.new()
	_aviso.position = Vector2(560, 300)
	_aviso.size = Vector2(160, 80)
	_aviso.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_aviso.add_theme_font_size_override("font_size", 40)
	_aviso.add_theme_color_override("font_color", Color("fbff86"))
	_aviso.add_theme_color_override("font_outline_color", Color("2e222f"))
	_aviso.add_theme_constant_override("outline_size", 6)
	add_child(_aviso)
	_forca = ProgressBar.new()
	_forca.show_percentage = false
	_forca.max_value = 1.0
	_forca.position = Vector2(540, 400)
	_forca.size = Vector2(200, 14)
	add_child(_forca)
	visible = false


## A melhor cana na mochila: 0 = nenhuma.
static func tier_cana() -> int:
	var t := 0
	for e in Jogo.inventario.espacos:
		if e != null and String(e.id).begins_with("cana_"):
			t = maxi(t, {"cana_bambu": 1, "cana_mangue": 2, "cana_prata": 3, "cana_coral": 4, "cana_do_pip": 5}.get(e.id, 1))
	return t


## Que peixe morde (andar ou cidade, hora, clima, estação; iscos e skill puxam pelos raros).
func escolher_peixe(andar: int, cidade: bool) -> String:
	var c := Dados.constantes
	if _rng.randf() < float(c.pesca_lixo) * (0.0 if Jogo.nivel_vida("pesca") >= 30 else 1.0):
		return ["bota_velha", "lata", "alga_seca"][_rng.randi() % 3]
	var possiveis := []
	var total := 0.0
	var isco := Jogo.inventario.tem("isco_dourado")
	for p in Dados.tabela("peixes").values():
		var aqui: bool = (cidade and p.get("cidade", false)) or (not cidade and float(andar) in p.andares)
		if not aqui or not Condicoes.avaliar(p.get("cond", "")):
			continue
		var w := float(c.pesca_pesos.get(p.raridade, 10))
		if isco and p.raridade in ["raro", "lendario"]:
			w *= float(c.pesca_isco_raro)
		possiveis.append([p.id, w])
		total += w
	if possiveis.is_empty():
		return ["bota_velha", "lata", "alga_seca"][_rng.randi() % 3]
	var x := _rng.randf() * total
	for p in possiveis:
		x -= p[1]
		if x <= 0.0:
			return p[0]
	return possiveis[0][0]


func pescar(andar: int, cidade: bool) -> void:
	if visible:
		return
	if tier_cana() == 0:
		Sistema.mensagem("Precisas de uma cana de pesca (o Pip vende).", "aviso")
		return
	visible = true
	get_tree().paused = true
	_fundo.visible = false
	_peixe_id = escolher_peixe(andar, cidade)
	_dados_peixe = Dados.obter("peixes", _peixe_id)
	var j := get_tree().get_first_node_in_group("jogador")
	if j:
		j.tocar("pescar", 1.0, true)
	_fase = "lancar"
	_forca.visible = true
	_forca.value = 0.0
	_aviso.text = ""
	Sistema.mensagem("Segura [interagir] para lançar.")
	await _fim
	visible = false
	get_tree().paused = false


func _process(delta: float) -> void:
	if not visible:
		return
	var carregar := Input.is_action_pressed("interagir") or Input.is_action_pressed("atacar")
	match _fase:
		"lancar":
			if carregar:
				_forca.value = fmod(_forca.value + delta * 0.9, 1.0)
			elif _forca.value > 0.05:
				_forca.visible = false
				_fase = "esperar"
				var lim: Array = Dados.c("pesca_espera", [1.5, 5.0])
				_t = _rng.randf_range(float(lim[0]), float(lim[1])) * (1.0 + _forca.value * 0.4)
				_aviso.text = "..."
		"esperar":
			_t -= delta
			if _t <= 0.0:
				_fase = "fisgar"
				_t = float(Dados.c("pesca_fisgar", 0.6))
				_aviso.text = "!"
		"fisgar":
			_t -= delta
			if Input.is_action_just_pressed("interagir") or Input.is_action_just_pressed("atacar"):
				_comecar_puxar()
			elif _t <= 0.0:
				_acabar(false, "O peixe fugiu antes de fisgares.")
		"puxar":
			_puxar(delta, carregar)


func _comecar_puxar() -> void:
	_fase = "puxar"
	_aviso.text = ""
	_fundo.visible = true
	var c := Dados.constantes
	_zona.size.y = float(c.pesca_zona) + tier_cana() * float(c.pesca_zona_por_tier) + Jogo.nivel_vida("pesca") * float(c.pesca_zona_por_nivel)
	_zona_y = ALTURA - _zona.size.y
	_zona_v = 0.0
	_peixe_y = ALTURA * 0.5
	_peixe_alvo = _peixe_y
	_progresso = 0.3
	var ic: String = Inventario._dados(_peixe_id).get("icone", "")
	_peixe.texture = load(ic) if ic != "" and ResourceLoader.exists(ic) else load("res://arte/icones/truta_ribeiro.png")


## O peixe mexe-se conforme o estilo: preguiçoso (devagar), normal, saltitão (saltos), rápido (lendários).
func _puxar(delta: float, carregar: bool) -> void:
	var estilo: String = _dados_peixe.get("estilo", "preguicoso" if _peixe_id in ["bota_velha", "lata", "alga_seca"] else "normal")
	var vel: float = {"preguicoso": 60.0, "normal": 110.0, "saltitao": 160.0, "rapido": 240.0}.get(estilo, 100.0)
	if absf(_peixe_y - _peixe_alvo) < 4.0 or _rng.randf() < delta * (2.5 if estilo == "saltitao" else 0.8):
		_peixe_alvo = _rng.randf_range(0, ALTURA - 32)
	_peixe_y = move_toward(_peixe_y, _peixe_alvo, vel * delta)
	_peixe.position.y = _peixe_y
	_zona_v += (-520.0 if carregar else 420.0) * delta
	_zona_v = clampf(_zona_v, -260.0, 260.0)
	_zona_y = clampf(_zona_y + _zona_v * delta, 0.0, ALTURA - _zona.size.y)
	if _zona_y <= 0.0 or _zona_y >= ALTURA - _zona.size.y:
		_zona_v *= -0.3
	_zona.position.y = _zona_y
	var dentro := _peixe_y + 16 >= _zona_y and _peixe_y + 16 <= _zona_y + _zona.size.y
	_progresso += (float(Dados.c("pesca_encher", 0.28)) if dentro else -float(Dados.c("pesca_esvaziar", 0.2))) * delta
	_captura.value = _progresso
	if _progresso >= 1.0:
		_acabar(true, "")
	elif _progresso <= 0.0:
		_acabar(false, "O peixe soltou-se.")


func _acabar(ok: bool, msg: String) -> void:
	_fase = ""
	if ok:
		Jogo.apanhar(_peixe_id, 1)
		if not _peixe_id in ["bota_velha", "lata", "alga_seca"]:
			Colecoes.peixe(_peixe_id)
			Eventos.peixe_apanhado.emit(_peixe_id)
		Jogo.treinar_vida("pesca", 1)
		if _dados_peixe.get("raridade", "") == "lendario":
			Sistema.mensagem("Um peixe LENDÁRIO! %s!" % _dados_peixe.get("nome_pt", ""), "nivel")
	else:
		Sistema.mensagem(msg, "aviso")
	_fundo.visible = false
	_aviso.text = ""
	_fim.emit()
