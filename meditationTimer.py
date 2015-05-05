# WHAT: Timer for practicing meditation
# FEATURES:
    # In main(), can specify total timer length, as well as
    # an interval bell (to go off at certain increments)
    # The end vs interval bells have different sounds to distinguish them
# NOTE: Uses pygame to manage sounds. Make sure to have it installed

import time
import math
import pygame

class meditationTimer:
    def __init__(self, dir_sounds, total_inMinutes, interval_inMinutes):
        self.dir_sounds = dir_sounds
        self.total = 60 * total_inMinutes
        self.interval = 60 * interval_inMinutes

    def prepSounds(self):
        """ Uses pygame to load sound files """
        pygame.init()
        pygame.mixer.init()
        self.bellEnd = pygame.mixer.Sound(self.dir_sounds + "/shipBell.wav")
        self.bellInterval = pygame.mixer.Sound(self.dir_sounds + "/metalGong.wav")

    def runTimer(self):
        """ Use sleep() to wait 1sec at a time """
        self.prepSounds()
        startTime =time.time()

        elapsed = 0
        while True:
            if elapsed>=self.total:
                self.bellEnd.play()
                break
            elif elapsed%self.interval == 0:
                self.bellInterval.play()

            time.sleep(1)
            elapsed += 1
            print "elapsed: ",elapsed

        print "total elapsed: ", elapsed
        print "end-start: ", time.time() - startTime
        print "total diff: ", (time.time() - startTime) - elapsed


def main():
    dir_sounds = 'C:/Users/Abe/Dropbox/CS/apps/meditationTimer/sounds'
    total_inMins = 10
    interval_inMins = 1
    t =meditationTimer(dir_sounds, total_inMins, interval_inMins)
    t.runTimer()

main()

