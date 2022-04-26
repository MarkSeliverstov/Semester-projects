# Mark Seliverstov, I. ročník
# zimní semestr 2021/22
# Programování NPRG030

def NapisVelikost():
    velikost = input("Enter the sudoku difficulty (4/9/16): ")
    try:
        velikost = int(velikost)
    except ValueError:
        velikost = 0

    # pokud není zadáno číslo, pak se to bude opakovat
    while velikost != 4 and velikost != 9 and velikost != 16:
        velikost = input("Try entering the sudoku difficulty again (4/9/16): ")
        try:
            velikost = int(velikost)
        except ValueError:
            velikost = 0
    return velikost


def NapisData(grid):
    for v in range(velikost):
        radek = [int(i) for i in input(f"Enter the {v + 1} row of sudoku separated by a space: ").split()]
        while len(radek) != velikost: # kontrola počtu čísel
            if len(radek) != velikost:
                # čísla z řádku jsou zapsána do listu
                radek = [int(i) for i in input(f"Enter the {v + 1} row of sudoku separated by a space: ").split()]
        grid += [radek]
    return grid


def check(j, i, k, velikost):
    # Funkce kontroluje v každém řádku, v každém sloupci a v každém dílčích čtverců
    # jsou použity vždy všechny číslice, každá právě jednou
    # True je správné
    # False není spravneé

    global grid
    for x in range(len(grid)):  # kontroluje vertikálně
        if k == grid[i][x]:
            return False
    for y in range(len(grid)):  # kontroluje horizontálně
        if k == grid[y][j]:
            return False

    # kontroluje v každé buňce
    v = int(velikost ** (1 / 2))
    x0 = (j // v) * v
    y0 = (i // v) * v
    for i in range(v):  # kontroluje v každé buňce
        for j in range(v):
            if k == grid[y0 + i][x0 + j]:
                return False
    return True


def reseni(velikost):
    global grid
    global jet

    for y in range(len(grid)):  # prochází každé číslo
        for x in range(len(grid[0])):
            if grid[y][x] == 0:  # pokud hodnota je 0, pak bereme možné číslo na místo této hodnoty
                for k in range(1, velikost + 1):
                    if check(x, y, k, velikost):  # kontrola: je možné dát určité číslo namísto 0
                        grid[y][x] = k
                        reseni(velikost)
                        if jet == True:  # aby se při návratu výsledek nezměnil
                            grid[y][x] = 0
                return grid
    jet = False


def vystup(grid):
    global velikost

    n = int(velikost ** (1 / 2))  # kolik čísel v jedné buňce

    # rozdělení na části
    for q in range(len(grid) // n):
        for i in grid[:n]:
            raw = []
            for k in range(n):
                for j in i[k * n:(k + 1) * n:1]:
                    if j <= 9:
                        raw += " " + str(j) + " "
                    else:
                        raw += str(j) + " "
                if k != n - 1:
                    raw += "|"
            print("".join(raw))
            grid.remove(i)
        if q != n - 1:
            print("".join(["-" for i in range(len(raw))]))


jet = True
end = False
grid = []

# Konec?
while end == False:
    if end == False:
        # provádí se, pokud jsou data zadána nesprávně
        if grid != []:
            print("\n")
            print("ERROR! Try other values...")
        grid = []
        correctly = True

        # Vstup:
        # 1) je velikost sudoku a pokud je vstup nesprávný, bude se opakovat vstup
        velikost = NapisVelikost()
        # 2) je data sudoku a pokud je vstup nesprávný, bude se opakovat vstup
        grid = NapisData(grid)

        # Kontrola vstupu a pokud je vstup nesprávný, bude se opakovat vstup
        for y in range(velikost):
            for x in range(velikost):
                if grid[y][x] != 0:
                    pam = grid[y][x]
                    grid[y][x] = 0
                    if not check(x, y, pam, velikost):
                        correctly = False
                    else:
                        grid[y][x] = pam

        # Reseni
        if correctly == True:
            jet = True
            reseni(velikost)
            print("Sudoku solved:")
            vystup(grid)

            # Jeste?
            if input("would you like to do it again?(ano/ne): ") == "ne":
                end = True
            print('\n')
            grid = []

"""
Priklad
7 0 0 0 1 0 0 0 9
0 0 0 0 0 0 4 1 0
5 0 9 0 0 6 0 0 7
0 0 0 0 0 0 0 0 2
1 8 0 0 0 0 9 0 5
0 0 0 0 0 5 0 8 0
0 0 2 8 4 0 0 9 0
0 6 0 0 0 0 1 5 8
0 0 0 6 0 0 0 0 0
"""