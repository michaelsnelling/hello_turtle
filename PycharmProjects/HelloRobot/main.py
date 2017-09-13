from gopigo import *
import time

#### MY CLASS

class Piggy(object):

    def__init__(self):

        print("Hello, I'm your robot")
        self.dance()

    def dance(self):
        fwd()
        time.sleep(1.5)
        right.rot()
        time.sleep(.5)
        stop()


##### MY APP

mra = Piggy()


