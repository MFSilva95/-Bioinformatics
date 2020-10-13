####################################################################################################################
###                                    Algorithms for Bioinformatics
###                                 *** Sequence functions              ***    
###
### Test number: 3      Class Number: 3         Date:   17 to 21 February 2020
###
### Group
### Student: Lucas Carvalho de Paula               Number: 201608440
### Student: Marina Filipa da Silva Gonçalves      Number: 201305591
###
####################################################################################################################
### Add below all the functions from sequence_function.py to be completed and submit in Test 3
def write_seq_to_file(seq, filename):
    """ Writes a sequence to file. """
    # complete 
    # DONE
    f = open(filename, 'w')
    f.write(seq)
    f.close()
def read_genetic_code_from_file(filename):
    """ Reads the genetic code to a dictionary from a multi-line text file. """
    dic = {}
    #DONE
    # complete
    with open(filename, 'r') as file:
        for line in file:
            k, v = line.split(' ')
            dic[k.replace('\"', '')] = v.replace('\n', '').replace('\"', '')
            
    return dic
def gc_content_subseq(dna_seq, k=100): #testar
    """ Returns GC content of non-overlapping sub-sequences of size k. """
    # complete
    #DONE
    list=[]  
    for s in range(0,len(dna_seq)-(k-1),k):
        list.append(gc_content(dna_seq[s:s+k]))        
    return list    

def reverse_complement (dna_seq):
    """ Computes the reverse complement of the inputted DNA sequence. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    comp = ""
    # complete
    #DONE
    aux = {
        'A':'T', 'T':'A', 'C':'G', 'G':'C'
    }
    for i in dna_seq:
        comp = comp+aux[i]
    return comp[::-1]

def translate_seq(dna_seq, ini_pos = 0):
    """ Translates a DNA sequence into an aminoacid sequence. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    seqm = dna_seq.upper()
    seq_aa = ""
    # complete
    #DONE
    for s in range(ini_pos, len(seqm),3):
        if(s+3<=len(seqm)):
            seq_aa=seq_aa + translate_codon(seqm[s:s+3])
    return seq_aa

def all_orfs (dna_seq):
    """Computes all possible proteins for all open reading frames."""
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    res = []
    # complete
    # DONE
    rfs = reading_frames(dna_seq)
    for aa_seq in rfs:
        proteins = []
        aa_seq = aa_seq.upper()
        proteins = all_proteins_rf(aa_seq) 
        for p in proteins:
            res.append(p)
    return res

def all_orfs_ord (dna_seq, minsize = 0):
    """Computes all possible proteins for all open reading frames. Returns ordered list of proteins with minimum size."""
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    rfs = reading_frames (dna_seq)
    res = []
    # complete
    # DONE  
    for aa_seq in rfs:
        aa_seq = aa_seq.upper()
        current_prot =[]
        proteins = []
        for aa in aa_seq:
            if aa == "_":
                if current_prot:
                    for p in current_prot:
                        if len(p)>minsize:
                            proteins.append(p)
            else:
                if aa == "M":
                    current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i]= current_prot[i]+aa                    
        for p in proteins:
            insert_prot_ord(p, res)
    return res