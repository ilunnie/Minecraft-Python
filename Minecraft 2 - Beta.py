
"""
Created on 01/03/2023

@author: Luis Gustavo Caris dos Santos
""""""
Objetivo:
     • Criar algum jogo em python, usando qualquer biblioteca.

Ideia:
     • Criar usando algum método que eu ainda não conhecia
	 • Usar a biblioteca Ursina Engine, para criar um jogo em 3D
	 • Recriar a versão beta do Minecraft(Com algumas melhorias)
"""

# Importa todos os itens da biblioteca Ursina Engine
from ursina import *
# Importa os controles de primeira pessoa
from ursina.prefabs.first_person_controller import FirstPersonController

# Cria o app do jogo
app = Ursina()
# Carrega as texturas
grass_texture       = load_texture('assets/grass_block.png')
dirt_texture   	    = load_texture('assets/dirt_block.png')
stone_texture       = load_texture('assets/stone_block.png')
stoneBrick_texture  = load_texture('assets/stoneBrick_block.png')
brick_texture       = load_texture('assets/brick_block.png')
wood_texture 		= load_texture('assets/wood_block.png')
logWood_texture 	= load_texture('assets/logWood_block.png')
leaves_texture 		= load_texture('assets/leaves_block.png')
sky_texture     	= load_texture('assets/skybox.png')
arm_texture     	= load_texture('assets/arm_texture.png')
# Lista de texturas
sprites = [grass_texture, dirt_texture, stone_texture, brick_texture, wood_texture, logWood_texture, stoneBrick_texture, leaves_texture, None]
# Carrega os blocos
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
# Define o item que está na mão
slot_pick = 1

# Define a visibilidade do contador de FPS
window.fps_counter.enabled = False
# Define a visibilidade do botão de fechar
window.exit_button.visible = False

# Função padrão do Ursina Engine que é chamada a cada frame
def update():
	global slot_pick
	slots.atualizar_slot()
	
	if held_keys['left mouse'] or held_keys['right mouse']:
		mao.active()
	else:
		mao.passive()

	for i in range(1, 10):
		if held_keys[str(i)]: slot_pick = i

# Classe que cria os icones de slots
class Slots(Entity):
	def __init__(self, num_circulos=9, tamanho_circulo=0.1):
		super().__init__()
		self.num_circulos = num_circulos
		self.tamanho_circulo = tamanho_circulo
		self.circulos = []
		self.texturas = []
		for i in range(num_circulos):
			x = (i - num_circulos/2 + 0.5) * tamanho_circulo
			y = -0.4
			circulo = Entity(
                parent=camera.ui,
                model='circle',
				scale=tamanho_circulo/2,
				position = (x, y),
				color=color.dark_gray
			)
			self.circulos.append(circulo)
			if sprites[i] != None:
				icons = Entity(
					parent=camera.ui,
					model='cube',
					scale=tamanho_circulo/3,
					position = (x, y),
					texture = sprites[i]
				)

	def atualizar_slot(self):
		for i in range(self.num_circulos):
			if i+1 == slot_pick:
				self.circulos[i].scale = 0.15/2
			else:
				self.circulos[i].scale = self.tamanho_circulo/2

# Classe para criar/destruir os blocos
class Voxel(Button):
	# Gera um bloco
	def __init__(self, textura, posicao = (0,0,0)):
		super().__init__(
			parent = scene,
			position = posicao,
			model = 'assets/block',
			origin_y = 0.5,
			texture = textura,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)
	# Quando uma tecla for precionada olhando para um bloco
	def input(self,key):
		if self.hovered:
			# Se for o botão direito do mouse, ele cria um bloco refetente ao slot selecionado
			if key == 'right mouse down':
				punch_sound.play()
				if slot_pick == 1: voxel = Voxel(grass_texture, posicao = self.position + mouse.normal)
				if slot_pick == 2: voxel = Voxel(dirt_texture, posicao = self.position + mouse.normal)
				if slot_pick == 3: voxel = Voxel(stone_texture, posicao = self.position + mouse.normal)
				if slot_pick == 4: voxel = Voxel(brick_texture, posicao = self.position + mouse.normal)
				if slot_pick == 5: voxel = Voxel(wood_texture, posicao = self.position + mouse.normal)
				if slot_pick == 6: voxel = Voxel(logWood_texture, posicao = self.position + mouse.normal)
				if slot_pick == 7: voxel = Voxel(stoneBrick_texture, posicao = self.position + mouse.normal)
				if slot_pick == 8: voxel = Voxel(leaves_texture, posicao = self.position + mouse.normal)
			# Se for o botão esquerdo do mouse, ele destroy o bloco
			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)

# Classe que cria o céu
class ceu(Entity):
    def __init__(self):
        super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

# Classe que cria a mão
class mao(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

# Classe capaz de gerar estruturas a travez de arquivo txt
class GerarEstrutura():
	# Separa as informações do txt
	def lerArquivo(self, arquivo):
		with open(arquivo, 'r') as arquivo:
			linhas = arquivo.readlines()
			lista = []
			for linha in linhas:
				partes = linha.strip().split(',')
				lista.append(list(map(str.strip, partes)))
		return lista
	# Gera a estrutura
	def criarEstrutura(self, arquivo, position):
		lista = self.lerArquivo(arquivo)
		# Cria o bloco da linha
		for bloco in lista:
			# Pega a textura do bloco
			textura = eval(bloco[0].strip('()'))
			# Pega as coordenadas do bloco
			x = int(bloco[1].strip('()'))
			y = int(bloco[2])
			z = int(bloco[3].strip('()'))

			Voxel(textura, posicao=(position[0]+x, position[1]+y, position[2]+z))


# Gera o mundo padrão
for z in range(16):
	for x in range(16):
		voxel = Voxel(grass_texture, posicao = (x,0,z))
	
for y in range(-1, -3, -1):
	for z in range(16):
		for x in range(16):
			voxel = Voxel(dirt_texture, posicao = (x,y,z))
		
for y in range(-3, -5, -1):
	for z in range(16):
		for x in range(16):
			voxel = Voxel(stone_texture, posicao = (x,y,z))

GerarEstrutura().criarEstrutura('bases/tree.txt', (10, 1, 13))
FirstPersonController()
slots = Slots()
slots.atualizar_slot()
ceu = ceu()
mao = mao()

app.run()
