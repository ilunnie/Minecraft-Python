<img width=100% src="http://capsule-render.vercel.app/api?type=Soft&color=4b5c38&height=100&section=header&text=MINECRAFT%20PYTHON&fontSize=30&fontColor=fff&animation=twinkling&fontAlignY=50"/> 

<div>
  <img width=15% align="right" src="./assets/panda.gif"> <h2><b> Minecraft feito em sala usando python para apresentação </b></h2> ㅤ> Created on 01/03/2023 <br> ㅤ> @author: Luis Gustavo Caris dos Santos <br> ㅤ> <code>pip install Ursina</code> para usar<br><br>
</div>

<h3>Explicação:</h3>

| FUNÇÕES | EXPLICAÇÃO |
|----|----|
| Voxel(textura, posicao) | Gera o bloco na posição informada<br>- por padrão `posicao` = (0, 0, 0)
| Voxel().input(key) | Se `key` == "right mouse down":<br>- posiciona o bloco selecionado<br><br> Se `key` == "left mouse down"<br>- Destroy o bloco que está no centro da visão|
| GerarEstrutura().lerArquivo(arquivo) | Interpreta um .txt da pasta `bases` com informações sobre um estrutura |
| GerarEstrutura().criarEstrutura(arquivo, position) | Controi uma estrutura:<br>- `arquivo` = .txt que ira passar para `.lerArquivo(arquivo)`<br>- `position` = coordenadas base do mundo para contruir a estrutura |
| update() | Função chama a cada frame |
| Slots().atualizar_slot() | Identifica o slot de itens selecionado |
| mao.active() | Atualiza a posição da mão para frente |
| mao.passive() | Volta a posição da mão para o padrão |

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=4b5c38&height=120&section=footer"/>
