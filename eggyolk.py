import checkyrsai
import gamerunner

ai1 = checkyrsai.CheckyrsAI(1)
ai1.Initialise( True )

ai2 = checkyrsai.CheckyrsAI(-1)
ai2.Initialise( True )

gr = gamerunner.Gamerunner()
gr.initialise(ai1,ai2)

while gr.continueGame():
    pass

print("game over")
