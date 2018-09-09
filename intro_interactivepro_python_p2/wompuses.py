
counter=0 


def regeneration(rate):
    sw_t=[1000]
    fw_t=[1]
   
    while sw_t[-1] > fw_t[-1]:
        global counter
        counter += 1
        sw_t.append(((sw_t[-1]*rate)-(sw_t[-1]*rate*.4))) 
       
        fw_t.append(((fw_t[-1]*rate)-(fw_t[-1]*rate*.3)))
   

    print "After "+str(counter)+" years the slow wumpus population is "+str(sw_t[-1])
    print "After "+str(counter)+" years the fast wumpus population is "+str(fw_t[-1])



regeneration(2) 