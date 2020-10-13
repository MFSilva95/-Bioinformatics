#Marina Gonçalves up201305591
from PairwiseAlignment import PairwiseAlignment
from MyAlign import MyAlign
from MySeq import MySeq
from SubstMatrix import SubstMatrix

class MultipleAlignment():

    def __init__(self, seqs, alignseq):
        self.seqs = seqs # list of MySeq objects
        self.alignpars = alignseq # PairwiseAlignment objects
    
    def num_seqs(self):
        return len(self.seqs)
    
    def add_seq_alignment (self, alignment, seq):
        #....
        #adds new sequences to existing alignments. It is called in each iteration of the main algorithm.
        #It receives as input an existing alignment and a new sequence.
        res = []
        for i in range(len(alignment.listseqs)+1):
            res.append("")
        # create consensus from give alignments
        cons = MySeq(alignment.consensus(),alignment.al_type)
        self.alignpars.needleman_Wunsch(cons, seq)
        align2 = self.alignpars.recover_align()
        orig = 0
        for i in range(len(align2)):
            if align2[0,i]== '-':
                for k in range(len(alignment.listseqs)):
                    res[k] += "-"
            else:
                for k in range(len(alignment.listseqs)):
                    res[k] += alignment[k,orig]
                orig+=1
        res[len(alignment.listseqs)] = align2.listseqs[1]
        return MyAlign(res, alignment.al_type)  
    
    def align_consensus(self):
        #...
        self.alignpars.needleman_Wunsch(self.seqs[0], self.seqs[1])
        res = self.alignpars.recover_align()
        for i in range(2, len(self.seqs)):
            res = self.add_seq_alignment(res, self.seqs[i])
        return res
        
    def ScoreColumn(self, charsCol):
        # ...
        ''' Write a method ScoreColumn(self, charsCol) to add to the MultipleAlign class that allows to calculate the score 
        of each column in the alignment (charsCol is a list of characters from the column of the alignment that can be 
        retrieved using the method column from the class MyAlign). The score is calculated using the Sum of Pairs (SP) approach,
         i.e. the score will be the sum of the scores of each pair of characters in the alignment. 
         If two gaps are found in each pair then the score will be zero. '''
        #
            
    def scoreSP (self, alignment):
        #
   

def printMat (mat):
    for i in range(0, len(mat)):
        print(mat[i])

def test_prot():  
    print("test_prot()")
    s1 = MySeq("PHWAS","protein")
    s2 = MySeq("HWASW","protein")
    s3 = MySeq("HPHWA","protein")
    sm = SubstMatrix()
    sm.read_submat_file("blosum62.mat", "\t")
    aseq = PairwiseAlignment(sm, -8)
    ma = MultipleAlignment([s1,s2,s3], aseq)
    alinm = ma.align_consensus()
    print(alinm)
    

def test():
    print("test")
    s1 = MySeq("ATAGC")
    s2 = MySeq("AACC")
    s3 = MySeq("ATGAC")
    
    sm = SubstMatrix()
    sm.create_submat(1,-1,"ACGT")
    aseq = PairwiseAlignment(sm,-1)
    ma = MultipleAlignment([s1,s2,s3], aseq)
    al = ma.align_consensus()
    print(al)
    
def exercise1():
    print("exercise1")
    s1 = MySeq("ACATATCAT")
    s2 = MySeq("AACAGATCT")
    s3 = MySeq("AGATATTAG")
    s4 = MySeq("GCATCGATT")
    
    sm = SubstMatrix()
    sm.create_submat(1,-1,"ACGT")
    aseq = PairwiseAlignment(sm,-1)
    ma = MultipleAlignment([s1,s2,s3,s4], aseq)
    al = ma.align_consensus()
    print(al)
  

if __name__ == "__main__": 
    
    test_prot()
    print()
    test()
    print()
    exercise1()
    

'''
RESULTS:

test_prot()

-PHWAS-
--HWASW
HPHWA--

test

ATAG-C
A-AC-C
AT-GAC

exercise1

A-CATATC-AT-
AACAGATC--T-
AG-ATATT-AG-
G-CAT--CGATT
'''