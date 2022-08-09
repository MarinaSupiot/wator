from random import randint
from time import sleep

class Espace:
    """
    Class qui représente l'Espace (la fille avec des Requins et des Poisson)

    ..............................
    Attributes:
    nb_ligne: (srt) nombre de lignes dans la grille
    nb_colonne: (str) nombre de colonnes dans la grille
    nombre_poisson: (str) nombre de poissons dans la grille
    nombre_requin: (str) nombre de requins dans la grille
    .............................

    """

    def __init__(self,nb_ligne,nb_colonne,nombre_poisson,nombre_requin,x,y):
        self.nb_ligne = nb_ligne
        self.nb_colonne= nb_colonne
        self.grille = [[0 for i in range(nb_ligne)] for j in range(nb_colonne)]
        self.nombre_poisson = nombre_poisson
        self.nombre_requin = nombre_requin
        self.x = x
        self.y = y

    def afficher_grille(self):

        """
        La fonction qui affiche la grille du jeu
        :returne: (none)
        """
        for i in range(self.nb_colonne):
            print(self.grille[i])
        print("\n")


    def affiche_grille2(self):
        for i in self.grille :
            ligne_aff =" "
            for j in i:
                if isinstance(j,Requin):
                    ligne_aff += "2"
                elif isinstance(j,Poisson):
                    ligne_aff += "1"
                elif j == 0:
                    ligne_aff += "0"
            print(ligne_aff)
        print ("........................................................","\n")


    def peupler_grille(self):

        """
        La fonction qui place les Poisson et les Requins sur la grille à la façon aléatoire. 
        (les Requins et les Poisson appartiennent au type de données .class)
        :returne(liste):La grille avec les Poissons et les Requins placés
        """
        #le placement d'un Poisson
        i=0
        while i < self.nombre_poisson:
            pif = randint(0,self.nb_ligne-1)
            paf = randint(0,self.nb_colonne-1)
            if self.grille[pif][paf] == 0:
                self.grille[pif][paf] = Poisson(pif,paf,120)
        
                i += 1    
         #le placement d'un Requin        
        j=0
        while j < self.nombre_requin:
            pif = randint(0,self.nb_ligne-1)
            paf = randint(0,self.nb_colonne-1)
            if self.grille[pif][paf] == 0:
                self.grille[pif][paf] = Requin(pif,paf,50,60)
                j += 1
        return self.grille 

            
        
        
    def convertir_grille_peupler(self):
        """
        La fonction qui permet de reconvertir la grille avec les Poissons et les Requins 
        avec le type de données .class en '1' (pour les Poisson) et '2' (pour les Requins)
        :returne grille(liste): La liste avec des '0', '1', '2' qui represente l'Espace (0) 
        avec les Poissons(0) et les Requins(2)
        """
        for i in range(0,self.nb_ligne):
            for j in range(0,self.nb_colonne):
                if  type(self.grille[i][j]) is Poisson:
                    self.grille[i][j] = 1
                elif type(self.grille[i][j]) is Requin:
                    self.grille[i][j] = 2
                else:pass
        return self.grille


    def afficher_grille_peupler(self):
        """
        La fonction qui affiche le grille du jeu avec '0', '1'
        :returne: (none)
        """
        for i in range(self.nb_colonne):
            print(self.grille[i])

        
    def depla_possible(self, monde):
        """
        La fonction qui vérifie les deplassements possibles pour un Animal
        :param monde (liste) : Une liste avec les Animaux placés
        :param returne(liste) : Une liste avec les deplassement possibles avec 
        de chaine de caractères : 'bas', 'haut', 'gauche', 'droite'
        """
        t = []
        if monde.grille[(self.x+1)%monde.nb_ligne][self.y] == 0:
            t.append('bas')
        if monde.grille[(self.x-1)%monde.nb_ligne][self.y] == 0:
            t.append('haut')
        if monde.grille[self.x][(self.y-1)%monde.nb_colonne] == 0:
            t.append('gauche')
        if monde.grille[self.x][(self.y+1)%monde.nb_colonne] == 0:
            t.append('droite')
        return t 
        
    def tour_du_monde(self):
        for ligne in self.grille:
            for case in ligne:
                if case != 0:
                    
                    case.jouer_un_tour(monde)
        return monde
                  


