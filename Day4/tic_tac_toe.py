import random


# Player Base Class
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        """Abstract method, implemented by subclasses"""
        raise NotImplementedError(
            "This method should be overridden by subclasses")


# Human Player
class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                move = int(
                    input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid choice! Pick between 1 and 9.")
                    continue

                row, col = divmod(move - 1, 3)
                if board.update(row, col, self.symbol):
                    break
                else:
                    print("Cell already taken. Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")


# Computer Player
class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")
        empty = board.get_empty_cells()
        row, col = random.choice(empty)
        board.update(row, col, self.symbol)


# Board Class
class Board:
    def __init__(self):
        self.__grid = [[" " for _ in range(3)] for _ in range(3)]

    def __str__(self):
        """Return a string representation of the board (instead of display())."""
        rows = []
        for i, row in enumerate(self.__grid):
            rows.append(" | ".join(row))
            if i < 2:
                rows.append("---------")
        return "\n".join(rows)

    def update(self, row, col, symbol):
        if self.__grid[row][col] == " ":
            self.__grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.__grid[i][j] == symbol for j in range(3)) or \
               all(self.__grid[j][i] == symbol for j in range(3)):
                return True
        if all(self.__grid[i][i] == symbol for i in range(3)) or \
           all(self.__grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.__grid for cell in row)

    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.__grid[i][j] == " "]


# Game Class
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_turn = 0

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        print(self.board)
        while True:
            current_player = self.players[self.current_turn]
            current_player.make_move(self.board)
            print(self.board)

            if self.board.check_winner(current_player.symbol):
                print(f"\n🎉 {current_player.name} wins!")
                break
            if self.board.is_full():
                print("\nIt's a draw!")
                break

            self.switch_turns()


# Main Function
def main():
    print("Welcome to Tic-Tac-Toe!")

    # Validate game mode input (must be 1 or 2)
    while True:
        try:
            mode = int(
                input("Do you want to play with a friend (1) or vs computer (2)? "))
            if mode in [1, 2]:
                break
            else:
                print("Please enter only 1 or 2.")
        except ValueError:
            print("Enter a number (1 or 2) !!")

    # Human vs Human
    if mode == 1:
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")

        # Player 1 chooses symbol
        while True:
            symbol1 = input(f"{name1}, choose your symbol (X/O): ").upper()
            if symbol1 in ["X", "O"]:
                break
            else:
                print("Invalid choice! Please choose X or O.")

        symbol2 = "O" if symbol1 == "X" else "X"
        player1 = HumanPlayer(name1, symbol1)
        player2 = HumanPlayer(name2, symbol2)

    # Human vs Computer
    elif mode == 2:
        name = input("Enter your name: ")

        # Human chooses symbol
        while True:
            symbol = input(f"{name}, choose your symbol (X/O): ").upper()
            if symbol in ["X", "O"]:
                break
            else:
                print("Invalid choice! Please choose X or O.")

        player1 = HumanPlayer(name, symbol)
        comp_symbol = "O" if symbol == "X" else "X"
        player2 = ComputerPlayer("Computer", comp_symbol)

    # Start the game
    game = Game(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
