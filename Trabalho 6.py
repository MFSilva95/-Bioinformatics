#1
def test_diagonal_length(mat, istart, jstart):
    # given the starting indices on the row and column
    # check along the diagonal that starts in istart and jstart
    # the longest sub-sequences of matches; return this value
    # ....
    
    lsub = 0
    actsub = 0
    start = max(istart,jstart)
    for i in range(len(mat)-start-1):
        if(mat[istart][jstart]==1):
            actsub+=1
            istart+=1
            jstart+=1
        elif(mat[istart][jstart]!=1):
            istart+=1
            jstart+=1
            if(lsub<actsub):
                lsub=actsub
            actsub=0            
    if(actsub>lsub): lsub = actsub
    return lsub 



#5
def test_DNA_GlobalAlign():
    # test function
    # Test sequences seq1 and seq2
    # create a substitution matrix with the match and mismatch values
    # solve the NW algorithm with gap p
    # obtain the score of the alignment: using matrix cells and score alignment function
    # recover the alignment and print the aligned sequences 1 and 2
    
    # complete here ...
    seq1 = "TACT"
    seq2 = "ACTA"
    g = -3
    match = 3
    mismatch = -1
    sm = create_submat(match,mismatch,"ACTA")  
    print("SM:",sm)  
    NW = needleman_Wunsch(seq1, seq2, sm, g)
    S = NW[0]
    T = NW[1]
    print("NW:",NW)
    i, j = max_mat(S)
    best_score = S[i][j]
    print("bestScore:",best_score)
    aux1 = recover_align_local(S,T,seq1,seq2)
    print(aux1[0]) #sequence 1
    print(aux1[1]) #sequence 2
    scorealig = score_align(aux1[0],aux1[1],sm,g) 
    print("scorealigment global:", scorealig)
  
#2    
def score_align (seq1, seq2, sm, g):
    """ score of the whole alignment; iterate through the two sequences
    sum the score of each position and return its sum; assume sequences are of equal length
    
    """
    res = 0;
    for i in range(len(seq1)):
        res = res + score_pos(seq1[i],seq2[i],sm,g)
  
    return res    
#3
def test_prot():
    # test the alignment of the two sequence
    # plot the score of alignment using the subtitution matrix blosum62.mat
    # plot the score of alignment using affine gap score with gap value.
    # complete here ...
    seq1 = "LGPSSGCASRIWTKSA"
    seq2 = "TGPS-G--S-IWSKSG"
    sm = read_submat_file("blosum62.mat")
    g = -8
    print("score alignment:",score_align(seq1,seq2,sm,g))
    print("score alignment using affine gap:",score_affinegap(seq1,seq2,sm,g,-9))
    
#6
def max_mat(mat):
    """finds the max cell in the matrix"""
    maxval = mat[0][0]
    maxrow = 0
    maxcol = 0
    actmax = 0
    # returns the cell with maximum value
    # complete here... #DONE
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(actmax<mat[i][j]):
                actmax = mat[i][j]
                maxrow = i
                maxcol = j
    return (maxrow,maxcol)

#8
def test_Prot_LocalAlign():
    # Test local alignment SW to sequences seq1 and seq2
    seq1 ="ANDDR"
    seq2 = "AARRD"
    g = -8
    match = 3
    mismatch = -1
    sm = create_submat(match,mismatch,"ANDR")
    SW = smith_Waterman(seq1,seq2,sm,g)
    S = SW[0]
    T = SW[1]
    print("S:",S)
    print("T:",T)
    maxscore = SW[2]
    print("local max score:",maxscore)
    alinL= recover_align_local(S, T, seq1, seq2)
    print(alinL[0]) #sequence 1
    print(alinL[1]) #sequence 2
    scorealig = score_align(alinL[0],alinL[1],sm,g) 
    print("score aligment local:", scorealig)
    
#9
def identity(seq1, seq2, alphabet = "ACGT"):
    '''calculate the identity score between seq1 and seq2 '''
    # complete here ...
    g = 0
    match = 1
    mismatch = 0
    sm = create_submat(match,mismatch,alphabet)
    NW,_ = needleman_Wunsch(seq1,seq2,sm,g)
    eq = NW[len(seq1)][len(seq2)]
    #print(eq)
    res = eq/max(len(seq1),len(seq2))
    return res
    