class Animaux:
    """
    Class 'Animaux'  

    ..............................
    Attributes:
    x: (srt) position X dans la grille
    y: (str) position Y dans la grille
    energie_reproduction: (str) niveau d'énerdie de reproduction
    .............................  
    """

    def __init__(self,x,y,energie_reproduction):
        self.x = x
        self.y = y
        self.energie_reproduction = energie_reproduction
    


    def depla_possible(self,monde):
        """
        La fonction qui vérifie les deplassements possibles pour un Animal
        :param monde (liste) : Une liste avec les Animaux placés
        :param returne(liste) : Une liste avec les deplassement possibles avec 
        de chaine de caractères : 'bas', 'haut', 'gauche', 'droite'
        """
        t = []
        if monde.grille[(self.x+1)%monde.nb_ligne][(self.y)%monde.nb_colonne] == 0:
            t.append('bas')
        if monde.grille[(self.x-1)%monde.nb_ligne][(self.y)%monde.nb_colonne] == 0:
            t.append('haut')
        if monde.grille[(self.x)%monde.nb_ligne][(self.y-1)%monde.nb_colonne] == 0:
            t.append('gauche')

        if monde.grille[self.x][(self.y+1)%monde.nb_colonne] == 0:
            t.append('droite')
        return t 

    def deplacement_animaux(self,monde):
        """
        La fonction qui deplasse un Animal
        :param monde (liste) : Une liste avec les Animaux placés
        :param returne(bolean, liste) : True(si le deplassement possible) La grille avec les Animaux deplassées
        """

        
        a = self.depla_possible(monde)
        l = monde.grille
       
       
        if len(self.depla_possible(monde)) == 0:
            pass
        else : 
            b = randint(0,len(a)-1) 
            c = a[b]
            
            if c  == 'haut':
                l[(self.x-1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.x = (self.x-1)%monde.nb_ligne
                self.energie_reproduction += 1  
              
            if c  == 'bas':
                l[(self.x+1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.x = (self.x+1)%monde.nb_ligne
                self.energie_reproduction += 1  
      
            if c == 'droite':
                l[self.x][(self.y+1)%monde.nb_colonne] = l[self.x][self.y]
                l[self.x][self.y] = 0
                self.y = (self.y+1)%monde.nb_colonne
                self.energie_reproduction += 1  
                
            if c == 'gauche':
                l[self.x][(self.y-1)%monde.nb_colonne] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.y = (self.y-1)%monde.nb_colonne
                self.energie_reproduction += 1  
               
            return True , l

    
    def se_reproduire(self,monde):
        """
        La fonction qui laisse un Animal à sa place s'il y a la possibilité de se déplacer
        :param grille: (liste) Une liste avec des '0', '1', '2'
        :param return (bolean, liste) : True(si la repoduction possible) La grille avec les Animaux
        """
        a = self.depla_possible(monde)

        l = monde.grille
        
       
        if len(self.depla_possible(monde)) == 0:
            pass
        
        else:
            b = randint(0,len(a)-1) # len(a)-1? 
            c = a[b]
            if c  == 'haut':
                l[(self.x-1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = Poisson(self.x,self.y,0)
                self.x = (self.x-1)%monde.nb_ligne
                 
              
            if c  == 'bas':
                l[(self.x+1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = Poisson(self.x,self.y,0)
                self.x = (self.x+1)%monde.nb_ligne
                
      
            if c == 'droite':
                l[self.x][(self.y+1)%monde.nb_colonne] = l[self.x][self.y]
                l[self.x][self.y] = Poisson(self.x,self.y,0)
                self.y = (self.y+1)%monde.nb_colonne
                 
                
            if c == 'gauche':
                l[self.x][(self.y-1)%monde.nb_colonne] = l[self.x][self.y] 
                l[self.x][self.y] = Poisson(self.x,self.y,0)
                self.y = (self.y-1)%monde.nb_colonne
                
            self.energie_reproduction = 0   
            monde.nombre_poisson += 1 
             
            return True , l


    def jouer_un_tour(self,monde):
        """
        La fonction qui permet de jouer un tour
        :param returne: (none)
        """
        if len(self.depla_possible(monde)) != 0 :
            pass
        if self.energie_reproduction >=  20:
            self.se_reproduire(monde)
            self.energie_reproduction =0
        else:
            self.deplacement_animaux(monde)
        return monde

class Poisson(Animaux):
    pass


class Requin(Animaux):
    """
    Class 'Requin'  
    ..............................
    Attributes:
    x: (srt) position X dans la grille
    y: (str) position Y dans la grille
    energie_reproduction: (str) niveau d'énerdie de reproduction
    energie: (str) niveau d'énerdie par défaut
    .............................  
    """

    def __init__(self, x, y, energie_reproduction,energie):
        super().__init__(x, y, energie_reproduction)
        self.energie = energie 


    def deplacement_possible_requin(self,monde):
        """
        La fonction qui vérifie les deplassements possibles pour un Animal
        :param monde (liste) : Une liste avec les Animaux placés
        :param returne(liste) : Une liste avec les deplassement possibles avec 
        de chaine de caractères : 'bas', 'haut', 'gauche', 'droite'
        """
        t=[]
        l= monde.grille
        if l[(self.x+1)% monde.nb_ligne][self.y] == 0 :
            t.append('bas')
        if l[(self.x-1)%monde.nb_ligne][self.y] == 0 :
            t.append('haut')
        if l[self.x][(self.y-1)%monde.nb_colonne] == 0 :
            t.append('gauche')

        if l[self.x][(self.y+1)%monde.nb_colonne] == 0 :
            t.append('droite')
        return t


    def manger_possible(self,monde):
        """
        La fonction qui vérifie s'il y a un Poisson dans les cases voisines
        :param grille: (liste) Une liste avec des Animaux placés
        :param return: (liste) Une liste de chaine de caractères avec les noms de directions possibles

        """
        t = []
        if type(monde.grille[(self.x+1)%monde.nb_ligne][self.y]) is Poisson:
            t.append('bas')
        if type (monde.grille[(self.x-1)%monde.nb_ligne][self.y]) is Poisson:
            t.append('haut')
        if type(monde.grille[self.x][(self.y-1)%monde.nb_colonne]) is Poisson:
            t.append('gauche')
        if type (monde.grille[self.x][(self.y+1)%monde.nb_colonne]) is Poisson:
            t.append('droite')
        return t 

    def manger(self,monde):
        """
        Fonction qui permet de deplacer un Requin vers un Poisson si la case voisine le contient
        :param grille: (liste) Une liste avec les Animaux placés

        :param returne: (liste) Retourne une nouvelle liste avec les Requins deplacés, 
                        False si le deplacemenr n'est pas possible
        """
        t = self.manger_possible(monde)
        l = monde.grille
        if len(Requin.manger_possible(self,monde)) == 0:
            return l
        else: 
            
            if t[randint(0,len(t)-1)]  == 'haut':
                l[(self.x-1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.x = (self.x-1)%monde.nb_ligne
                
            if t[randint(0,len(t)-1)]  == 'bas':
                l[(self.x+1)% monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                
                self.x = (self.x+1)% monde.nb_ligne
               
            if t[randint(0,len(t)-1)] == 'droite':
                l[self.x][(self.y+1)%monde.nb_colonne] = l[self.x][self.y]
                l[self.x][self.y] = 0
                self.y = (self.y+1)%monde.nb_colonne
                
            if t[randint(0,len(t)-1)]  == 'gauche':
                l[self.x][(self.y-1)%monde.nb_colonne] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.y = (self.y-1)%monde.nb_colonne
                
        self.energie += 10
        monde.nombre_poisson -= 1
        

        
        return l

    def deplacement_requin(self,monde):
        """
        Fonction qui permet de deplacer un Requin vers une case voisine si le deplessement est possible
        :param grille: (liste) Une liste avec les Animaux placés
        :param t:(liste) Une liste qui contient  les deplacement possibles d'un requin (chaine de caractères)
        :param returne: (liste) Retourne une nouvelle liste avec les Requins deplacés, 
                        False si le deplacemenr n'est pas possible 
        """
        
        t= self.deplacement_possible_requin(monde)
        l = monde.grille
       
        if len(t) != 0:
            if t[randint(0,len(t)-1)]  == 'haut':
                monde.grille[(self.x-1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.x = (self.x-1)%monde.nb_ligne
              
                
            elif t[randint(0,len(t)-1)]  == 'bas':
                l[(self.x+1)% monde.nb_ligne][self.y] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.x = (self.x+1)% monde.nb_ligne
                
                
            elif t[randint(0,len(t)-1)] == 'droite':
                l[self.x][(self.y+1)%monde.nb_colonne] = l[self.x][self.y]
                l[self.x][self.y] = 0
                self.y = (self.y+1)%monde.nb_colonne
                
                
            elif t[randint(0,len(t)-1)]  == 'gauche':
                l[self.x][(self.y-1)%monde.nb_colonne] = l[self.x][self.y] 
                l[self.x][self.y] = 0
                self.y = (self.y-1)%monde.nb_colonne
               
            self.energie -= 1
        return l     




    def bouger_requin(self):
        """
        La fonction qui permet de bouger un Requin
        :param returne: True si le deplacement possible et s'il y a un Poisson autour, False sinon
        """

        if len(self.deplacement_possible_requin(monde)) != 0:
            return True
        if len(self.manger_possible(monde)) != 0:
            return True
        else:
            return False    


    def se_reproduire(self,monde):
        """La fonction qui permet de donner la naissance à un autre Requin 
        s'il y a la possibilité de le bouger et le niveau d'énergie est suffisant
        :param returne: (boléan) True si deux conditions peuvent être remplies, False sinon
        """

        
        t= self.deplacement_possible_requin(monde)
        l = monde.grille
  
        
        if self.energie_reproduction < self.energie :
            if len(t)>0:
                if t[randint(0,len(t)-1)]  == 'haut':
                    monde.grille[(self.x-1)%monde.nb_ligne][self.y] = l[self.x][self.y] 
                    l[self.x][self.y] = Requin(self.x,self.y,30,6)
                    self.x = (self.x-1)%monde.nb_ligne
                    monde.nombre_requin += 1 
                    self.energie -= 5
                    return True
                    
                if t[randint(0,len(t)-1)]  == 'bas':
                    l[(self.x+1)% monde.nb_ligne][self.y] = l[self.x][self.y] 
                    l[self.x][self.y] = Requin(self.x,self.y,30,6)
                    self.x = (self.x+1)% monde.nb_ligne
                    self.energie -=5
                    monde.nombre_requin += 1 
                    return True
                    
                if t[randint(0,len(t)-1)] == 'droite':
                    l[self.x][(self.y+1)%monde.nb_colonne] = l[self.x][self.y]
                    l[self.x][self.y] = Requin(self.x,self.y,30,6)
                    self.y = (self.y+1)%monde.nb_colonne
                    self.energie -= 5
                    monde.nombre_requin += 1 
                    return True
                    
                if t[randint(0,len(t)-1)]  == 'gauche':
                    l[self.x][(self.y-1)%monde.nb_colonne] = l[self.x][self.y] 
                    l[self.x][self.y] = Requin(self.x,self.y,30,6)
                    self.y = (self.y-1)%monde.nb_colonne
                    self.energie -=5
                    monde.nombre_requin += 1 
                    return True
    def est_mort(self,monde):
        if self.energie <= 0:
            monde.grille[self.x][self.y] = 0 
            monde.nombre_requin -= 1 
            
    def jouer_un_tour(self,monde):
        """
        La fonction qui permet de jouer un tour
        returne(liste):la grille avec les Animaux deplasés

        """

        self.manger(monde)
        self.se_reproduire(monde)
        self.deplacement_requin(monde)
        self.est_mort(monde)

        monde.grille = self.deplacement_requin(monde)
        return monde

            
               

monde = Espace(5,5,20,1,2,10)
monde.peupler_grille()

print(type(monde.grille))
i=0
listem = [[0 for i in range(monde.nb_ligne)] for j in range(monde.nb_colonne)]
listemo = [[Poisson for i in range(monde.nb_ligne)] for j in range(monde.nb_colonne)]
print(monde.nombre_poisson)
    

        
        
while i <200:

    monde.affiche_grille2()
    monde.tour_du_monde() 
    monde.affiche_grille2()
  
    if monde.grille == listem:
        print('Le jeu est terminé ... plus de requins, plus de poissons')
        print ("........................................................","\n")
        break
    if monde.nombre_requin < 1:
        print('Le jeu est terminé...plus de requins')
        print ("........................................................","\n")
        break
    if monde.nombre_poisson <-10:
        print("Le jeu est terminé...plus de poissons")
        print ("........................................................","\n")
        break
        
    i += 1
  
    sleep(1)   


