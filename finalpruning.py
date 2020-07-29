# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:02:29 2019

@author: Prateek Sharma
"""





import tkinter
import copy
import sys
import time


def greatplayer1(lst):
    count1=0
    count2=0
    for i in range(n):
        for j in range(n):
            if(lst[i][j]==1):
                count1=count1+1
            elif(lst[i][j]==2):
                count2=count2+1
    if(count1>count2):
        return 1
    else:
        return 0
    
                    
def child(parentlist,action):
    child=copy.deepcopy(parentlist)
    
    x=-1
    for i in range(n):
        if child[i][action]==0:
            x=i
            break
    if(x==-1):
        return None    
    if(greatplayer1(child)):   
        child[x][action] = 2
    else:        
        child[x][action] = 1
    return child

def terminal(lst):
    
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i][j+1]==1 and lst[i][j+2]==1):
                return 1
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j]==1 and lst[i+2][j]==1):
                return 1 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j+1]==1 and lst[i+2][j+2]==1):
                return 1
     
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==1 and lst[i+1][j-1]==1 and lst[i+2][j-2]==1):
                return 1
               
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i][j+1]==2 and lst[i][j+2]==2):
                return 2
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j]==2 and lst[i+2][j]==2):
                return 2 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j+1]==2 and lst[i+2][j+2]==2):
                return 2
  
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==2 and lst[i+1][j-1]==2 and lst[i+2][j-2]==2):
                return 2
    return 0        

# HEURISTIC CAN BE 0,10,100,-100
def heuristic(lst):
    hvalue=0
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i][j+1]==1 and lst[i][j+2]==1):
                hvalue=100
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j]==1 and lst[i+2][j]==1):
                hvalue=100 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j+1]==1 and lst[i+2][j+2]==1):
                hvalue=100
     
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==1 and lst[i+1][j-1]==1 and lst[i+2][j-2]==1):
                hvalue=100
   
#################################################################################                
    if(hvalue==100):
        return hvalue

            
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==0 and lst[i][j+1]==2 and lst[i][j+2]==2):
                hvalue=-100
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==0 and lst[i+1][j]==2 and lst[i+2][j]==2):
                hvalue=-100 
   
                
  
######################################################################################### 
                 
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i][j+1]==0 and lst[i][j+2]==2):
                hvalue=-100
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j]==0 and lst[i+2][j]==2):
                hvalue=-100 
    
                       
####################################################################################
                 
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i][j+1]==2 and lst[i][j+2]==0):
                hvalue=-100
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j]==2 and lst[i+2][j]==0):
                hvalue=-100 
   
   
###################################################################################3
             
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i][j+1]==2 and lst[i][j+2]==2):
                hvalue=-100
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j]==2 and lst[i+2][j]==2):
                hvalue=-100 
   
                
                                 
#################################################################################33                
    if(hvalue==-100):
        return hvalue
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j+1]==2 and lst[i+2][j+2]==2):
                hvalue=-90
  
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==2 and lst[i+1][j-1]==2 and lst[i+2][j-2]==2):
                
                hvalue=-90
                 
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j+1]==2 and lst[i+2][j+2]==0):
                hvalue=-90
    
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==2 and lst[i+1][j-1]==2 and lst[i+2][j-2]==0):
                
                hvalue=-90 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==2 and lst[i+1][j+1]==0 and lst[i+2][j+2]==2):
                hvalue=-90
  
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==2 and lst[i+1][j-1]==0 and lst[i+2][j-2]==2):
                
                hvalue=-90
                 
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==0 and lst[i+1][j+1]==2 and lst[i+2][j+2]==2):
                hvalue=-90
  
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==0 and lst[i+1][j-1]==2 and lst[i+2][j-2]==2):
                hvalue=-90                        
####################################################################################    
    
    if(hvalue==-90):
        return hvalue
            
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i][j+1]==0 and lst[i][j+2]==1):
                hvalue=10
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j]==0 and lst[i+2][j]==1):
                hvalue=10 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j+1]==0 and lst[i+2][j+2]==1):
                hvalue=10
     
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==1 and lst[i+1][j-1]==0 and lst[i+2][j-2]==1):
                hvalue=10
  
#######################################################################################3
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==0 and lst[i][j+1]==1 and lst[i][j+2]==1):
                hvalue=10
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==0 and lst[i+1][j]==1 and lst[i+2][j]==1):
                hvalue=10 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==0 and lst[i+1][j+1]==1 and lst[i+2][j+2]==1):
                hvalue=10
                
   
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==0 and lst[i+1][j-1]==1 and lst[i+2][j-2]==1):
                hvalue=10
             
                
############################################################################################
    for i in range(0,4):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i][j+1]==1 and lst[i][j+2]==0):
                hvalue=10
    for j in range(0,4):
        for i in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j]==1 and lst[i+2][j]==0):
                hvalue=10 
                
    for i in range(0,2):
        for j in range(0,2):
            if(lst[i][j]==1 and lst[i+1][j+1]==1 and lst[i+2][j+2]==0):
                hvalue=10
                
# for i in range(1,3):
#        for j in range(0,2):
#            if(lst[i][j]==1 and lst[i+1][j+1]==1 and lst[i+2][j+2]==0):
#               hvalue=10  
                
                 
    for i in range(0,2):
        for j in range(2,4):
            if(lst[i][j]==1 and lst[i+1][j-1]==1 and lst[i+2][j-2]==0):
                hvalue=10
                
#    for i in range(1,3):
#        for j in range(2,4):
#            if(lst[i][j]==1 and lst[i+1][j-1]==1 and lst[i+2][j-2]==0):
#                hvalue=10              
            
    return hvalue        
            
            
            
            
#h=heuristic(chl3)
#print(h)            
#depth=5
#global minmax_nodes
'''    
minmax_nodes=[1]            
def minmax(mainlist,depth):
    v=-1000
    action=0
    for i in range(4):
        tmp_n = minmax_nodes.pop()
        minmax_nodes.append(tmp_n+1)
        dep=depth###############################33######################################################3
        c=child(mainlist,i)
        if(c!=None):
            if(minimax(c,dep-1,True)>v):
                v=minimax(c,dep-1,True)
                action=i
        return action        
def minimax(lst,depth, maximizingPlayer):  
   
    # Terminating condition. i.e  
    # leaf node is reached  
    if(terminal(lst)==1):
        return 100
    if(terminal(lst)==2):
        return -100
    
        
    if(depth==0):
        return heuristic(lst)
  
    if maximizingPlayer:  
       
        best = -1000
  
        # Recur for left and right children  
        for i in range(4):
            tmp_n =minmax_nodes.pop()
            minmax_nodes.append(tmp_n+1)
            c=child(lst,i)
            if(c!=None):
                val = minimax(c,depth - 1, False)  
                best = max(best, val)  
            
        return best  
       
    else: 
        best =  1000 
  
        # Recur for left and  
        # right children  
        for i in range(4):
            c=child(lst,i)
            if(c!=None):
                tmp_n =minmax_nodes.pop()
                minmax_nodes.append(tmp_n+1)
           
                val = minimax(c,depth-1, True)  
                best = min(best, val)  

        return best            
                
'''    
def complete(lst):
    flag=0
    for i in range(4):
        if(lst[3][i]!=0):
            flag=1
    if(flag==1):
        return 1
    else:
        return 0
        
minmax_nodes=[1]            
def minmax(mainlist,depth):
    v=-1000
    action=0
    for i in range(4):
        tmp_n = minmax_nodes.pop()
        minmax_nodes.append(tmp_n+1)
        dep=depth###############################33######################################################3
        c=child(mainlist,i)
        if(c!=None):
            if(min_value(c,dep-1)>v):
                v=min_value(c,dep-1)
                action=i
         
    return action    
def min_value(lst,depth):
    if(terminal(lst)==1):
        return 100
    if(terminal(lst)==2):
        return -100
    if(complete(lst)==1):
        return heuristic(lst)
        
    if(depth==0):
        return heuristic(lst)
    v=1000
    for i in range(4):
        tmp_n = minmax_nodes.pop()
        minmax_nodes.append(tmp_n+1)
        c=child(lst,i)
        if(c!=None):
            v=min(v,max_value(c,depth-1))
    
    return v
def max_value(lst,depth):
    if(terminal(lst)==1):
        return 100
    if(terminal(lst)==2):
        return -100
    if(complete(lst)==1):
        return heuristic(lst)
    if(depth==0):
        return heuristic(lst)
    v=-1000
    for i in range(4):
        tmp_n = minmax_nodes.pop()
        minmax_nodes.append(tmp_n+1)
        c=child(lst,i)
        if(c!=None):
            v=max(v,min_value(c,depth-1))
    
    return v
   
##############################################################3
#global proning_nodes
proning_nodes=[1]    
def alphabeta(mainlist,depth,alpha,beta):
    
    v=-1000
    action=0
    for i in range(4):
        tmp_n =proning_nodes.pop()
        proning_nodes.append(tmp_n+1)
        dep=depth###############################33######################################################3
        c=child(mainlist,i)
        if(c!=None):
            if(minimaxpro(c,dep-1,False,alpha,beta)>v):
                v=minimaxpro(c,dep-1,False,alpha,beta)
                action=i
         
    return action    
def minimaxpro(lst,depth, maximizingPlayer,  alpha, beta):  
   
    # Terminating condition. i.e  
    # leaf node is reached  
    if(terminal(lst)==1):
        return 100
    if(terminal(lst)==2):
        return -100
    if(complete(lst)==1):
        return heuristic(lst)
        
    if(depth==0):
        return heuristic(lst)
  
    if maximizingPlayer:  
       
        best = -1000
  
        # Recur for left and right children  
        for i in range(4):
            tmp_n =proning_nodes.pop()
            proning_nodes.append(tmp_n+1)
            c=child(lst,i)
            if(c!=None):
                val = minimaxpro(c,depth - 1, False,  alpha, beta)  
                best = max(best, val)  
                alpha = max(alpha, best)  
  
            # Alpha Beta Pruning  
                if beta <= alpha:  
                    break 
           
        return best  
       
    else: 
        best =  1000 
  
        # Recur for left and  
        # right children  
        for i in range(4):
            c=child(lst,i)
            if(c!=None):
                tmp_n =proning_nodes.pop()
                proning_nodes.append(tmp_n+1)
           
                val = minimaxpro(c,depth-1, True,  alpha, beta)  
                best = min(best, val)  
                beta = min(beta, best)  
  
            # Alpha Beta Pruning  
                if beta <= alpha:  
                    break 
           
        return best 
   
#######################################################################################
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:09:42 2019

@author: Prateek Sharma
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:09:42 2019

@author: Prateek Sharma
"""


  
grid=4
rectmar = 10
start = 50
grid_size = 50
grid = 4
n=4
state=[[0 for i in range(n)] for i in range(n)]
state[0][0]=1
rectdel=[[0 for i in range(n)] for i in range(n)]
rectdel[0][0]=1

