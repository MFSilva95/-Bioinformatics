def repeated_subsequences_frequency(dna_seq, k = 10):
    '''Write a function that, given a DNA sequence, allows to detect if there are repeated sequences of size k
    The result should be a dictionary with sub-sequences as keys, and their frequency as values.'''
    # complete here ...
    import re
    from re import findall
    dic = {}
   
    for p in range(0,len(dna_seq)-k-1,1):
        s = dna_seq[p:p+k]
        match = re.findall(s,dna_seq,0)
        if s in dic: 
            dic[s] += len(match)
        else:
            dic[s] = len(match)              
    return dic          
