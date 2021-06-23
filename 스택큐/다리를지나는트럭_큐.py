def solution(bridge_length, weight, truck_weights):
    answer = 0
    truckqueue=truck_weights
    truckquefront=0
    truckquerear=len(truckqueue)
    runingbridge=[]#kg, endtime queue
    limitweight=weight
    currenttime=1
    despos=0#적재량
    runingtime=bridge_length
    front=0
    while(truckquefront!=truckquerear):
        if truckqueue[truckquefront]+despos<=limitweight:
            despos+=truckqueue[truckquefront]
            runingbridge.append([truckqueue[truckquefront],currenttime+runingtime])
            currenttime+=1
            truckquefront+=1
        else:
            currenttime=runingbridge[front][1]  
        if currenttime==runingbridge[front][1]:
            despos-=runingbridge[front][0]
            front+=1
    answer=runingbridge[-1][-1]
    return answer
