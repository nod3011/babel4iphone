#PyGL2D - A 2D library for PyGame and PyOpenGL
#Copyright (C) 2008 - PyMike

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import rect, display, texture

def load(elem, pos = [0, 0], filters = ["filter"]):
    return Surface(elem, pos, filters)


class Surface(object):

    def __init__(self, elem, pos = [0, 0], filters = ["filter"]):
        if type(elem) is str:
            self.surface = pygame.image.load(elem)
        else:
            # is a pygame.Surface
            self.surface = elem
        
        self.texture = texture.Texture(self.surface, filters)
        
        # image dimensions
        [self.width, self.height] = [self.w, self.h] = self.surface.get_size()
        self.center = [self.w / 2, self.h / 2]
        self.win_size = display.get_size()
        
        # rect
        self.rect = rect.Rect(0, 0, self.w, self.h)
        self.rect.center = pos
        
        # image mods
        self.rotation = 0
        self.scalar = 1.0
        self.color = [1.0, 1.0, 1.0, 1.0]
        
        # setting GL
        self.dl = glGenLists(1)
        glNewList(self.dl, GL_COMPILE)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        glTexCoord2i(0, 0); glVertex3f(-self.w / 2.0, -self.h / 2.0, 0)
        glTexCoord2i(1, 0); glVertex3f( self.w / 2.0, -self.h / 2.0, 0)
        glTexCoord2i(1, 1); glVertex3f( self.w / 2.0,  self.h / 2.0, 0)
        glTexCoord2i(0, 1); glVertex3f(-self.w / 2.0,  self.h / 2.0, 0)
        glEnd()
        glEndList()
    
    #def get_at(self, pos):
    #    return self.surface.get_at(pos) # ???
    
    def delete(self):
        glRemoveTextures([self.texture])
        del self
    
    def scale(self, scale):
        self.scalar = scale
        
        # rect
        self.rect.width = self.w * scale
        self.rect.height = self.h * scale
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y
    
    def rotate(self, rotation):
        self.rotation = rotation
    
    def colorize(self, R, G, B, A):
        self.color = [R / 255.0, G / 255.0, B / 255.0, A / 255.0]
    
    def get_width(self):
        return self.w * self.scalar
    
    def get_height(self):
        return self.h * self.scalar
    
    def get_rect(self):
        return self.rect
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.rect.x + self.rect.w / 2, 
                     self.win_size[1] - self.rect.y - self.rect.h / 2,
                     0)
        glColor4f(*self.color)
        glRotatef(self.rotation, 0, 0, 1)
        glScalef(self.scalar, self.scalar, self.scalar)
        glCallList(self.dl)
        glPopMatrix()
