#!/usr/bin/python3
import random
import os


def clear_screen():
    """Clear the terminal screen (Windows / Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # choose unique mine positions
        self.mines = set(random.sample(range(width * height), mines))
        # board data (not really used for logic, but kept)
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # track which cells are revealed
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Reveal a cell. Return False if it's a mine, True otherwise."""
        if (y * self.width + x) in self.mines:
            return False

        if self.revealed[y][x]:
            # already revealed, nothing to do
            return True

        self.revealed[y][x] = True

        # if no mines nearby, recursively reveal neighbors
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height \
                            and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def has_won(self):
        """Return True if all non-mine cells have been revealed."""
        for y in range(self.height):
            for x in range(self.width):
                idx = y * self.width + x
                if idx not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of range.")
                    continue

                # reveal the chosen cell
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # check winning condition
                if self.has_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


if name == "__main__":
    game = Minesweeper()
    game.play()
