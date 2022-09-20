#!/usr/bin/env python
# coding: utf-8

# In[337]:


#TEST ADEQUATION pour distribution d'une loi de probabilité pi.
#Je fais un tirage et applique ce test sur mes résultats. Je regarde ma distribution et j'observe comment cette v.a
#converge vers une distribution donnée (ici Chi-deux).

import pylab
import random
import math
import numpy as np
import scipy.stats


#Definition des variables:
X = [1, 2, 3, 4] #X une variable aléatoire appartenant à un ensemble fini de [1;4] 
n = 1000
wX1 = 60 #wX1 le poids (weight) associé au tirage pour X = 1 tq wX1 = probabilité(X = 1) * 100
wX2 = 10
wX3 = 25
wX4 = 5

#Definition de Pi vecteur de probabilités associés aux Xi: 
Pi = [wX1, wX2, wX3, wX4] 
for i in range(len(Pi)):
    Pi[i] = Pi[i]/100
Pi = np.array(Pi)             
print("Pi = ",Pi, type(Pi))


def VariablesAleatoires(n):
    global X
    string = ""
    observation = []
    observationdict = {}
    observation = random.choices(X, weights=(wX1, wX2, wX3, wX4), k=n)
    string += '{}'.format(observation)
    observation.sort() #la fonction sort() permet de trier en ordre croissant (utiliser print(observation) pour voir l'effet)
    #print(observation)
    dict_obs = {x:observation.count(x) for x in observation}
    X, observationfreq = list(dict_obs.keys()), dict_obs.values() #dict_values correspond aux fréquences des valeurs tirées.
    Ni = np.array(list(observationfreq)) #dict_values étant une valeur de dictionnaire, on la transforme une première fois en liste, puis en vecteur pour pouvoir faire des opérations dessus.
    string+="X = {} {} \n".format(X, type(X))
    string+="Ni = {} \n".format(Ni, type(Ni))
    return string, Ni #Ni correspond bien aux fréquences des valeurs tirées sous forme de vecteur.
    
string1, Ni = VariablesAleatoires(n)


def TestAdequation(n, Ni, Pi):
    #Ni our observed frequency
    string = ""
    string += "__ TEST ADEQUATION FUNCTION FOR 1 TEST : __ \n"
    string +="\t Ni in function TestAdequation is {} \n".format(Ni)
    X_critic_5percent = scipy.stats.chi2.ppf(1-.05, df=len(X)-1) #On définit notre Xcritique pour un seuil de 5%
    string +='\t X_critic_5percent is {} \n'.format(X_critic_5percent)
    theo_quantity = Pi*n
    string +='\t theo_quantity = {} {} \n'.format(theo_quantity, type(theo_quantity))
    Z = np.subtract(Ni, theo_quantity)
    string += "\t Z is {} \n".format(Z)
    Z_2 = np.square(Z)
    string +="\t Z2 is {} \n".format(Z_2)
    D = np.divide(Z_2, theo_quantity)
    string +="\t D is {} \n".format(D)
    Dn = sum(D)
    string +='\t Dn is {} \n'.format(Dn)
    if Dn<X_critic_5percent:
        string +="\t H0 is valid"
        return string, 1
    else:
        string +="\t H0 is not valid"
        return string, 0
    
string, Test = TestAdequation(n, Ni, Pi)
print(string )

m = 100

#faire une boucle qui recommence et qui evalue la proportion de H0 valide et non valide. A quelle fréquence H0 est rejeté par le test.

def Proportion_H0_H1(m):
    print()
    print("__ PROPORTION H0/H1 FOR m TRIALS : __")
    ListTest = [0, 0]
    for i in range(m) :
        string1, Ni = VariablesAleatoires(n)
        string, Test = TestAdequation(n, Ni, Pi)
        if Test == 1:
            ListTest[0] += 1
        else :
            ListTest[1] += 1
    print('\t', ListTest)
    print('Ho has a porportion of',ListTest[0], '% and H1 has a proportion of', ListTest[1],'%')

a = Proportion_H0_H1(m)


# In[338]:


#TEST ADEQUATION PIECE PILE OU FACE

import pylab
import random
import math
import numpy as np
import scipy.stats
#Definition des variables:
p = 0.5
n = 1000
X = [0, 1] #X une variable aléatoire appartenant à un ensemble fini de [0,1] (une pièce pile ou face)

def VariablesAleatoires(n):
    global X
    string = ''
    N_pile = np.random.binomial(n,p) #Ni une v.a représentant la fréquence observée de la somme des Xi, pour X suivant une loi de bernouilli.
    N_face = n - N_pile
    Ni = np.array([N_pile, N_face])
    string+="X = {} {} \n".format(X, type(X))
    string+="Ni = {} {} \n".format(Ni, type(Ni))
    return string, Ni #Ni correspond bien aux fréquences des valeurs tirées sous forme de vecteur.

string, Ni = VariablesAleatoires(n)
print(string)

def TestAdequation(n, Ni):
    #Ni our observed frequency
    string = ''
    string+="__ TEST ADEQUATION FUNCTION FOR 1 TEST : __ \n"
    string+="\t Ni in function TestAdequation is {} \n".format(Ni)
    X_critic_5percent = scipy.stats.chi2.ppf(1-.05, df=len(X)-1) #On définit notre Xcritique pour un seuil de 5%
    string+='\t X_critic_5percent is {} \n'.format(X_critic_5percent)
    theo_quantity = p*n
    string+='\t theo_quantity = {} {} \n'.format(theo_quantity, type(theo_quantity))
    Z = np.subtract(Ni, theo_quantity)
    string+="\t Z is {} \n".format(Z)
    Z_2 = np.square(Z)
    string+="\t Z2 is {} \n".format(Z_2)
    D = np.divide(Z_2, theo_quantity)
    string+="\t D is {} \n".format(D)
    Dn = sum(D)
    string+='\t Dn is {} \n'.format(Dn)
    if Dn<X_critic_5percent:
        string+="\t H0 is valid"
        return string,1 
    else:
        string+="\t H0 is not valid"
        return string, 0
        
        
