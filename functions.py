import random
from class_project import *


# ===============================================================================================
#                                   OPTION 1
# ===============================================================================================
def cargar_proyectos(n, gProyecto):

    titles = "Lucca", "Cars", "Madagascar", "Simpsons", "Spider-Man", "Venom"

    # This was done to have no limit on the number of projects that can be added., min = 1
    max_qty_projs = len(gProyecto) + 1

    for i in range(n):
        num = random.randint(1, max_qty_projs)
        title = random.choice(titles)
        day = random.randint(1, 31)
        month = random.randint(1, 12)
        year = random.randint(2000, 2022)
        lang = random.randint(0, 10)
        qty_line = random.randint(300, 700)

        # For valid number of project don't repeat
        num_valid = valid_num_project(gProyecto, num)
        while not num_valid:
            num = random.randint(1, max_qty_projs)
            # This section was created to remove the limit on the number of Project Numbers that can be loaded.
            num_valid = valid_num_project(gProyecto, num)
            if not num_valid:
                max_qty_projs += 1


        proy = Project(num, title, day, month, year, lang, qty_line)
        gProyecto.append(proy)


def valid_num_project(gProyecto, num):
    for i in gProyecto:
        if i.num == num:
            return False
    return True


# ===============================================================================================
#                                   OPTION 2
# ===============================================================================================
def sort_for_title_op2(gProyecto):
    n = len(gProyecto)
    for i in range(n-1):
        for j in range(i+1, n):
            if gProyecto[i].title > gProyecto[j].title:
                gProyecto[i], gProyecto[j] = gProyecto[j], gProyecto[i]


# ===============================================================================================
#                                   OPTION 3
# ===============================================================================================
def change_qty_and_date_op3(gProject, x):
    # Reciclo la funcion de la opcion 1.
    if not valid_num_project(gProject, x):
        opc = input("Do you want to modify the project? Y/N")
        if opc.lower() == "y":
            qty = int(input("New Lines of Code Quantity: "))
            day, month, year = valid_date_op3()
            for i in range(len(gProject)):
                if gProject[i].num == x:
                    gProject[i].qty_line = qty
                    gProject[i].day = day
                    gProject[i].month = month
                    gProject[i].year = year
                    print("The updated project is as follows: ")
                    print(gProject[i])
                    break
        else:
            return
    else:
        print("No project was found with that number.")


def valid_date_op3():
    day = int(input("Enter new day: "))
    while not 1 <= day <= 31:
        day = int(input("Enter new day: (1-31): "))

    month = int(input("Enter new month: "))
    while not 1 <= month <= 12:
        month = int(input("Enter new month (1-12): "))

    year = int(input("Enter new year: "))
    while not 2000 <= year <= 2022:
        year = int(input("Enter new year (2000-2022): "))

    return day, month, year


# ===============================================================================================
#                                   OPTION 4
# ===============================================================================================
def accumulators_op4(gProject):
    acum = [0] * 11
    for i in gProject:
        acum[i.lang] += i.qty_line
    return acum


def show_op4(acum_op4):
    print("=" * 50)
    print('{:<20}'.format("language") + '{:<20}'.format("Qty. of Lines of Code"))

    for i in range(len(acum_op4)):
        x = languajes(i)
        print('{:<20}'.format(x) + '{:<20}'.format(acum_op4[i]))


# ===============================================================================================
#                                   OPTION 5
# ===============================================================================================
def counters_op5(gProject):
    cont = [0] * 23
    for i in gProject:
        cont[(i.year - 2000)] += 1
    return cont


def show_op5(count_op5):
    print("=" * 50)
    print('{:<12}'.format("Year") + '{:<20}'.format("Qty. Projects"))
    for i in range(len(count_op5)):
        if count_op5[i] > 0:
            print('{:<12}'.format(i+2000) + '{:<20}'.format(count_op5[i]))


# ===============================================================================================
#                                   OPTION 6
# ===============================================================================================
def sort_for_num_op6(gProject):
    n = len(gProject)
    for i in range(n-1):
        for j in range(i+1, n):
            if gProject[i].num > gProject[j].num:
                gProject[i], gProject[j] = gProject[j], gProject[i]


def filter_for_language_and_show(gProject, ln):
    print("=" * 50)
    one_time = True
    ln = ln.lower()
    for i in range(len(gProject)):
        if gProject[i].lang == ln or languajes(gProject[i].lang).lower() == ln:
            if one_time:
                print('{:<15}'.format("Project ID") + '{:<20}'.format("Language"))
                print('{:<15}'.format(gProject[i].num) + '{:<20}'.format(languajes(gProject[i].lang)))
                one_time = False
            else:
                print('{:<15}'.format(gProject[i].num) + '{:<20}'.format(languajes(gProject[i].lang)))


# ===============================================================================================
#                                   OPTION 7
# ===============================================================================================
def calcular_may_op7(acum_op5):
    max_list = list()
    for i in range(len(acum_op5)):
        if acum_op5[i] == max(acum_op5):
            max_list.append(i+2000)
    return max_list


def show_op7(may_op7):
    n = len(may_op7)
    print("=" * 50)
    if n == 1:
        print("The year with the most updated projects was:", (may_op7[0]))
    elif n > 1:
        print("The years with the most updated projects were:")
        for i in range(n):
            print("Year:", may_op7[i])
