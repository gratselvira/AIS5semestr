#игра крестики-нолики
import os #чтобы получить доступ к файлу
import json

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print('|'.join(row))
            print('-' * (2 * self.size - 1))

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)

    def make_move(self, row, col, symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Проверка горизонталей и вертикалей
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True
        # Проверка диагоналей
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size-i-1] == symbol for i in range(self.size)):
            return True
        return False

class Game:
    def __init__(self, size=3):
        self.size = size
        self.board = Board(size)
        self.players = []
        self.current_player_index = 0
        self.moves = 0

    def add_player(self, name, symbol):
        self.players.append(Player(name, symbol))

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def current_player(self):
        return self.players[self.current_player_index]

    def play(self):
        while True:
            self.board.display()
            player = self.current_player()
            print(f"{player.name}'s turn ({player.symbol}):")

            try:
                row, col = map(int, input(f"Введите строку и столбец (0-{self.size-1}): ").split())
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите строку и столбец в виде двух чисел, разделенных пробелом.")
                continue

            if not (0 <= row < self.size and 0 <= col < self.size):
                print("Недопустимый ход. Попробовать снова.")
                continue

            if not self.board.make_move(row, col, player.symbol):
                print("Ячейка уже занята. Пробовать снова.")
                continue

            self.moves += 1

            if self.board.check_winner(player.symbol):
                self.board.display()
                print(f"{player.name} победил!")
                player.wins += 1
                break

            if self.moves == self.size ** 2:
                self.board.display()
                print("Это ничья!")
                break

            self.switch_player()


    def save_game(self, filename):
        game_data = {
            'size': self.size,
            'grid': self.board.grid,
            'current_player_index': self.current_player_index,
            'moves': self.moves,
            'players': [{'name': p.name, 'symbol': p.symbol, 'wins': p.wins} for p in self.players]
        }
        with open(filename, 'w') as f:
            json.dump(game_data, f)
        print(f"Игра сохранена в {filename}")

    def load_game(self, filename):
        if not os.path.exists(filename):
            print(f"Сохраненная игра с таким названием {filename} не найдена ")
            return False

        with open(filename, 'r') as f:
            game_data = json.load(f)

        self.size = game_data['size']
        self.board = Board(self.size)
        self.board.grid = game_data['grid']
        self.current_player_index = game_data['current_player_index']
        self.moves = game_data['moves']
        self.players = [Player(p['name'], p['symbol']) for p in game_data['players']]

        print(f"Игра зугружена из файла {filename}")
        return True

def main():
    size = int(input("Введите размер доски: "))
    game = Game(size)
    game.add_player(input("Введите имя игрока 1 (X): "), 'X')
    game.add_player(input("Введите имя игрока 2 (O): "), 'O')

    if input("Вы хотите загрузить сохраненную игру? (д/н): ").lower() == 'д':
        filename = input("Введите название файла: ")
        if game.load_game(filename):
            game.play()
        else:
            print("Начать новую игру")
            game.play()
    else:
        game.play()

    if input("Сохранить игру? (д/н): ").lower() == 'д':
        filename = input("Введите название файла: ")
        game.save_game(filename)

if __name__ == "__main__":
    main()
