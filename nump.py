import numpy as np
notes = np.array([11, 14,9,8])
moy= notes.mean()
best = notes.max()
worse = notes.min()

def sup10(notes):
 n = 0
 for i in range(0,4):
  if notes[i] >=10:
   n +=1
 return n

def ajoute2(notes):
 for i in range(0,4):
  notes[i] = notes[i] + 2
 return notes

nb = sup10(notes) 
p= ajoute2(notes)
print (f"la moyenne des notes est : {moy}")
print (f"la meilleure note est : {best}")
print (f"la  pire note est: {worse}")
print(f"les notes supérieurs ou égales à 10 sont au nombre de : {nb}")
print(f"le nouveau tableau : {p}")


