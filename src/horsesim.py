from sys import flags, stdin
import math
import re
import queue
import typing
import itertools
# from numpy.core.numeric import outer
input = stdin.readline
import copy

MOD = 1000000007
INF = 122337203685477580

NUMBER_OF_HORSE = 16
#
ticket_sample =[
    (("Win",1),100,10.0),#単勝
    (("Place",1),100,3.0),#複勝
    (("Tierce",1,2,3) ,100,1000.0),#3連単
    (("Trio",1,2,3) ,100,1.0),#3連複
    (("Quinella",1,2),100,1.0), #馬連
    (("Exacta",1,2),100,1.0), #馬単
    (("QuinellaPlace",1,2),100,1.0) #ワイド
    
]

ticket_kind ={
    "Win":0,
    "Place":1,
    "Tierce":2,
    "Trio":3,
    "Quinella":4,
    "Exacta":5,
    "QuinellaPlace":6,
    "単勝":0,
    "複勝":1,
    "三連単":2,
    "三連複":3,
    "馬連":4,
    "馬単":5,
    "ワイド":6
}

myticket = [
    (("三連単",1,2,3),100,2.0) #馬連
]

def ticket_hit(ticket,horse):
    idx = ticket_kind[ticket[0]]
    #あたったらリターンTrueでそうでない場合は一番下でReturn False するようにする
    if idx == 0:#単勝チェック
        if horse[0] == ticket[1]:
            return True
    elif idx == 1:#複勝チェック
        x = ticket[1]
        for y in horse:
            if x == y:
                return True
    elif idx == 2:#三連単
        l = [ticket[1],ticket[2],ticket[3]]
        if l == horse:
            return True
    elif idx == 3:#三連複
        h = copy.copy(horse)
        l = [ticket[1],ticket[2],ticket[3]]
        l.sort()
        h.sort()
        if h == l:
            return True
    elif idx == 4:#馬連
        l = [ticket[1],ticket[2]]
        if (l[0] == horse[0] and l[1] == horse[1]) or (l[0] == horse[1] and l[1] == horse[0]):
            return True 
    elif idx == 5:
        l = [ticket[1],ticket[2]]
        if (l[0] == horse[0] and l[1] == horse[1]):
            return True 
    elif idx == 6:
        if ticket[1] in horse and ticket[2] in horse:
            return True
        
    return False
    
    
def winnning_ticket_fn(data):
    spent_money = 0
    if data == None:
        data = []
    for item in myticket:
        spent_money += item[1]
    print("Spent Money >> ",spent_money)
    data.sort()
    data.reverse()
    cnt = 0
    for i in data:
        
        print("No.",cnt ," >> " ,"return  >> " + str(i[0]), "horce >> " + str(i[1])  )
        cnt += 1
        if cnt == 100:
            break;
            
    return
    

def horse_sim():
    n = NUMBER_OF_HORSE
    winning_ticket = []
    for i1 in range(1,n+1):
        for i2 in range(1,n+1):
            for i3 in range(1,n+1):
                l = [i1,i2,i3]
                if i1 == i2 or i2 == i3 or i3 == i1:
                    continue
                back_money = 0
                for ticket in myticket:
                    if ticket_hit(ticket= ticket[0],horse = l):
                        back_money += ticket[1]*ticket[2]
                        print(l,ticket)
                if back_money > 0:
                    winning_ticket.append((back_money,l))
    
    winnning_ticket_fn(winning_ticket)
    return
    
    
        


if __name__ == '__main__':
    horse_sim()
    
 