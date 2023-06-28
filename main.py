# pip install pygame moderngl pyGLM numba
from settings import *
import moderngl as mgl
import pygame as pg
import sys

class VoxelEngine: 
    def __init__(self):    # class constructor
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)    # prevent use of depracated fn
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)    # depth buffer

        pg.display.set_mode(WIN_RES, flags = pg.OPENGL | pg.DOUBLEBUF)  # set window
        self.ctx = mgl.create_context()

        self.ctx.enable(flags = mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)    # activate fragment depth testing, culling of invisible faces & color blending
        self.ctx.gc_mode = 'auto'    # mgl auto garbage collect unused opengl objects to avoid manual deletion

    def update(self):      # method to update state of objects
        pass

    def render(self):      # render objects
        pass

    def handle_events(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    app = VoxelEngine()
    app.run()