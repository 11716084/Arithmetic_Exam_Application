import random
while True:
    print("""Which level do you want? Enter a number:
    1 - simple operations with numbers 2-9
    2 - integral squares of 11-29""")
    user_choice = int(input())
    if int(user_choice) != 1 and int(user_choice) != 2:
        print("Incorrect format.")
    else:
        break

znak = ["+", "-", "*"]
attempt = 0
mark = 0


def funkcja():
    global attempt
    global mark
    global choice
    x = int(input())

    if choice[1] == "+":
        suma = (int(choice[0]) + int(choice[2]))
    elif choice[1] == "*":
        suma = (int(choice[0]) * int(choice[2]))
    elif choice[1] == "-":
        suma = (int(choice[0]) - int(choice[2]))
    if suma == x:
        attempt += 1
        mark += 1
        print("Right!")
    else:
        attempt += 1
        print("Wrong!")


def fun1():
    global attempt
    global mark
    global choice
    while True:
        if attempt < 5 and user_choice == 1:
            choice = [random.randint(2, 9), random.choice(znak), random.randint(2, 9)]

            print(*choice)
            while True:
                if attempt < 5:
                    try:
                        funkcja()
                        break

                    except (ValueError, SyntaxError, NameError):
                        print("Incorrect format.")
                else:
                    continue

        if attempt == 5:
            print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
            save = input()
            if save == "yes" or save == "YES" or save == "y" or save == "Yes":
                name = input("What is your name?")
                f = open("results.txt", "a", encoding='utf-8')
                f.write(f"{name}: {mark}/5 in level {user_choice} (simple operations with numbers 2-9).")
                f.close()
                print('The results are saved in "results.txt".')
                break
            if save == "no":
                break
            else:
                break


def fun2():
    global attempt
    global mark
    while True:
        if attempt < 5 and user_choice == 2:
            choice = random.randint(11, 29)
            print(choice)
            while True:
                if attempt < 5:
                    try:
                        x = int(input())
                        if choice*choice == x:
                            attempt += 1
                            mark += 1
                            print("Right!")
                            break
                        else:
                            attempt += 1
                            print("Wrong!")
                            break

                    except (ValueError, SyntaxError, NameError):
                        print("Incorrect format.")
                else:
                    continue
        if attempt == 5:
            print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
            save = input()
            if save == "yes" or save == "YES" or save == "y" or save == "Yes":
                name = input("What is your name?")
                f = open("results.txt", "a", encoding='utf-8')
                f.write(f"{name}: {mark}/5 in level {user_choice} (integral squares 11-29).")
                f.close()
                print('The results are saved in "results.txt".')
                break
            if save == "no":
                break
            else:
                break


if int(user_choice) == 1:
    fun1()
if int(user_choice) == 2:
    fun2()
