# -*- coding: utf-8 -*-

class MyBlast:
    '''
    Classe que implementa Simple Blast
    '''

    def __init__(self, filename = None, w = 3):
        '''
        Construtor
        '''
        if filename is not None:
            self.readDatabase(filename)
            
        else:
            self.db = []
        self.w = w
        self.map = None

    def readDatabase(self, filename):
        # ... #DONE
        cont = open(filename)
        newdb = []
        
        for i in cont:
            newdb.append(str(i))   
        cont.close()    
        self.db = newdb
    
    def addSequenceDB(self, seq):
        self.db.append(seq)
        
    def buildMap (self, query):
        # ...
        res = {}
        w = self.w
        for i in range(len(query)-w+1):
            k = query[i:i+w]
            if k in res:
                res[k].append(i)
            else:
                res[k] = [i]
        self.map =  res    
            
        
    
    def getHits (self, seq, query):
        # ...
        w = self.w
        m = self.map
        res = []
        for i in range (len(seq)-w+1):
            k= seq[i:i+w]
            if k in m: 
                l = m[k]
                for ind in l:
                    res.append((ind,i))
        return res                
        
    def extendsHit (self, seq, hit, query):
        # ...
        w = self.w
        stq = hit[0]
        sts = hit[1] 
        #move forward
        matfw = 0
        k = 0
        bestk = 0
        
        while 2*matfw >= k  and (stq+w+k) < len(query) and sts+w+k < len(seq):
            if query[stq+w+k] == seq[sts+w+k]:
                matfw+=1
                bestk = k+1
            k+=1
        size = w + bestk
        #move backwards
        k = 0
        matbw = 0
        bestk = 0
        while 2*matbw >= k and stq > k and sts > k:
            if query[stq-k-1] == seq[sts-k-1]:
                matbw+=1
                bestk = k+1
            k+=1
        size+=bestk 
        return (stq-bestk, sts-bestk, size, w+matfw+matbw)
        
        
    
    def hitBestScore(self, seq, query):
        # ...
        #2: O desempate entre iguais "bestScore" é através do que ocorre mais vezes, usando o extendsHit.

        hits = self.getHits(seq, query)
        bestScore = -1.0
        best = ()
        for h in hits:
            ext = self.extendsHit(seq,h,query)
            score = ext[3]
            
            if score > bestScore or (score == bestScore and ext[2] < best[2]):
                bestScore = score
                best = ext
        return best
    
    def bestAlignment (self, query):
        # 3:
        # self:Usado para ter acesso aos atributos e métodos da class myblast
        # query: 
        db = self.db
       
        self.buildMap(query)
        bestScore = -1.0
        res = (0,0,0,0,0)
        for k in range(0, len(db)):
            bestSeq = self.hitBestScore(db[k],query)
            #print("bestseq:",bestSeq)
            
            if bestSeq != ():
                score = bestSeq[3]
                if score > bestScore or (score == bestScore and bestSeq[2] < res[2]):
                    bestScore = score
                    res = bestSeq[0], bestSeq[1], bestSeq[2], bestSeq[3], k
        if bestScore < 0: 
            return ()
        else: 
            return res              

def test1():
    mb = MyBlast("seqBlast.txt",11)
    query2 = "cgacgacgacgacgaatgatg"
    r = mb.bestAlignment(query2)
    print(r)

#4
def test2():
    mb = MyBlast("seqBlast.txt",3)
    f = open("query1.fasta", "r")
    query1 = f.read()
    r = mb.bestAlignment(query1)
    print(r)

test1()
test2()