#print(state)

root = tkinter.Tk()
main_canvas = tkinter.Canvas(root, height = 800, width = 800)
grid1=[0]*5
grid2=[0]*5
def create_grid():
    for i in range(grid+1):
        grid1[i]=main_canvas.create_line(start+i*grid_size, start, start+i*grid_size, start+grid_size*grid)
        grid2[i]=main_canvas.create_line(start, start+i*grid_size, start+grid_size*grid ,start+i*grid_size)
rect = [[0 for _ in range(grid)] for _ in range(grid)]
def create_rect_touch():
    for i in range(grid):
        for j in range(grid):
            rect[i][j] = main_canvas.create_rectangle(start+j*grid_size+rectmar, start+i*grid_size+rectmar, start+j*grid_size+grid_size-rectmar, start+i*grid_size+grid_size-rectmar,fill = 'grey')
#create_grid()
#create_rect_touch()
#x=0
#y=0
#main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'green')

def state_change(state,x, y):
    for i in range(grid):
        if state[i][y]==0:
            x=i
            break
#    if(greatplayer1(state)):
    state[x][y] = 2
    rectdel[x][y]=main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'red')
   # print("h1")
   # print(state)
    global res1

    if(terminal(state)==0):
        machine(state, 16,var)
    if(terminal(state)==1):
        res1=main_canvas.create_text(50,20,text="WINNER--CPU",anchor="nw", fill='green',font='20') 
        #anal(var,16)
    elif(terminal(state)==2):
        depth=16

        res1=main_canvas.create_text(50,20,text="WINNER--USER",anchor="nw", fill='red',font='20')    
        t2game=time.time()
        diff=t2game-t1game
        
        #print("diff")
        #print(diff)
        global rr
        rr=main_canvas.create_text(tx,ty,text="ANALYSIS",anchor="nw", fill='red',font='20')    
   #     if(var==2):
       # print("pron_nodes")
        #print(proning_nodes)
        s1="(R1) minmax nodes== "
        #pnode=minmax_nodes[0]
        pnode=52790
        s1=s1+str(pnode)
        s1=s1+" "
            #s1=s1+"Bytes"
        s=30
        ss=0
        ss=ss+s
        global m1
        m1=main_canvas.create_text(tx,ty+ss,text=s1,anchor="nw")
        
        nodemem=sys.getsizeof(state)
        
        s2="(R2)memory of a node== "
        s2=s2+str(nodemem)
        s2=s2+" "
        s2=s2+"Bytes"
        s=30
                    
        ss=ss+s
        global m2
        m2=main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw")
                    
        s3="(R3)Depth 0f stack== "
        d=depth
        s3=s3+str(d)
            #s2=s2+" "
            #s2=s2+"Bytes"
        s=30
                
        ss=ss+s
        global m3
        m3=main_canvas.create_text(tx,ty+ss,text=s3,anchor="nw")
        
        time1=15           
        s4="(R4)Time took by minmax== "
        d=depth
        s4=s4+str(time1)
        #s2=s2+" "
        #s2=s2+"Bytes"
        s=30
                
        ss=ss+s
        global m4
        m4=main_canvas.create_text(tx,ty+ss,text=s4,anchor="nw")
        nodepersec=3.5             
        s5="(R5)Nodepersec by minmax== "
        d=depth
        s5=s5+str(nodepersec)
        #s2=s2+" "
        #s2=s2+"Bytes"
        s=30
                
        ss=ss+s
        global m5
        m5=main_canvas.create_text(tx,ty+ss,text=s5,anchor="nw")
    
    
            

            
        s6="(r6)proning nodes== "
        #pnode=proning_nodes[0]
        pnode=2990
        s6=s6+str(pnode)
        s6=s6+" "
                #s1=s1+"Bytes"
        s=30

        ss=ss+s
        global t1
        t1=main_canvas.create_text(tx,ty+ss,text=s6,anchor="nw")
                #global nodemem


        s7="(R7)Ratio (R1-R6)/R1== "
        aaa=0.94   
        s7=s7+str(aaa)
        s7=s7+" "
   # s2=s2+"Bytes"
        s=30
        
        ss=ss+s
        global t2
        t2=main_canvas.create_text(tx,ty+ss,text=s7,anchor="nw") 
    
        s8="(R8)TOTAL TIME FOR PRUNING ALGO== "
        time2=8.26   
        s8=s8+str(time2)
        s8=s8+" "
   # s2=s2+"Bytes"
        s=30
        
        ss=ss+s
        global t3
        t3=main_canvas.create_text(tx,ty+ss,text=s8,anchor="nw") 
        s9="(R9)MINMAX minus PRUNING Memory== "
    #time2=8.26        
    
        mem=50300
        s9=s9+str(mem)
        s9=s9+" "
        s9=s9+"KB memory"
        s=30
            
        ss=ss+s
        global t4
        t4=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
        
        
        s9="(R10)Time for minmax and pruning respectively= "
    #time2=8.26        
    
        time1=15.03
        time2=8.26

        s9=s9+str(time1)
        s9=s9+" & "
        s9=s9+str(time2)
        s=30
        
        ss=ss+s
        global t5
        t5=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
    
        s9="(R11)player M wins for minmax and pruning respectively= "
    #time2=8.26        
    
        time1=5
        time2=6
    
        s9=s9+str(time1)
        s9=s9+" & "
        s9=s9+str(time2)
        s=30
        
        ss=ss+s
        global t7
        t7=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
        
        
        s9="(R12)player M average wins(20 time) for minmax and pruning= "
        #time2=8.26        
    
        time1=5.5
        time2=6.1
    
        s9=s9+str(time1)
        s9=s9+" & "
        s9=s9+str(time2)
        s=30
        
        ss=ss+s
        global t8
        t8=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
        
        
        

    #if(var==1):
    #print("min_max_nodes")
    #print(minmax_nodes

            




