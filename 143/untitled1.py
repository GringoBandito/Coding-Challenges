
#

def drawdowncalc(rets, N):
    # Write your code here
    
    drawdowns = []
    peak = -10000
    trough = 10000
    discovered = 0    
    peakindices = [0]
    drawdowntotals = []
    
    
    for i in range(len(rets)):
        if rets[i] >= peak:
            if discovered == 1:
                drawdowns.append((peak,trough))
                peak = rets[i]
                trough = 10000 
                discovered = 0
                peakindices.append(i)
                
            else:
                peak = rets[i]
                
            
        elif rets[i] < trough:
            trough = rets[i]
            discovered = 1
            
    
    if peak != -10000 and trough != 10000:
        drawdowns.append((peak,trough))
        peakindices.append(len(rets))
    
    
    if len(drawdowns) < N:
        return len(drawdowns)
    
    
    for i in range(len(peakindices)-1):
        val1 = peakindices[i] + 1
        val2 = peakindices[i+1] 
        
        lst = rets[val1:val2]
        dtotal = 1
        print(lst)
        for j in lst:
            dtotal*= (1+j)
            
        dtotal -=1
        
        drawdowntotals.append(round(dtotal,4))
        
    
    drawdowntotals.sort()
    
    return drawdowntotals[N-1]

print(drawdowncalc([0.01,-0.04,0.05,-0.01,-0.01,0.01],3))