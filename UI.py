import tkinter as tk
import random
import sys
import time
Width = 80
reached = 0
score =0
episode =0
flag =0
player = (4, 0)
(x, y) = (5, 5)
walk_reward = -1
w=12
gamma=0.5
alpha=0.3
hasblock=0
actions=[0,1,2,3]
a=[4,4,4,4,0,0]
q={}
for i in range(5):
    for j in range(5):
        for m in range(2):
            for k in range(4):
                q[(i,j,m,k)]=0
pickDrop = [(0,0, 0, "red", 4, 12), (1,0, 3, "red", 4, 12), (2,2, 2, "red", 4, 12), (3,4, 4, "red", 4, 12),
                    (4,4, 4, "green", 0, 12), (5,0, 4, "green", 0, 12)]
terminal = [0,0,0,0,8,8]
def Draw():
    global text,board
    board = tk.Canvas(root, width=x * Width, height=y * Width)
    frame=tk.Frame(root)
    frame.grid(row=0,column=1)
    v = tk.IntVar()
    print(v)
    button1=tk.Radiobutton(frame, text="Experiment1", variable=v, value=1,command=PRandom)
    button2=tk.Radiobutton(frame, text="Experiment2", variable=v, value=2,command=PExploit1)
    button3 = tk.Radiobutton(frame, text="Experiement3", variable=v, value=3,command=PRandom)
    button1.grid(row=1,column=1)
    button2.grid(row=1,column=2)
    button3.grid(row=1,column=3)
    if v.get()==1:
        PRandom()
    if v.get()==2:
        PExploit1()
    if v.get()==3:
        PRandom()
    root.mainloop()
def PExploit1():
    probs=[0.65,0.35]
    r = random.random()
    index = 0
    while (r >= 0 and index < len(probs)):
        r = probs[index] - r
        index += 1
    index = index - 1
    if index == 0:
        PExploit()
    else:
        PRandom()
def PRandom():
    global text,board,me,episode,hasblock
    if episode ==3000:
        for (sx,sy,hasblock,operator) in q:
            qval = q.get((sx,sy,hasblock,operator))
            print (sx," ",sy," ",hasblock," ",operator," ",qval)
        PExploit()
        return
    board.grid(row=0,column=0)
    for i in range(x):
        for j in range(y):
            board.create_rectangle(i * Width, j * Width, (i + 1) * Width, (j + 1) * Width, fill="white", width=1)

    for (pos,i, j, c, d, w) in pickDrop:
        board.create_rectangle(i * Width, j * Width, (i + 1) * Width, (j + 1) * Width, fill=c, width=1)
    val = round(q.get((player[0], player[1], hasblock, 0)),2)
    board.create_text( player[0] * Width + Width * 5 / 10,player[1] * Width + Width * 1 / 10,text=val)
    val =round( q.get((player[0], player[1], hasblock, 1)),2)
    board.create_text(player[0] * Width + Width * 1 / 10, player[1] * Width + Width * 5 / 10, text=val)
    val = round(q.get((player[0], player[1], hasblock, 2)),2)
    board.create_text(player[0] * Width + Width * 5 / 10, player[1] * Width + Width * 9 / 10, text=val)
    val = round(q.get((player[0], player[1], hasblock, 3)),2)
    board.create_text(player[0] * Width + Width * 9 / 10, player[1] * Width + Width * 5 / 10, text=val)
    if hasblock==0:
        me = board.create_rectangle(player[0] * Width + Width * 2 / 10, player[1] * Width + Width * 2 / 10,
                                player[0] * Width + Width * 8 / 10, player[1] * Width + Width * 8 / 10,
                                fill="orange",
                              width=1, tag="me")

    else:
        me = board.create_rectangle(player[0] * Width + Width * 2 / 10, player[1] * Width + Width * 2 / 10,
                                    player[0] * Width + Width * 8 / 10, player[1] * Width + Width * 8 / 10,
                                    fill="pink",
                                    width=1, tag="me")
    direction = random.randint(0, 3)
    move_random(direction)
    episode += 1
    root.after(1,PRandom) # every second...
