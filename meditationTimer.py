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
        #self.total = 60.0 * total_inMinutes
        #self.interval = 60.0 * interval_inMinutes
        self.total = 6.0
        self.interval = 2.0
        self.startTime = time.time()
        self.prepSounds()

    def prepSounds(self):
        """ Uses pygame to load sound files """
        pygame.init()
        pygame.mixer.init()
        self.bellEnd = pygame.mixer.Sound(self.dir_sounds + "/shipBell.wav")
        self.bellInterval = pygame.mixer.Sound(self.dir_sounds + "/metalGong.wav")

    def printEndingStats(self):
        diff = time.time() - self.startTime
        print ""
        print "clock diff: ", diff
        print "error: ", diff-self.total

    def runTimer_int_elapsed(self):
        """ 
        Use sleep() to wait 1sec at a time
        All vars are in integer seconds
        """
        self.total = int(self.total)
        self.interval = int(self.interval)

        print "elapsed: 0"
        elapsed = 0
        while (elapsed<self.total):

            if elapsed%self.interval == 0:
                self.bellInterval.play()
                print "bellInterval"

            time.sleep(1)
            elapsed += 1
            print "elapsed: ", elapsed

        # End
        self.bellEnd.play()
        print "bellEnd"
        self.printEndingStats()

    def runTimer_int_remain(self):
        """ 
        Use sleep() to wait 1sec at a time
        All vars are in integer seconds
        """
        self.interval = int(self.interval)
        remain = int(self.total)
        print "remain: ", remain

        while (remain>0):
            if remain%self.interval == 0:
                self.bellInterval.play()
                print "bellInterval"

            time.sleep(1)
            remain -= 1
            print "remain: ", remain

        # End
        self.bellEnd.play()
        print "bellEnd"
        self.printEndingStats()

def main():
    dir_sounds = 'C:/Users/Abe/Dropbox/CS/apps/meditationTimer/sounds'
    total_inMins = 10
    interval_inMins = 1
    t =meditationTimer(dir_sounds, total_inMins, interval_inMins)
    t.runTimer_int_elapsed()
    #t.runTimer()
    #t.runTimer_int_remain()

main()

# TODO:
# wrap up int_remain (make sure it works)
# work on float_refined (harder than it looks!)
# What I want
    # print 0...total (include 0)
    # ring interval bell at 0, ring bell after each interval secs
    # ring end bell after total
    # TRY to get time to be more accurate

