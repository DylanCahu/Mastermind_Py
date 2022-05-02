from random import randint

#variables globale
choixPC =   [0,0,0,0]
choixJoueur=[0,0,0,0]

def choixOrdinateur():
 for i in range(4):
     choixPC[i] = randint(1, 5)
 #return (choix)

def choixOrdinateur2():
 choix= [randint(1, 5)for i in range(4)]
 return (choix)

def ChoixJoueur():
#variables locale
  n=int(input("nb composé de 4 chiffres entre 1 et 5 :"))
  choixvalide=0

  for i in range(4):
    choixJoueur[3-i]=int(n%10)
    n=(n-choixJoueur[3-i])/10 #cette fonction transforme un int de 4 chiffre en tableau de ces 4 même chiffres

  for i in range(4):
    if 0<choixJoueur[i]<6:
      choixvalide=choixvalide+1

  if choixvalide==4 and len(choixJoueur)==4:
    return choixJoueur
  else:
    print("entré invalide")
    ChoixJoueur() #récursif

  

def nbCommun(TabPC, TabJoueur):
  #variables locale

  cpt=0
  choixPC2 = TabPC.copy()

  for i in range(4):
    if choixPC2[i]==TabJoueur[i]:
      choixPC2[i]= 6
      cpt=cpt+1
  if cpt==4:
    print("Bravo ! Tu as réussi. La solution été : ", TabPC)
  elif cpt>1:
    print (cpt, "bonnes réponses, essaye encore !")
  else :
    print (cpt, "bonne réponse, essaye encore !")

  for i in range(4):
    if choixPC2[i]!=TabJoueur[i] and TabJoueur.count(choixPC2[i])>0:
      print("Mais", choixPC2[i], "est correct")
  return cpt
 

def Jeu():

  #variables locale
  nbJeu=0
  choixOrdinateur()
  print(choixPC) #debug  
  ChoixJoueur() #1ere manche

  while nbCommun(choixPC, choixJoueur) !=4:
    if nbJeu <=10: #soit 11 manches de plus donc 12 manches totals
      nbJeu+=1
      ChoixJoueur()
    else:
      print("PERDUUUUUU, c'était : ", choixPC)
      return

Jeu()