def is_valid_move(x, y, board_size, visited):
    return 0 <= x < board_size and 0 <= y < board_size and not visited[x][y]

def find_knight_tour(board_size, start_x, start_y):
    # Les 8 mouvements possibles du cavalier
    moves = [
        (2, 1), (2, -1),
        (-2, 1), (-2, -1),
        (1, 2), (-1, 2),
        (1, -2), (-1, -2)
    ]
    
    # Initialisation du plateau
    visited = [[False for _ in range(board_size)] for _ in range(board_size)]
    path = []
    
    # Fonction récursive avec backtracking
    def backtrack(x, y, step):
        # Marquer la case comme visitée et l'ajouter au chemin
        visited[x][y] = True
        path.append((x, y))
        
        # Si toutes les cases sont visitées, on a trouvé une solution
        if step == board_size * board_size - 1:
            return True
        
        # Essayer tous les mouvements possibles
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            
            if is_valid_move(next_x, next_y, board_size, visited):
                if backtrack(next_x, next_y, step + 1):
                    return True
        
        # Backtrack si aucun mouvement ne mène à une solution
        visited[x][y] = False
        path.pop()
        return False
    
    # Démarrer l'algorithme
    if backtrack(start_x, start_y, 0):
        return path
    else:
        return None