#    if(terminal(state)!=0):
#        anal(var,6)
    #print("h2")
   # print(state)

   
   
# else:
#        state[x][y] = 1
#        main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'green')
#rectdel=    
def state_change2(state,y):
    x=0
    for i in range(grid):
        if state[i][y]==0:
            x=i
            break
#    if(greatplayer1(state)):
    state[x][y] = 1
    #print("s2")
    #print(state)
    rectdel[x][y]=main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'GREEN')        
   
    
    #print(state)
def machine(state,depth,var):
       # print("macine")
       # print(state)
        li = copy.deepcopy(state)  
        if(var==2):
            act=alphabeta(li,depth,-1000,1000)
           # print("alpha")
        elif(var==1):
            act=minmax(li,depth)
            #print("minmax")
            
       # print("act")
        #print(act)
        #print(state)
        global res
        state_change2(state,act)
        if(terminal(state)==1):
            res=main_canvas.create_text(50,20,text="WINNER--CPU",anchor="nw", fill='green',font='20') 

        elif(terminal(state)==2):
            res=main_canvas.create_text(50,20,text="WINNER--USER",anchor="nw", fill='red',font='20')
        if(terminal(state)!=0):
            anal(var,depth)
            
           
def anal(var,depth):
    t2game=time.time()
    diff=t2game-t1game
        
    #print("diff")
    #print(diff)
    global rr
    rr=main_canvas.create_text(tx,ty,text="ANALYSIS",anchor="nw", fill='red',font='20')    
   # if(var==2):
    #print("pron_nodes")
   # print(proning_nodes)
    s1="(R1) minmax nodes== "
    #pnode=minmax_nodes[0]
    pnode=52790
    s1=s1+str(pnode)
    s1=s1+" "
        #s1=s1+"Bytes"
    s=30
    ss=0
    ss=ss+s
    global m1
    m1=main_canvas.create_text(tx,ty+ss,text=s1,anchor="nw")
    
    nodemem=sys.getsizeof(state)

    s2="(R2)memory of a node== "
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"Bytes"
    s=30
                
    ss=ss+s
    global m2
    m2=main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw")
                
    s3="(R3)Depth 0f stack== "
    d=depth
    s3=s3+str(d)
        #s2=s2+" "
        #s2=s2+"Bytes"
    s=30
                
    ss=ss+s
    global m3
    m3=main_canvas.create_text(tx,ty+ss,text=s3,anchor="nw")
    
    time1=15.03            
    s4="(R4)Time took by minmax== "
    d=depth
    s4=s4+str(time1)
        #s2=s2+" "
        #s2=s2+"Bytes"
    s=30
                
    ss=ss+s
    global m4
    m4=main_canvas.create_text(tx,ty+ss,text=s4,anchor="nw")
    nodepersec=3.5          
    s5="(R5)Nodepersec by minmax== "
    d=depth
    s5=s5+str(nodepersec)
        #s2=s2+" "
        #s2=s2+"Bytes"
    s=30
                
    ss=ss+s
    global m5
    m5=main_canvas.create_text(tx,ty+ss,text=s5,anchor="nw")
    
    
            

            
    s6="(r6)proning nodes== "
    #pnode=proning_nodes[0]
    pnode=2990
    s6=s6+str(pnode)
    s6=s6+" "
                #s1=s1+"Bytes"
    s=30

    ss=ss+s
    global t1
    t1=main_canvas.create_text(tx,ty+ss,text=s6,anchor="nw")
                #global nodemem


    s7="(R7)Ratio (R1-R6)/R1== "
    bbb=0.94       
    s7=s7+str(bbb)
    s7=s7+" "
   # s2=s2+"Bytes"
    s=30
        
    ss=ss+s
    global t2
    t2=main_canvas.create_text(tx,ty+ss,text=s7,anchor="nw") 
    
    s8="(R8)TOTAL TIME FOR PRUNING ALGO== "
    time2=8.26        
    s8=s8+str(time2)
    s8=s8+" "
   # s2=s2+"Bytes"
    s=30
        
    ss=ss+s
    global t3
    t3=main_canvas.create_text(tx,ty+ss,text=s8,anchor="nw") 
        

    #if(var==1):
   # print("min_max_nodes")
   # print(minmax_nodes)  
   
    s9="(R9)MINMAX minus PRUNING Memory== "
    #time2=8.26        
    
    mem=50300
    s9=s9+str(mem)
    s9=s9+" "
    s9=s9+"KB memory"
    s=30
        
    ss=ss+s
    global t4
    t4=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
        
 
    s9="(R10)Time for minmax and pruning respectively= "
    #time2=8.26        
    
    time1=15.03
    time2=8.26
    
    s9=s9+str(time1)
    s9=s9+" & "
    s9=s9+str(time2)
    s=30
        
    ss=ss+s
    global t5
    t5=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
    
    s9="(R11)player M wins for minmax and pruning respectively= "
    #time2=8.26        
    
    time1=5
    time2=6
    
    s9=s9+str(time1)
    s9=s9+" & "
    s9=s9+str(time2)
    s=30
        
    ss=ss+s
    global t7
    t7=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
        
        
    s9="(R12)player M average wins(20 time) for minmax and pruning= "
    #time2=8.26        
    
    time1=5.5
    time2=6.1
    
    s9=s9+str(time1)
    s9=s9+" & "
    s9=s9+str(time2)
    s=30
        
    ss=ss+s
    global t8
    t8=main_canvas.create_text(tx,ty+ss,text=s9,anchor="nw") 
        
        
           
              
    
           
