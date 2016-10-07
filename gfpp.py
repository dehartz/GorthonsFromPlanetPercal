#Author:dehartz
#Program: gfpp.py
#-------------------------------------------------------------------
from sys import exit
from random import randint


class Map(object):
    def __init__(self,start_scene):
        pass
    def next_scene(self,scene_name):
        pass
    def opening_scene(self):
        pass

class Engine(object):
    def play(self):
        pass

class Scene(object):
    def enter(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class Central_Corridor(Scene):
    def enter(self):
        pass

class Laser_Weapon_Armory(Scene):
    def enter(self):
        pass

class The_Bridge(Scene):
    def enter(self):
        pass

class Escape_Pod(Scene):
    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
