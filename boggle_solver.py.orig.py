class Boggle:
    def __init__(self, board, dictionary):
        """
        Initialize the Boggle game with the given board and dictionary.
        """
        if not self.is_valid_grid(board):
            self.board = []
            self.n = 0
        else:
            self.board = [[cell.upper() for cell in row] for row in board]
            self.n = len(board)

        # Store dictionary as a set for O(1) lookups
        self.dictionary = set(word.upper() for word in dictionary)
        # Precompute all possible prefixes
        self.prefixes = self.build_prefixes(self.dictionary)
        # Directions for 8 possible moves (horizontal, vertical, diagonal)
        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

    def is_valid_grid(self, board):
        """
        Check if the input grid is valid.
        """
        if not board or not all(board):
            return False
        row_lengths = set(len(row) for row in board)
        return len(row_lengths) == 1  # All rows should have the same length

    def build_prefixes(self, dictionary):
        """
        Build a set of all possible prefixes from the dictionary.
        """
        prefixes = set()
        for word in dictionary:
            for i in range(1, len(word)):
                prefixes.add(word[:i])
        return prefixes

    def dfs(self, i, j, visited, current_word):
        """
        Perform Depth-First Search from the cell (i, j).
        """
        if (i < 0 or i >= self.n or j < 0 or
                j >= len(self.board[i]) or visited[i][j]):
            return

        current_word.append(self.board[i][j])

        # Handle cases for 'Q' needing 'U' and 'S' needing 'T'
        extra_chars_map = {'Q': 'U', 'S': 'T'}
        extra_chars = 0
        if self.board[i][j] in extra_chars_map:
            current_word.append(extra_chars_map[self.board[i][j]])
            extra_chars += 1

        word = ''.join(current_word)

        # Check if the current sequence is a valid prefix or word
        if word not in self.prefixes and word not in self.dictionary:
            self.backtrack(current_word, extra_chars)
            return

        if word in self.dictionary and len(word) >= 3:
            self.found_words.add(word)

        visited[i][j] = True
        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            self.dfs(ni, nj, visited, current_word)

        visited[i][j] = False
        self.backtrack(current_word, extra_chars)

    def backtrack(self, current_word, extra_chars):
        """
        Backtrack by removing the last added character(s) from current_word.
        """
        for _ in range(1 + extra_chars):
            if current_word:
                current_word.pop()

    def find_valid_words(self):
        """
        Find all valid words on the Boggle board based on the dictionary.
        """
        self.found_words = set()
        if self.n == 0:
            return []
        visited = [[False for _ in row] for row in self.board]

        for i in range(self.n):
            for j in range(len(self.board[i])):
                self.dfs(i, j, visited, [])

        return sorted(self.found_words)

    def getSolution(self):
        """
        Get the solution for the Boggle game.
        This method returns the valid words found on the board.
        """
        return self.find_valid_words()


def main():
    """
    Example usage of the Boggle class.
    """
    grid = [
        ['D', 'E', 'F'],
        ['E', 'A', 'B'],
        ['E', 'B', 'C'],
        ['E', 'C', 'B'],
        ['E', 'D', 'B'],
        ['E', 'F', 'B'],
        ['E', 'G', 'H'],
        ['E', 'H', 'I'],
        ['E', 'I', 'H']
    ]

    dictionary = [
        'DEF', 'EAB', 'EBC', 'ECB', 'EDB',
        'EFB', 'EGH', 'EHI', 'EIH'
    ]
    mygame = Boggle(grid, dictionary)

    # Optionally, call the getSolution method to find valid words
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
