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

        self.clock = pg.time.Clock()    # keep track of time
        self.delta_time = 0
        self.time = 0

        self.is_running = True    # flag to check if app is running

    def update(self):      # method to update state of objects
        self.delta_time = self.clock.tick()    # update deltatime
        self.time = pg.time.get_ticks() * 0.001    # update time
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')    # show fps in title bar

    def render(self):      # render objects
        self.ctx.clear(color=BG_COLOR)    # clear frame and depth buffers
        pg.display.flip()    # display new frame

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        while self.is_running:  # check if is_running = True
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    app = VoxelEngine()
    app.run()