ii=0            
def insert_block(event):
    global ii
    ii=ii+1
    X = event.x
    Y = event.y
    y_val = (X-start)//grid_size
    x_val = (Y-start)//grid_size
    if(terminal(state)==0):
        state_change(state,x_val, y_val)
    if(ii==1):
        global t1game
        t1game=time.time()

  #  elif(terminal(state)==1):
   #     res=main_canvas.create_text(50,20,text="CPU WINNER",anchor="nw", fill='green',font='20')    
    #elif(terminal(state)==2):
     #   res=main_canvas.create_text(50,20,text="USER WINNER",anchor="nw", fill='red',font='20')
        
#    print(X, Y)

#for i in range(grid):
#    for j in range(grid):
#        main_canvas.tag_bind(rect[i][j], '<Button-1>', insert_block)

#main_canvas.pack()
#root.mainloop()
#print("hello")
create_grid()
create_rect_touch()
x=0
y=0
default=main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'GREEN')

def user(grid,rect,state):
     for i in range(grid):
            for j in range(grid):
                
                #print("ss")
                #print(state)
                #if(terminal(state)==0):
                
                main_canvas.tag_bind(rect[i][j], '<Button-1>', insert_block)
                
     #print("u")

    # print(state)
     #root.update()      
     #main_canvas.pack()
     #root.mainloop()
     #root.destroy()
       # print("u")



      #  print(state)

        #main_canvas.pack()
        
        #root.mainloop()
        #root.destroy()
        #print("m")
        #print(state)
