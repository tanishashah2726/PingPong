import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {'paddle': (40,100), 'ball': (30,30)}
POS = {'player': (WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2), 'opponent': (50, WINDOW_HEIGHT / 2)}
SPEED = {'player': 500, 'opponent': 175, 'ball': 450}
REVERSE = {'player': 1}
COLORS = {
    'paddle': '#c77478',
    'paddle shadow': '#c1666b',
    'ball': '#e49273',
    'ball shadow': '#cf8569',
    'bg': '#5ca4a9',
    'bg detail': '#9bc1bc'
}