class_name Estacao
extends Interagivel
## Estação de crafting (docs/SISTEMAS.md, secção 11): forja, alquimia, fogao, fogueira, tear, joalharia, bancada.
## Abre a janela de crafting com as receitas desta estação.

const NOMES := {"forja": "Forja", "alquimia": "Mesa de Alquimia", "fogao": "Fogão", "fogueira": "Fogueira",
	"tear": "Tear", "joalharia": "Mesa de Joalharia", "bancada": "Bancada"}

@export var estacao: String = "fogueira"


func _ready() -> void:
	texto = "Usar %s" % NOMES.get(estacao, estacao)
	super._ready()
	usado.connect(func(_j): 
		var ui = get_tree().get_first_node_in_group("crafting_ui")
		if ui:
			ui.abrir_estacao(estacao))
