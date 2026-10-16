extends Node
## Central de sinais: os sistemas (missões, conquistas, bestiário, HUD) ouvem daqui.

signal monstro_morto(id: String, nivel: int)
signal item_apanhado(id: String, qtd: int)
signal boss_derrotado(id: String)
signal missao_mudou(id: String)
signal jogador_dano(valor: int)
signal jogador_morreu
signal jogador_subiu_nivel(nivel: int)
signal xp_ganha(valor: int)
signal ouro_mudou(total: int)
signal stats_mudaram
signal mensagem_sistema(texto: String, tipo: String)
signal andar_entrou(numero: int)
