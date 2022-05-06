#!/usr/bin/env python
# coding=utf-8
import sys
import argparse
import os
from slicerender import *
from raycast import *
import glfw


class RenderWin:
    """GLFW Rendering window class"""
    def __init__(self, imageDir):
        # save current working directory
        cwd = os.getcwd()

        #initialize glfw, this changes cwd
        glfw.init()

        # restore cwd
        os.chdir(cwd)

        # version hints
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE,
                         glfw.OPENGL_CORE_PROFILE)

        # make a window
        self.width, self.height = 512, 512
        self.aspect = self.width / float(self.height)
        self.win = glfw.create_window(self.width, self.height, 'volrender', None, None)
        # make context current
        glfw.make_context_current(self.win)

        # initialize GL
        glViewport(0, 0, self.width, self.height)
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 0.0)

        # set window callbacks
        glfw.set_mouse_button_callback(self.win, self.onMouseButton)
        glfw.set_key_callback(self.win, self.onKeyboard)
        glfw.set_window_size_callback(self.win, self.onSize)

        # load volume data
        self.volume = volreader.loadVolume(imageDir)
        # create renderer
        self.renderer = RayCastRender(self.width, self.height, self.volume)

        # exit flag
        self.exitNow = False

    def onMouseButton(self, win, button, action, mods):
        pass

    def onKeyboard(self, win, key, scancode, action, mods):
        if key is glfw.KEY_ESCAPE:
            self.renderer.close()
            self.exitNow = True
        else:
            if action is glfw.PRESS or action is glfw.REPEAT:
                if key == glfw.KEY_V:
                    # toggle render mode
                    if isinstance(self.renderer, RayCastRender):
                        self.renderer = SliceRender(self.width, self.height,
                                                    self.volume)
                    else:
                        self.renderer = RayCastRender(self.width, self.height,
                                                      self.volume)

                    # call reshape on renderer
                    self.renderer.reshape(self.width, self.height)
                else:
                    # send keypress to renderer
                    keyDict = {glfw.KEY_X: 'x', glfw.KEY_Y: 'y',
                               glfw.KEY_Z: 'z', glfw.KEY_LEFT: 'l',
                               glfw.KEY_RIGHT: 'r'}
                    try:
                        self.renderer.keyPressed(keyDict[key])
                    except:
                        pass

    def onSize(self, win, width, height):
        self.width = width
        self.height = height
        self.aspect = width / float(height)
        glViewport(0, 0, self.width, self.height)
        self.renderer.reshape(width, height)

    def run(self):
        # start loop
        while not glfw.window_should_close(self.win) and not self.exitNow:
            # render
            self.renderer.draw()
            # swap buffers
            glfw.swap_buffers(self.win)
            # wait for events
            glfw.wait_events()
        # end
        glfw.terminate()


def main():
  print('starting volrender...')
  # create parser
  parser = argparse.ArgumentParser(description="Volume Rendering...")
  # add expected arguments
  parser.add_argument('--dir', dest='imageDir', required=True)
  # parse args
  args = parser.parse_args()

  # create render window
  rwin = RenderWin(args.imageDir)
  rwin.run()

# call main
if __name__ == '__main__':
  main()
