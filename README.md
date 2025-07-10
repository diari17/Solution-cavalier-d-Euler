# Solution du Cavalier d'Euler ♞


Solution algorithmique du problème du parcours du cavalier utilisant le backtracking.

![Demo](demo.gif) *(Animation de la solution en action)*

## Principe Mathématique 🧮
Le problème consiste à trouver une séquence de mouvements d'un cavalier sur un échiquier de taille N×N telle que :
- Chaque case est visitée exactement une fois
- Les déplacements suivent les règles du jeu d'échecs (en L)
- Solution utilisant l'algorithme de **backtracking** avec heuristique

## Fonctionnalités Techniques ⚙️
def find_knight_tour(size, start_x, start_y):
    # Implémentation du backtracking avec...
    # 1. Vérification des mouvements valides
    # 2. Marquage des cases visitées
    # 3. Retour arrière si impasse

Visualisation 🎨
L'interface affiche :
- La progression du cavalier case par case
- Le numéro de chaque mouvement
- Le temps d'exécution
