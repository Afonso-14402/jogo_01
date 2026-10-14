# Instruções para o Claude neste repositório

- O plano oficial do jogo está em `OBJETIVO.md`, com os detalhes em `docs/TORRE.md` (100 andares),
  `docs/ARMAS.md` (armas), `docs/HISTORIA.md`, `docs/NPCS.md`,
  `docs/ATIVIDADES.md`, `docs/PROGRESSAO.md` e `docs/ARTE.md` (regras da arte, nomes e pastas). Lê-os antes de qualquer
  trabalho e segue-os. Se uma tarefa contrariar o plano, avisa o utilizador e propõe a alteração ao plano primeiro.
- Fala com o utilizador em **português de Portugal**, de forma simples (está a aprender estas ferramentas).
- Motor: **Godot 4** com **GDScript**. Mundo 3D (Blender, `.glb`) + bonecos 2D pixel art em `Sprite3D` com billboard.
- Texturas pixel art sempre com filtro *nearest* (nunca desfocar).
- A arte do utilizador fica em `arte/` (ver `docs/ARTE.md`, secção 8). O projeto Godot fica na raiz do repositório.
- Dados do jogo (itens, armas, receitas, monstros, andares) ficam em ficheiros de dados separados do código,
  para serem fáceis de editar.
- Ao acabar uma etapa, marca-a como feita (`[x]`) no `OBJETIVO.md`.
