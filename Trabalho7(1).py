#Marina Gonçalves up201305591

#Task 1: 3)
        #considerei que era para apresentar os valores na matriz completa e não apenas a metade inferior da matriz
def distance_matrix():     
    seq = ["A-CATATC-AT-", "A-GATATT-AG-", "AACAGATC-T--","G-CAT--CGATT"] 
    up = NumMatrix(len(seq),len(seq)) 
    for i in range(up.num_rows()):
        for j in range(up.num_cols()):
            seq1 = seq[i]
            seq2 = seq[j]
            differences = 0
            for k in range(len(seq1)):
                    if(seq1[k]!= seq2[k]):
                        differences = differences +1
            up.set_value(i,j,differences)
            up.mat[j][i] = differences
    up.print_mat()
if __name__ == '__main__': 
    distance_matrix()
    
    #RESULTADO:
''' [0, 3, 4, 5]
    [3, 0, 6, 8]
    [4, 6, 0, 9]
    [5, 8, 9, 0] '''
    
#Task 2: 1)
def get_cluster(self):
    list = []
      
    if self.value >= 0:
        list.append(self.value)
    if(self.left != None):
        list.extend(self.left.get_cluster())
    if(self.right != None):
        list.extend(self.right.get_cluster())   
    return list
    #RESULTADO:
    '''[2, 3, 4, 1] '''
 
#Task 2: 2)
 def exists_leaf(self, leafnum):
        '''
        returns true or false if leafnum appears in the leaves of the tree
        '''
        # ...
        pos = 0
        list = self.get_cluster()
        #print(list)
        if(leafnum in list):
            pos = list.index(leafnum)
       
        if(self.right ==None and self.left == None):
            if(self.value == leafnum):
                return True
        if(pos >= (len(list))/2):
            if(self.right != None):
                return self.right.exists_leaf(leafnum)
        if(pos < (len(list))/2):
            if(self.left != None):
                return self.left.exists_leaf(leafnum)
        return False
    #RESULTADO:
    '''True
        False'''
#Task 2: 3)
def distance_leaves(self, leafnum1, leafnum2):
       ''' distance between leafnum1 and leafnum2 using the common ancestor function.
       '''
       # ...
       st = self.common_ancestor(leafnum1,leafnum2)
       dist = st.distance  
       return  dist*2
    #RESULTADO:
    '''3.0
        9.0'''

#Task 3: 1)
def execute_clustering(self):
        # initialize the trees
        trees = []
        for i in range(self.matdists.num_rows()):
            # create a tree for each leaf
            # add to list of trees
            # ... 
            bTree = BinaryTree(i)
            trees.append(bTree)
            
        # make a copy of the distance matrix to change it
        tableDist = self.matdists.copy()
        # iterations
        for k in range(self.matdists.num_rows(), 1, -1):
            # indices in the matrix for the minimum distance
            mins = tableDist.min_dist_indexes()
            i,j = mins[0], mins[1]
            # create a new tree joining the clusters
            # this will be internal node; height will half of distance in the distance matrix
            # set left tree; set right tree
            n = BinaryTree(-1,tableDist.get_value(i,j)/2,trees[i],trees[j])
            if k>2:
                # remove trees being joined from the list 
                ti = trees.pop(i)
                tj = trees.pop(j)
                dists = []
                # calculate the distance for the new cluster
                for x in range(tableDist.num_rows()):          
                    if x != i and x != j:
                        si = len(ti.get_cluster())
                        sj = len(tj.get_cluster())
                        # use the weighted average to calculate the distances between the clusters
                        d = (si*tableDist.get_value(i,x)+sj*tableDist.get_value(j,x))/(si+sj)
                        dists.append(d)
                # update the matrix:
                # remove col corresponding to i and j
                # remove row corresponding to i and j
                # add row with new distances
                # add col with zero distances
                # ...
                tableDist.remove_row(i)
                tableDist.remove_row(j)
                tableDist.remove_col(i)
                tableDist.remove_col(j)
                tableDist.add_row(dists)
                tableDist.add_col([0]*(len(dists)+1))
                trees.append(n)
            else: return n
            
    #RESULTADO:
    ''' Root - Dist.:  3.25
         Left - Dist.:  2.25
                 Left - Dist.:  1.0
                         Left  - value: 1
                         Right  - value: 0
                 Right  - value: 2
         Right - Dist.:  1.5
                 Left  - value: 4
                 Right  - value: 3  '''

#Task 3: 2)

    
    def create_mat_dist(self):
        # create distance matrix with dim N x N sequences
        self.matdist = NumMatrix(len(self.seqs),len(self.seqs))
        for i in range(len(self.seqs)):
            for j in range(i, len(self.seqs)):
                # retrieve the two sequences to align
                s1 = self.seqs[i]
                s2 = self.seqs[j]
                # align the sequences
                self.alseq.needleman_Wunsch(s1, s2)
                # recover the alignment
                alin = self.alseq.recover_align()
                ncd = 0
                # fill the matrix
                # count the number of different symbols in the alignment as the distance
                for k in range(len(alin)):
                    col = alin.column(k)
                    if (col[0] != col[1]): ncd += 1
                # set distance value in the matrix
                self.matdist.set_value(i,j,ncd) #set for cell i,j the value of ncd
                    
    def run(self):
        # create an object of the class HierarchicalClustering
       
        ch = HierarchicalClustering(self.matdist)
        # execute the clustering algorithm
        t = ch.execute_clustering()
        return t
    
    #RESULTADO: (com: seq1 = MySeq("ACATATCAT")seq2 = MySeq("AACAGATCT")seq3 = MySeq("AGATATTAG")seq4 = MySeq("GCATCGATT"))
    '''Root - Dist.:  2.0
         Left - Dist.:  0.75
                 Left - Dist.:  0.5
                         Left  - value: 3
                         Right  - value: 1
                 Right  - value: 2
         Right  - value: 0 '''

#Task 4: 1)
        