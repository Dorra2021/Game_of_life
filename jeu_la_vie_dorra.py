import numpy as np
from matplotlib import pyplot as plt

frame =  np.array([[0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,1,1,1,1,1,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0]])

#yassmine ici j'ai calculé le nombre des voisins (la fonction me donne un entier qui représente le nombre des voisins)
def compute_number_neighbors(paded_frame,index_line,index_column):
  neighbors=0
  for i in range(index_line-1,index_line+2):
    for j in range(index_column-1,index_column+2):
      if i!=index_line or j!=index_column:
        neighbors+=paded_frame[i][j]
  return neighbors
#je vais parcourir la matrice paded_frame mais je veux savoir les elements de la matrice avant l'ajout des zeros(avant de la rendre comme paded frame)
def compute_next_frame(frame):
  paded_frame=np.pad(frame,1,mode='constant')
#on va commencer par la ligne 1 jusqu'à u-1
#la colonne 1 jusqu'à la colonne v-1
#(puisqu'on veut parcourir la matrice initiale avant d'ajouter les zéros et donc on entre au niveau de la matrice avec des zéros pour prendre en considérations les elements qui se trouvent au niveau des bordures )
#on peut donc prendre en consideration les voisins des elements des bordures
#ceci nous permet de
  for u in range(1,len(paded_frame)-1):
    for v in range(1,len(paded_frame[0])-1):
      voisins=compute_number_neighbors(paded_frame,u,v)
#la fonction compute number neighbors me donne le nombre des voisins seulement
      i=u-1
      j=v-1
      if frame[i][j]==0 and voisins==3:
        frame[i][j]=1
      elif frame[i][j]==1 and (voisins<2 or voisins>3):
        frame[i][j]=0

  return frame
while True:
    frame=compute_next_frame(frame)
    plt.imshow(frame, interpolation='nearest')
    plt.pause(3)
    plt.close()