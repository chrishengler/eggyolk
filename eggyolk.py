import checkyrsai
import gamerunner

def getScore(ai):
  return ai[1]

def play(ai1,ai2):
    gr = gamerunner.Gamerunner()
    gr.initialise(ai1,ai2)
    while gr.continueGame():
        pass
    return gr

def league(ailist):
    for ind1,p1 in enumerate(ailist):
        for ind2,p2 in enumerate(ailist):
            if ind1==ind2:
                continue
            gr = play(p1[0],p2[0])
            p1[1]+=gr.getPiecesPlayer(1)
            p2[1]+=gr.getPiecesPlayer(-1)
            if gr.isDraw():
                p1[1]+=6
                p2[1]+=6
            elif gr.getWinner()==1:
                p1[1]+=20
            else:
                p2[1]+=20

    ailist.sort(key=getScore,reverse=True)
    return ailist

def printTable(table):
    for entry in table:
        print(str(entry[2]) + ': ' + str(entry[1]))

firstGen = []

for i in range(0,3):
    ai = checkyrsai.CheckyrsAI()
    ai.Initialise( True )
    firstGen.append( [ai,0,i] )

printTable(league(firstGen))
