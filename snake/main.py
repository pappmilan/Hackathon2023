import random

#A pálya mérete
width = 60
height = 30

# A kígyó kezdőhelye és iránya
snakex = random.randint(2, width - 3)
snakey = random.randint(2, height - 3)

dx = 1
dy = 0

# A pálya feldolgozása
field = [[' '] * width for _ in range(height)]
snake_parts = [(snakex, snakey)]

# A pálya szélei
for i in range(width):
    field[0][i] = '*'
    field[height - 1][i] = '*'
for i in range(height):
    field[i][0] = '*'
    field[i][width - 1] = '*'


# A kígyó megjelenítése a pályán
def draw_snake():
    for i, (x, y) in enumerate(snake_parts):
        field[y][x] = '@'



# Pálya és péntszám megjelenítése
def draw_field():
    for row in field:
        print(''.join(row))



# Játék működése
while True:
    field = [[' '] * width for _ in range(height)]
    draw_snake()

    # Pálya széleinek kirajzolása
    for i in range(width):
        field[0][i] = '*'
        field[height - 1][i] = '*'
    for i in range(height):
        field[i][0] = '*'
        field[i][width - 1] = '*'

    draw_field()

    if snake_parts[-1][0] + dx == -1 or snake_parts[-1][0] + dx == width or \
            snake_parts[-1][1] + dy == -1 or snake_parts[-1][1] + dy == height:
        print("Megérintetted a kerítést!")
        print("Most ennyi volt, szép napot!")
        break

    for i in range(len(snake_parts) - 1):
        snake_parts[i] = snake_parts[i + 1]

    snakex += dx
    snakey += dy
    snake_parts[-1] = (snakex, snakey)


    print("merre?")

    #Irányítás
    command = input()

    if command == 'balra':
        dx = -1
        dy = 0
    elif command == 'jobbra':
        dx = 1
        dy = 0
    elif command == 'fel':
        dx = 0
        dy = -1
    elif command == 'le':
        dx = 0
        dy = 1
    elif command == 'meguntam':
        print("Most ennyi volt, szép napot!")
        break