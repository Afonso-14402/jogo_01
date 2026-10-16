extends Node
## Opções do jogo (docs/INTERFACE.md, secção 7), gravadas em user://opcoes.json.

const CAMINHO := "user://opcoes.json"

var valores := {
	"volume_geral": 1.0, "volume_musica": 0.8, "volume_efeitos": 1.0, "volume_bips": 0.7,
	"ecra_inteiro": false, "tremor": true, "flashes": true, "numeros_dano": true,
	"velocidade_texto": 1.0, "dicas": true, "gravacao_automatica": true, "idioma": "pt",
}


func _ready() -> void:
	carregar()
	aplicar()


func v(chave: String) -> Variant:
	return valores.get(chave)


func mudar(chave: String, valor: Variant) -> void:
	valores[chave] = valor
	aplicar()
	gravar()


func aplicar() -> void:
	Audio.volume_musica = float(valores.volume_musica) * float(valores.volume_geral)
	Audio.volume_efeitos = float(valores.volume_efeitos) * float(valores.volume_geral)
	AudioServer.set_bus_volume_db(0, linear_to_db(maxf(0.0001, float(valores.volume_geral))))
	if DisplayServer.get_name() != "headless":
		DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN if valores.ecra_inteiro else DisplayServer.WINDOW_MODE_WINDOWED)


func gravar() -> void:
	var f := FileAccess.open(CAMINHO, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(valores, "\t"))


func carregar() -> void:
	if not FileAccess.file_exists(CAMINHO):
		return
	var d: Variant = JSON.parse_string(FileAccess.get_file_as_string(CAMINHO))
	if d is Dictionary:
		for k in d:
			valores[k] = d[k]