def PExploit():
    global text, board, me,episode,hasblock
    if episode ==6000:
        print ("-------------------------------------")
        for (sx,sy,hasblock,operator) in q:
            qval = q.get((sx,sy,hasblock,operator))
            print (sx," ",sy," ",hasblock," ",operator," ",qval)

        return
    board.grid(row=0, column=0)
    for i in range(x):
        for j in range(y):
            board.create_rectangle(i * Width, j * Width, (i + 1) * Width, (j + 1) * Width, fill="white", width=1)
    for (pos,i, j, c, d, w) in pickDrop:
        board.create_rectangle(i * Width, j * Width, (i + 1) * Width, (j + 1) * Width, fill=c, width=1)
    val = round(q.get((player[0], player[1], hasblock, 0)), 2)
    board.create_text(player[0] * Width + Width * 5 / 10, player[1] * Width + Width * 1 / 10, text=val)
    val = round(q.get((player[0], player[1], hasblock, 3)), 2)
    board.create_text(player[0] * Width + Width * 1 / 10, player[1] * Width + Width * 5 / 10, text=val)
    val = round(q.get((player[0], player[1], hasblock, 1)), 2)
    board.create_text(player[0] * Width + Width * 5 / 10, player[1] * Width + Width * 9 / 10, text=val)
    val = round(q.get((player[0], player[1], hasblock, 2)), 2)
    board.create_text(player[0] * Width + Width * 9 / 10, player[1] * Width + Width * 5 / 10, text=val)
    if hasblock == 0:
        me = board.create_rectangle(player[0] * Width + Width * 2 / 10, player[1] * Width + Width * 2 / 10,
                                    player[0] * Width + Width * 8 / 10, player[1] * Width + Width * 8 / 10,
                                    fill="orange",
                                    width=1, tag="me")

    else:
        me = board.create_rectangle(player[0] * Width + Width * 2 / 10, player[1] * Width + Width * 2 / 10,
                                    player[0] * Width + Width * 8 / 10, player[1] * Width + Width * 8 / 10,
                                    fill="pink",
                                    width=1, tag="me")
    chooseAction()
    episode += 1
    root.after(1, PExploit)

def chooseAction():
    maxQ=max([getQ(player[0], player[1],hasblock, direct) for direct in actions])
    for direct in actions:
        if maxQ==q[(player[0], player[1],hasblock, direct)]:
            moveTo=direct
    move_random(moveTo)

def move_random(direction):

    if direction == 0:
        call_up()
    elif direction == 1:
        call_down()
    elif direction == 2:
        call_right()
    else:
        call_left()

def call_up():
    try_move(0, -1,0)

def call_left():
    try_move(-1, 0,3)

def call_right():
    try_move(1, 0,2)
def call_down():
    try_move(0, 1,1)
def reset():
    new_x = 4
    new_y = 0
    a=[4,4,4,4,0,0]

def try_move(dx, dy,direct):
    global player, x, y, score, walk_reward,restart,me,hasblock,reached,flag
    new_x = player[0] + dx
    new_y = player[1] + dy
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 8 and a[5] == 8:
        reset()



    if (new_x >= 0) and (new_x < x) and (new_y >= 0) and (new_y < y):
        for (pos, i, j, c, d, w) in pickDrop:
            if player[0] == i and player[1] == j:
                learnSARSA(player[0], player[1], direct, 12, new_x, new_y, hasblock)
                flag = 1

        board.coords(me, new_x * Width + Width * 2 / 10, new_y * Width + Width * 2 / 10,
                     new_x * Width + Width * 8 / 10, new_y * Width + Width * 8 / 10)


        score += -1

        for (pos,i, j, c, d, w) in pickDrop:
            if new_x == i and new_y == j:
                score += w
                if c=="red" and hasblock==0 and d>0:


                    hasblock = 1
                    lst = list(pickDrop[pos])
                    lst[4]=lst[4]-1
                    a[pos]=a[pos] -1
                    pickDrop[pos] = tuple(lst)

                elif c=="green" and hasblock==1 and d<8:

                    hasblock = 0
                    lst = list(pickDrop[pos])
                    lst[4] = lst[4] + 1
                    a[pos] = a[pos] + 1
                    pickDrop[pos] = tuple(lst)

        if flag ==0:
            learnSARSA(player[0], player[1], direct, -1, new_x, new_y, hasblock)


        player = (new_x, new_y)
        flag=0


def getQ(statex, statey, hasblock,action):
    return q.get((statex,statey,hasblock, action))
def learn(statex1,statey1,direct,reward,statex2,statey2,hasblock):
    maxqnew=max([getQ(statex2,statey2,hasblock, direct) for direct in actions])
    #learnQ(statex1,statey1, direct, reward, reward + gamma * maxqnew,hasblock)
    learnQ(statex1, statey1, direct, reward, reward + gamma * maxqnew, hasblock)

def learnQ(statex, statey, action, reward, value,hasblock):
    '''
    Q-learning:
        Q(s, a) += alpha * (reward(s,a) + max(Q(s') - Q(s,a))
    '''
    oldv = q.get((statex, statey,hasblock, action), None)
    if oldv is None:
        q[(statex, statey,hasblock, action)] = reward
    else:
        q[(statex, statey, hasblock, action)] = (1 - alpha) * oldv + alpha * value
        #q[(statex, statey,hasblock, action)] = oldv + alpha * (value - oldv)

def SARSA(statex, statey, action, reward, value,hasblock):
    oldv = q.get((statex, statey, hasblock, action), None)
    if oldv is None:
        q[(statex, statey,hasblock, action)] = reward
    else:
        q[(statex, statey,hasblock, action)] = oldv + alpha * (value - oldv)

def learnSARSA(statex1,statey1,direct,reward,statex2,statey2,hasblock):
    qnext = getQ(statex2,statey2,hasblock, direct)
    SARSA(statex1, statey1, direct,reward, reward + gamma * qnext,hasblock)




root=tk.Tk()
Draw()
#PRandom()
