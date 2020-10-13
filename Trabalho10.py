 ####Marina Filipa da Silva GOnçalves up201305591
###TASK1:
        Mudanças  a nível do DNA estão na base de multiplas doenças. Ao entender as redes genéticas que sofrem estas mudanças
    ou são influenciadas pelas mesmas ajuda no estudo do desenvolvimento destas doenças.
        A "Gene Expression Correlation Network Analisys" tem como objectivo a correlação entre expressões genéticas 
    e marcadores de DNA revelando conjuntos de genes e os marcadores associados a determinadas doenças. 
        As redes são constituidas por genes que são representados por nós com ligações entres eles que representam as suas associações, isto 
    é que contribuem para uma função e não que estão fisicamente conectados.
        Existem metodos como microarray e sequenciamento que permite interrogar o estado de uma celula em um dado momento. Também existem 
    metodos como Y2Y ou chips de proteína que ajuda a determinar como determinadas moléculas interagem e como. Y2Y ajuda é uma 
    abordagem genética para a identificação de potenciais interações entre proteínas. Os Chips de proteína ajuda a detectar a ligação de
    actividade das proteínas.
        Existem vários factores que influenciam este tipo de análise como a medida de centralidade que fornece critérios para avaliar 
    a importancia do nó, visto que nem todos os nós são igualmente significantes.   
        A Correlação de Pearson mede o grau de correlação entre duas variáveis entre [-1,1] em que valores aproximados de 1 indicam
    que há correlação, valores aproximados de 0 que não há correlação e valores aproximados de -1 indica que são anti-correlacionados.
    
###TASK2:


    def create_network_from_file(self, file,min_correlation):
        f = open(file,'r')
        lines = f.read().split("\n")
        f.close()
        for l in range(1,len(lines)):
            values = lines[l].split('\t')
            if(float(values[2]) > min_correlation):
                self.add_edge(values[0],values[1])
                self.add_edge(values[1],values[0])
        return None
        
###TASK3:

    ## get basic info
    def get_nodes(self):
        ''' Returns list of nodes in the graph '''
        # ....
        return list(self.graph.keys())
        
    def get_edges(self): 
        ''' Returns edges in the graph as a list of tuples (origin, destination) '''
        # ...
        edges = []
        for v in self.graph.keys():
            for d in self.graph[v]:
                edges.append((v,d))
        return edges
      
    def size(self):
        ''' Returns size of the graph : number of nodes, number of edges '''
        # ...
        return len(self.get_nodes()),len(self.get_edges())
        
    ## add nodes and edges    
    def add_vertex(self, v):
        ''' Add a vertex to the graph; tests if vertex exists not adding if it does '''
        # ...
        if v not in self.graph.keys():
            self.graph[v]= []
        
    def add_edge(self, o, d):
        ''' Add edge to the graph; if vertices do not exist, they are added to the graph ''' 
        # ...
        if o not in self.graph.keys():
            self.add_vertex(o)
        if d not in self.graph.keys():
            self.add_vertex(d)
        if (o,d) not in self.get_edges():
            self.graph[o].append(d)
        
    ## degrees    
    
    def out_degree(self, v):
        # ...
        return len(self.graph[v])
    def in_degree(self, v):
        # ...
        return len(self.get_predecessors(v))
        
    def degree(self, v):
        # ...
        return len(self.get_adjacents(v))
    
    ## topological metrics over degrees

    def mean_degree(self, deg_type = "inout"):
        ''' average degree of all nodes: sum of all degrees divided by number of nodes'''
        #....
        degs = self.all_degrees(deg_type)
        return sum(degs.values())/float(len(degs))        
    def prob_degree(self, deg_type = "inout"):
        # count the number of occurrences of each degree in the network and derive its frequencies
        # ...
        degs = self.all_degrees(deg_type)
        res = {}
        for k in degs.keys():
            if degs[k] in res.keys():
                res[degs[k]] += 1
            else:
                res[degs[k]] = 1
        for k in res.keys():
            res[k] /= float(len(degs))
        return res
                
    ## clustering
        
    def clustering_coef(self, v):
        adjs = self.get_adjacents(v) # ... get the list of adjancent nodes
        if len(adjs) <=1: return 0.0
        # calculate the number of links of the adjacent nodes 
        ligs = 0
        # compare pairwisely if nodes in this list are connected between them
        for i in adjs:
            for j in adjs:
                if i != j:
                    if i in self.graph[j] or j in self.graph[i]:
                        ligs +=1
                    # check if i and j are connected to each other; if yes increment counter of links                    
        return float(ligs)/(len(adjs)*(len(adjs)-1))
        
    def all_clustering_coefs(self):
        # go through all the nodes and calculate its cc
        # put those in a dictionary and return
        dic = {}
        for n in self.get_nodes():
            dic[n]= self.clustering_coef(n)
            
        return dic
            
        
    def mean_clustering_coef(self):
        # get all the clustering coefficients
        # and return the mean of all ccs
        acc = self.all_clustering_coefs()
        return sum(acc.values())/float(len(acc))

    ''' RESULT: 
    1  ->  [2]
    2  ->  [3]
    3  ->  [2, 4]
    4  ->  [2]
    size: (4, 5)
    sucessors(2): [3]
    precessores(2): [1, 3, 4]
    adj(2): [1, 3, 4]
    in_degree(2): 3
    out_degree(2): 1
    degree(2): 3
    all_degrees inout: {1: 1, 2: 3, 3: 2, 4: 2}
    all_degrees in:  {1: 0, 2: 3, 3: 1, 4: 1}
    all_degrees out {1: 1, 2: 1, 3: 2, 4: 1}
    [2, 3, 4, 5, 6, 8, 7]
    [2, 5, 7, 6, 3, 8, 4]
    distance(1,7): 3
    shortest_path(1,7): [1, 2, 5, 7]
    2
    [1, 3, 8]
    None
    None
    mean_degree(): 2.0
    prob_degree(): {1: 0.25, 3: 0.25, 2: 0.5}
    clustering_coef(1): 0.0
    clustering_coef(2): 0.3333333333333333
    all_clustering_coefs: {1: 0.0, 2: 0.3333333333333333, 3: 1.0, 4: 1.0}
    mean_clustering_coef: 0.5833333333333333 '''
###TASK4: