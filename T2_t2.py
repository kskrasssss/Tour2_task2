matrix = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
]
start_x = 0
start_y = 0
endx = 4
endy = 4
class FindTheExit:
    def valid_move(self, matrix, visited, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0 and not visited[x][y]
    # Перевірка, чи можна зробити крок в матриці(лабіринті)
    # 1) х по рядках повинен бути >= 0 і < довжини матриці 
    # 2) теж саме для у по кількості вкладених списків(стовпців)
    # 3) 0 - хід, 1 - шлях тому координати повинні дорівнюватись 0 в списку
    # 4) комірка має бути не відвіданою

    def find_path(self, matrix, x, y, endx, endy, path, visited): # path - список, в якому буде зберугатися дійсний шлях(вихід)
        if x == endx and y == endy:
            path.append((x, y))
            return True

        if self.valid_move(matrix, visited, x, y):
            path.append((x, y)) # За допомогою подвійних дужок, додаємо кортеж з двох чисел до списку 'path' --> (x, y)
            visited[x][y] = True

            if self.find_path(matrix, x + 1, y, endx, endy, path, visited):
                return True
            elif self.find_path(matrix, x - 1, y, endx, endy, path, visited):
                return True
            elif self.find_path(matrix, x, y + 1, endx, endy, path, visited):
                return True
            elif self.find_path(matrix, x, y - 1, endx, endy, path, visited):
                return True

            path.pop()   # якщо шлях не веде до виходу
            visited[x][y] = False
            return False

    def solve_matrix(self, matrix, start_x, start_y, endx, endy):
        path = [] # оголошую список, щоб він зберігся, для подальшого виводу після завершення функції.
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
        if self.find_path(matrix, start_x, start_y, endx, endy, path, visited):
            return path
        else:
            return "Виходу не існує."
        print(visited)

finder = FindTheExit()
path = finder.solve_matrix(matrix, start_x, start_y, endx, endy)

if isinstance(path, list):
    print("Шлях до виходу з лабіринту: ", *path, sep=' --> ')
else:
    print(path)
