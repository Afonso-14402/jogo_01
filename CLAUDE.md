# Instruções para o Claude neste repositório

- O plano oficial do jogo está em `OBJETIVO.md` e a **bíblia do jogo** em `docs/` (índice em `docs/README.md`):
  história, 100 andares (`docs/TORRE.md` e `docs/regioes/`), bosses, cidades, NPCs, missões, armas, equipamento,
  itens, progressão, atividades, **sistemas (fórmulas)**, **programação (Godot)**, interface, áudio e arte.
  Lê o que for preciso antes de qualquer trabalho e segue-o. Se uma tarefa contrariar o plano, avisa o utilizador
  e propõe a alteração ao documento primeiro. Quando programares, os números vêm de `docs/SISTEMAS.md` e os
  conteúdos dos outros documentos (passam para JSON em `dados/`).
- Fala com o utilizador em **português de Portugal**, de forma simples (está a aprender estas ferramentas).
- Motor: **Godot 4** com **GDScript**. Mundo 3D (Blender, `.glb`) + bonecos 2D pixel art em `Sprite3D` com billboard.
- Texturas pixel art sempre com filtro *nearest* (nunca desfocar).
- **Arte: quem desenha é o utilizador**, à mão no Pixelorama/Aseprite, no estilo da referência
  `arte/referencia/aranha_mae/`, e **tudo é animado** (ver `docs/ARTE.md`, secção 0). O Claude só faz arte
  provisória quando for pedida, e sempre que mostrar arte mostra-a **animada**.
- Ferramenta para ver sprites animados e verificar as regras: `ferramentas/visualizador.html`.
- A arte do utilizador fica em `arte/` (ver `docs/ARTE.md`, secção 8). O projeto Godot fica na raiz do repositório.
- Dados do jogo (itens, armas, receitas, monstros, andares) ficam em ficheiros de dados separados do código,
  para serem fáceis de editar.
- Ao acabar uma etapa, marca-a como feita (`[x]`) no `OBJETIVO.md`.