string1, Test  = TestAdequation(1000, Ni)
print(string1)

m = 100
def ProportionH0_H1(m):
    print()
    print("__ PROPORTION H0/H1 FOR m TRIALS : __")
    proportion = [0, 0]
    for i in range(m):
        string, Ni = VariablesAleatoires(n)
        string1, Test = TestAdequation(1000,Ni)
        if Test == 1:
            proportion[0] +=1
        else:
            proportion[1] +=1
    print('\t',proportion)
    print('Ho has a porportion of',proportion[0], '% and H1 has a proportion of', proportion[1],'%')

a = ProportionH0_H1(m)


# In[331]:


#TEST D'INDEPENDANCE
import pylab
import random
import math
import numpy as np
import scipy.stats
#Soit un couple (X1, Z1), ..., (Xn, Zn) de loi de proba Pij = P(X1 = i, Z1 = j)
#Definition des variables:
X = [1, 2, 3, 4, 5, 6]#X une variable aléatoire appartenant à un ensemble fini de [1;4] 
Z = [1, 2, 3, 4, 5, 6]
n = 1000

#Q = np.random.choice(X, size = (n,2) #Nous donne la combinaison de (X,Z) en colonne.
#ce Q = np.random.choice(X, size = (1,2)
#est similaire à Q = np.random.choice(X, size = 2)

#Tableau[i][j] : renvoie le jème élément de la ième ligne du tableau
#Ici, Lorsque l'on fait Ni[Q], comme Q est déjà composé de deux valeurs [i, j], c'est compris comme [i][j] automatiquement

def ObservedFrequency(n):
    global X, Z
    string = ''
    Nij = np.zeros((len(X),len(Z)))
    for k in range(n) :
        Q = np.random.choice(X, size = 2)
        #print(Q)
        Nij[Q[0]-1,Q[1]-1] += 1 #implicitement, la probabilité Pij pour un couple [ij] ici est 1/36
    string+='Les fréquences observées Nij pour n lancés : \n'
    string+= '{} \n\n'.format(Nij)
    return string, Nij #il faut penser à utiliser RETURN sinon la fonction TestIndependance ne pourra pas utiliser ses valeurs

string, Nij = ObservedFrequency(n) 
print(string)

def TestIndependance(Nij):
    string = ''
    string +='__ TEST INDEPENDANCE __ : \n'
    X_critic_5percent = scipy.stats.chi2.ppf(1-.05, df=(len(X)-1)*(len(Z)-1)) #On définit notre Xcritique pour un seuil de 5%
    string +='\t Xcritic 5% = {} \n'.format(X_critic_5percent)
    Ni = np.sum(Nij, axis=0) # Ici Ni représente les colonnes !
    string+='\t fréquences observées Ni. pour 1<i<r {} \n'.format(Ni) 
    Nj = np.sum(Nij, axis=1) # Ici Nj représente les lignes !
    string+='\t fréquences observées N.j pour 1<j<s {} \n'.format(Nj) 
    string+='\n'
    string+='Les v.a. X1 et Z1 sont indépendantes si et seulement si, pour tous i et j, Pij = Pi· x P·j \n'
    produit_freqobsi_j = np.tensordot(Nj, Ni, axes=0)/n #np.tensordot(vecteur1, vecteur2, axes=0) permet de créer une matrice par le multiple de deux vecteurs, case par case
    string+='frequence theorique (Ni x Nj)/n : \n' #ATTENTION, j'avais interverti les lignes et les colonnes en faisant np.tensordot(Ni,Nj, axes=0)
    string+='{} \n'.format(produit_freqobsi_j)                        # np.tensordot(vecteur_LIGNE, vecteur_COLONNE, axes = (0, 1 ou 2 selon le type de calcul))
    diff = Nij - produit_freqobsi_j
    squarediff = np.square(diff)
    D = squarediff / produit_freqobsi_j
    string+='\n'
    string+='{}'.format(D)
    D_n = sum(D)
    string+='\n'
    string+='{} \n'.format(D_n)
    string+='\n'
    Dn = sum(D_n)
    string+='Dn = {} \n'.format(Dn)
    string+='Xcritic 5% = {} \n'.format(X_critic_5percent)
    if Dn<X_critic_5percent:
        string+="\t H0 is valid"
        return string, 1
    else:
        string+="\t H0 is not valid"
        return string, 0
    
string1, TI = TestIndependance(Nij)
print(string1)

m = 100
def ProportionH0_H1(m):
    print()
    print("__ PROPORTION H0/H1 FOR m TRIALS : __")
    proportion = [0, 0]
    for i in range(m):
        string, Nij = ObservedFrequency(n)
        string1, TI = TestIndependance(Nij)
        if TI == 1:
            proportion[0] +=1
        else:
            proportion[1] +=1
    print('\t',proportion)
    print('Ho has a porportion of',proportion[0], '% and H1 has a proportion of', proportion[1],'%')

a = ProportionH0_H1(m)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




