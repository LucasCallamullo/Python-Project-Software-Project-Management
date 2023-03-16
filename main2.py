from functions import *


def menu(first_time):

    if first_time:
        print("1 - Load projects for first time.")
    else:
        print("=" * 50)
        print("1 - Adding more projects.")
    print("2 - Displaying projects.")
    print("3 - Updating project.")
    print("4 - Summary by programming language.")
    print("5 - Summary by year.")
    print("6 - Filter by programming language.")
    print("7 - Productivity.")
    print("0 - Quit.")
    return int(input("Please input an option: "))


def main():
    gProject = list()

    # To verify that they loaded data
    first_time = True
    # Because option 7 depends on option 5, it recycles a list that is created in option 5.
    independence_op5 = False

    op = -1
    while op != 0:

        op = menu(first_time)
        if first_time:
            if op == 1:
                n = int(input("Number of projects to load: "))
                cargar_proyectos(n, gProject)
                first_time = False

            elif op == 0:
                print("Thank you for using the program.")

            else:
                print("You must 'Load Projects for First Time' to execute the other options..")

        else:
            if op == 1:
                n = int(input("Number of projects to add: "))
                cargar_proyectos(n, gProject)
                # The flag is turned off in this case because more projects would be added, you will have to go through op 5 again 
                # if you want to use op 7
                independence_op5 = False

            elif op == 2:
                sort_for_title_op2(gProject)
                for i in gProject:
                    print(i)

            elif op == 3:
                x = int(input("Search Project Number: "))
                change_qty_and_date_op3(gProject, x)

            elif op == 4:
                acum_op4 = accumulators_op4(gProject)
                show_op4(acum_op4)

            elif op == 5:
                cont_op5 = counters_op5(gProject)
                show_op5(cont_op5)
                independence_op5 = True

            elif op == 6:
                ln = input("Enter language to search for (name or number): ")
                sort_for_num_op6(gProject)
                filter_for_language_and_show(gProject, ln)

            elif op == 7:
                if independence_op5:
                    may_op7 = calcular_may_op7(cont_op5)
                    show_op7(may_op7)
                else:
                    print("You need to perform 'Summary by Year' first. (Option 5)")

            elif op == 0:
                print("Thank you for using the program.")


if __name__ == "__main__":
    main()
