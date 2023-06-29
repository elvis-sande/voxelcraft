from settings import *

class ShaderProgram:
    def __init__(self, app):    # pointer to opengl context
        self.app = app
        self.ctx = app.ctx

    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()