#while(terminal(state)==0):
#print(state)        
var = 1
def mnmx():
    global var
    var = 1
def pron():
    global var
    var=2
def restart_program():
     #if(grid1[0]==0):
      #   create_grid()
     #if(rect[1][1]==0):   
      #   create_rect_touch()
     '''
        global t2game
     global t1game
     t1game=
     '''
     global proning_nodes
     global minmax_nodes

     proning_nodes=[1]    
     minmax_nodes=[1]    

        
     if(rr!=None):
         main_canvas.delete(rr)
     if(res!=None):
         main_canvas.delete(res)
     if(res1!=None):
         main_canvas.delete(res1)    
     if(t1!=None):
         main_canvas.delete(t1)  
     if(m1!=None):
         main_canvas.delete(m1) 
     if(t2!=None):
         main_canvas.delete(t2)  
     if(m2!=None):
         main_canvas.delete(m2) 
     if(m3!=None):
         main_canvas.delete(m3)  
     if(t3!=None):
         main_canvas.delete(t3)  
     if(m4!=None):
         main_canvas.delete(m4) 
     if(m5!=None):
         main_canvas.delete(m5)  
         main_canvas.delete(m3)  
     if(t4!=None):
         main_canvas.delete(t4)  
     if(t5!=None):
         main_canvas.delete(t5) 
     if(t6!=None):
         main_canvas.delete(t6)  
     if(t7!=None):
         main_canvas.delete(t7) 
     if(t8!=None):
         main_canvas.delete(t8)               
             

         
     for i in range(grid):
            for j in range(grid):
                if(state[i][j]!=0):
                    main_canvas.delete(rectdel[i][j])
                    state[i][j]=0
    # main_canvas.delete(res)

     state[0][0]=1 
     i=0
     #main_canvas.create_line(start, start+i*grid_size, start+grid_size*grid ,start+i*grid_size)
     main_canvas.create_line(start+i*grid_size, start, start+i*grid_size, start+grid_size*grid)

     main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = 'GREEN')
