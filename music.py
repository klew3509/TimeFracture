from gamelib import *

def meunMusic():
    pygame.mixer.music.load("WastelandOverdriveLooped(1).mp3")

def playmeunMusic():
    pygame.mixer.music.play(-1,0.0)

def stopmeunMusic():
    pygame.mixer.music.stop()

def loadingMusic():
    pygame.mixer.music.load("loadingmusic.mp3")

def playloadingMusic():
    pygame.mixer.music.play(-1,0.0)

def stoploadingMusic():
    pygame.mixer.music.stop()

def gameMusic():
    pygame.mixer.music.load("TacticalPursuit.mp3")

def playgameMusic():
    pygame.mixer.music.play(-1,0.0)

def stopgameMusic():
    pygame.mixer.music.stop()

def bossMusic():
    pygame.mixer.music.load("Thrust Sequence.mp3")

def playbossMusic():
    pygame.mixer.music.play(-1,0.0)

def stopbossMusic():
    pygame.mixer.music.stop()

def timeslow():
    timeslow.chan=1
    timeslow.file=pygame.mixer.Sound("TimeSlow.wav")

def timeslowPlay(time=0):
    c=pygame.mixer.Channel(1)
    if not c.get_busy():
        c.play(timeslow.file,maxtime=time)

def timeslow1():
    timeslow1.chan=2
    timeslow1.file=pygame.mixer.Sound("TimeSlow1.wav")

def timeslow1Play(time=0):
    c=pygame.mixer.Channel(2)
    if not c.get_busy():
        c.play(timeslow1.file,maxtime=time)

def forcefieldhit():
    forcefieldhit.chan=3
    forcefieldhit.file=pygame.mixer.Sound("forcefieldhit.wav")

def forcefieldhitPlay(time=0):
    c=pygame.mixer.Channel(3)
    if not c.get_busy():
        c.play(forcefieldhit.file,maxtime=time)

def timeblast():
    timeblast.chan=4
    timeblast.file=pygame.mixer.Sound("timeblast.wav")

def timeblast(time=0):
    c=pygame.mixer.Channel(4)
    if not c.get_busy():
        c.play(timeblast.file,maxtime=time)
