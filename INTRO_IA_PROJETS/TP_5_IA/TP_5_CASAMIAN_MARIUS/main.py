# import des librairies nécessaires
import time
from apyori import apriori
import re
import sys

#lecture du fichier en question
f = open(r'corpus.txt', encoding="UTF-8")

#mettre le fichier corpus.txt au propre grâce à cette fonction


def normalize(text):
  text = text.strip('\n').replace("!", "").replace("?", "").replace(
      ".", "").replace(",", "").replace(":", "").replace(";",
                                                         "").replace("-", "")
  return text


stopwords = {'the', 'a', 'of', 'for', 'in', 'and', 'de', 'et', 'pour'}

# création de la liste de transactions
transactions = []
for line in f:
  if len(line) > 1 and not line.startswith("#"):
    words = normalize(line).split()
    items = set()
    for word in words:
      if word not in stopwords:
        items.add(word)
    if len(items) != 0:
      transactions.append(sorted(items))
print(transactions)

# résultat dans un fichier
# on décide de créer une liste de tuples pour jouer sur les paramètres plus facilement

liste_param = [(0.01, 1.7, 0.2, 2), (0.01, 0.6, 1.2, 2), (0.01, 0.7, 1.5, 2),
               (0.01, 0.7, 1.2, 3)]

for j in liste_param:
  min_support, min_confidence, min_lift, min_length = j

  start_time = time.time()
  apriori_results = apriori(transactions,
                            min_support=min_support,
                            min_confidence=min_confidence,
                            min_lift=min_lift,
                            min_length=min_length)
  temps_exec = time.time() - start_time
  with open("resultat_apriori.txt", "w") as file:
    sys.stdout = file
    print(
        f"On utilise les paramètres suivants:\nmin_support={min_support}, min_confidence={min_confidence}, min_lift={min_lift}, min_length={min_length}\n"
    )

    print(f"Temps d'exécution est de: {temps_exec}s\n")
    print("Résultats d'exécution:\n")
    for i in apriori_results:
      print(i)

sys.stdout = sys.__stdout__