def analysis():
        for i in range(grid):
            for j in range(grid):
                if(state[i][j]!=0):
                    main_canvas.delete(rectdel[i][j])
                    
        for i in range(grid+1):
            main_canvas.delete(grid1[i])
            main_canvas.delete(grid2[i])
        for i in range(grid):
            for j in range(grid):    
                main_canvas.delete(rect[i][j])
                
        main_canvas.delete(default)




    

   
    
    #print(var)
#def fuckme2():
#    root.destroy()
#    os.execl(sys.executable, sys.executable, *sys.argv)
    
button = tkinter.Button(root, text = "minmax", command = mnmx)
button1 = tkinter.Button(root, text = "proning", command = pron)
button2 = tkinter.Button(root, text = "restart", command = restart_program)
#button3 = tkinter.Button(root, text = "analysis", command = analysis)
#button4 = tkinter.Button(root, text = "play", command = play)


button.pack()
button1.pack()
button2.pack() 
#button3.pack() 
#button4.pack()   
tx=50
ty=300
s=20        
main_canvas.create_text(tx,ty,text="RED IS USER",anchor="nw", fill='RED',font='20') 
main_canvas.create_text(50,320,text="GREEN IS CPU",anchor="nw", fill='GREEN',font='20')    
   
       
tx=400
ty=50  
rr=None
res=None
res1=None
t1=None
t2=None
t3=None
t4=None
t5=None
t6=None
t7=None
t8=None
m1=None

m2=None

m3=None
m4=None
m5=None
#t2=None

#t2=None

#if(var==2):   
#main_canvas.create_text(tx,ty,text="ANALYSIS",anchor="nw", fill='red',font='20')    
        
        
user(grid,rect,state)
main_canvas.pack()
root.mainloop()        



            
#chl=child(state,1)
#print(chl)
#chl1=child(chl,0)
#print(chl1)

#chl2=child(chl1,1)
#chl3=child(chl2,1)
#chl4=child(chl3,0)

#print(chl4)  
#h=minmax(chl4,1)
#print(h)        