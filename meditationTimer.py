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
        """ For debuggging: print time stats """
        diff = time.time() - self.startTime
        print ""
        print "clock diff: ", diff
        print "error: ", diff-self.total

    def runTimer_int_elapsed(self):
        """ 
        Use sleep() to wait 1sec at a time
        All vars are in integer seconds
        Prints time elapsed 
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
        Prints time remaining
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

    def runTimer_precise(self):
        """
        sleep(1) not accurate bc based on cpu time
        Instead: sleep in incrememnts, keep checking how long it's been
        All vars are in float seconds
        NOTE: time() produces floats in milliseconds
        """
        start =self.startTime
        elapsed = 0.0

        # keep sleeping, until past 1 sec
        startIncr = time.time()
        while True:
            time.sleep(0.001)
            incr = time.time() - startIncr
            if incr>=1.0:
                break

        # NOTE: All vars are in terms of seconds (float)
        #       Also, secCheck is for debugging
        #secCheck = 0.0
        #error = 0.0001
        #self.bellEnd.play()
        #elapsed =time.time() - startTime

        #while not (elapsed>self.timerLen):
            #time.sleep(error*10)
            #elapsed =time.time() - startTime

            # Don't report time right at start
            #if elapsed>error:

            ##Report at each second interval
            #if elapsed%1 > 0 and elapsed%1 <= error:
            #    print elapsed
            #    secCheck +=1
            ##Report at some other interval
            #if elapsed%self.interval>=0 and elapsed%self.interval<=error:
            #    #Don't ring bellInterval at end
            #    if elapsed%self.timerLen>error:
            #        print "bellInterval rings"
                    #self.bellInterval.play()
        #print "bellEnd rings"
        #self.bellEnd.play()


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

