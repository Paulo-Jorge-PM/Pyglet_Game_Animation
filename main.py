#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet, random
from pyglet.window import key
from pyglet.gl import *

W_width=640
W_height=480
window = pyglet.window.Window(W_width, W_height,caption = 'Animation Teste')
#centrar window no monitor
window.set_location(window.screen.width/2 - window.width/2, window.screen.height/2 - window.height/2)
FPS = pyglet.clock.ClockDisplay()

#load das imagens e cria a grid de sprites
fundo_load = pyglet.image.load('fundo.png')
snake_load = pyglet.image.load('player_walk.png')
fundo = pyglet.sprite.Sprite(fundo_load, x=0, y=0)
snake = pyglet.image.ImageGrid(snake_load, 4, 8)

#lista de coordenadas por onde se movimenta, centradas nos squars
GridY=[]
for i in range(W_height/20):
	GridY.append(20*i+8)
GridX=[]
for i in range(W_width/20):
	GridX.append(20*i-2)

#define a posicao inicial do player no ecrã e variaveis
class Player:
	Up=False
	Right=False
	Down=False
	Left=False
	animation=0
	x=GridX[20]
	y=GridY[20]
	speed=60
	intervalAnimation1=3 #retarda o tempo dos passos para nao ser rápido demais
	intervalAnimation2=3

	def __init__(self, lenghtN):
		self.lenghtN=lenghtN

	def img(self):
		player = pyglet.sprite.Sprite(snake[self.animation], self.x, self.y)
		return player

#move the player - cna be optimized with functions, too many if's
def update(dt):
	if Player.Up==True:
		Player.y += dt * Player.speed
		if Player.intervalAnimation1%Player.intervalAnimation2 == 0:
			if Player.animation < 16 or Player.animation > 23:
				Player.animation = 16
			Player.animation += 1
			if Player.animation > 23:
				Player.animation = 16
			Player.intervalAnimation1 += 1
		else:
			Player.intervalAnimation1 += 1
	elif Player.Right==True:
		Player.x += dt * Player.speed
		if Player.intervalAnimation1%Player.intervalAnimation2 == 0:
			if Player.animation > 7:
				Player.animation = 0
			Player.animation += 1
			if Player.animation > 7:
				Player.animation = 0
			Player.intervalAnimation1 += 1
		else:
			Player.intervalAnimation1 += 1
	elif Player.Down==True:
		Player.y -= dt * Player.speed
		if Player.intervalAnimation1%Player.intervalAnimation2 == 0:
			if Player.animation < 24:
				Player.animation = 24
			Player.animation += 1
			if Player.animation > 31:
				Player.animation = 24
			Player.intervalAnimation1 += 1
		else:
			Player.intervalAnimation1 += 1
	elif Player.Left==True:
		Player.x -= dt * Player.speed
		if Player.intervalAnimation1%Player.intervalAnimation2 == 0:
			if Player.animation < 8 or Player.animation > 15:
				Player.animation = 8
			Player.animation += 1
			if Player.animation > 15:
				Player.animation = 8
			Player.intervalAnimation1 += 1
		else:
			Player.intervalAnimation1 += 1



			
#lista com as sprites do player
#Players = []
#Players.append(Player(snake).img())
Lenght=1

@window.event
def on_key_press(symbol, modifiers):
    #too many if's, can be optimized with lists/functions
	if symbol == key.UP and Player.Down!=True:
		Player.Up=True
		Player.Right=False
		Player.Down=False
		Player.Left=False
	elif symbol == key.RIGHT and Player.Left!=True:
		Player.Up=False
		Player.Down=False
		Player.Left=False
		Player.Right=True
	elif symbol == key.DOWN and Player.Up!=True:
		Player.Up=False
		Player.Right=False
		Player.Left=False
		Player.Down=True
	elif symbol == key.LEFT and Player.Right!=True:
		Player.Up=False
		Player.Right=False
		Player.Down=False
		Player.Left=True

@window.event
def on_draw():
	window.clear()
	fundo.draw()
	for i in range(Lenght):
		Player(i).img().draw()

	FPS.draw()

if __name__ == '__main__':
	#FPS limit to 60 per second
	pyglet.clock.schedule_interval(update, 1/60.0)
	pyglet.app.run()