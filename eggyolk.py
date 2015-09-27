import random

import checkyrsai
import gamerunner

createdAI=1 #global vartracking created AIs, hack until internal IDs in checkyrs

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

def select(table):
    total = sum(entry[1] for entry in table)
    r = random.uniform(0,total)
    x=0
    for entry in table:
        x+=entry[1]
        if r<=x:
            return entry
            break

def newGen(table):
    global createdAI
    gen = []
    gen.append( [table[0][0],0,table[0][2] ] )
    gen.append( [table[1][0],0,table[0][2] ] )
    for i in range(2,5):
        gen.append( [select(table)[0].breed(select(table)[0]) , 0, createdAI] )
        createdAI+=1
    for i in range(5,6):
        ai = checkyrsai.CheckyrsAI()
        ai.Initialise( True )
        gen.append( [ai , 0, createdAI] )
        createdAI+=1
    return gen

currentGen = []
numGens = 5

for i in range(0,6):
    ai = checkyrsai.CheckyrsAI()
    ai.Initialise( True )
    currentGen.append( [ai,0,i] )

while numGens:
    numGens-=1
    currentGen = league(currentGen)
    print('table: (' +str(numGens) +' gens remaining)' )
    printTable(currentGen)
    currentGen[0][0].save('/tmp/round'+str(5-numGens)+'_1st.cai')
    currentGen[1][0].save('/tmp/round'+str(5-numGens)+'_2nd.cai')
    currentGen = newGen(currentGen)
