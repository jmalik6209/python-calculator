import  statistics

print("Welcome to the basic calculator!")
print('')


def Basic_Operations():
    print('Welcome to the Basic Operations Calculator')
    print('')
    print('''
    When inputting operations, please use the following key:

    Symbol:   |   Operation:
    -----------------------------
    +         |   Addition
    -         |   Subtraction
    *         |   Multiplication
    /         |   Division
    **        |   To the power of (Exponents)
    () or []  |   Parentheses or Brackets
    ''')
    print('')

    calculation=input('Please enter the expression you would like the calculator to solve (no variables): ')
    answer = eval(calculation)
    print(float(answer))
    print('')
    while(True):
        repeat = str(input('Would you like to enter another expression, or exit to main menu (no to exit, yes to continue)?'))

        if repeat=='yes':
            Basic_Operations()
            break
        elif repeat=='no':
            menu()
            break
        else:
            continue


def Statistics():
    print('Welcome to the Statistics Calculator')
    print('''
    Menu:
    1. Mean
    2. Median
    3. Mode
    4. Range
    5. Absolute Value
    6. Return to Main Menu
    ''')
    print('')
    choice=input('Please enter the number of the calculator you would like to use: ')

    if choice=='1':
        calculation=input('Please enter the data set to evaluate, each number separated by spaces:')
        dataset=calculation.split()
        for i in range(len(dataset)):
            dataset[i]=float(dataset[i])
        print(statistics.mean(dataset))
        print(Statistics())
    
    elif choice=='2':
        calculation=input('Please enter the data set to evaluate, each number separated by spaces:')
        dataset=calculation.split()
        for i in range(len(dataset)):
            dataset[i]=float(dataset[i])
        print(statistics.median(dataset))
        print(Statistics())
    
    elif choice=='3':
        calculation=input('Please enter the data set to evaluate, each number separated by spaces:')
        dataset=calculation.split()
        for i in range(len(dataset)):
            dataset[i]=float(dataset[i])
        print(statistics.mode(dataset))
        print(Statistics())

    elif choice=='4':
        calculation=input('Please enter the data set to evaluate, each number separated by spaces:')
        dataset=calculation.split()
        for i in range(len(dataset)):
            dataset[i]=float(dataset[i])
        maximum=max(dataset)
        minimum=min(dataset)
        print(maximum-minimum)
        print(Statistics())

    elif choice=='5':
        calculation=input('Please enter the number you want to calculate the absolute value of:')
        print(abs(float(calculation)))
        print(Statistics())

    elif choice=='6':
        menu()
    
    else: 
        print('Please enter a valid option')
        Statistics()


def menu():
    while(True):
        print('''
        1. Basic Operations
        2. Statistics
        3. Quit
        ''')
        print('')
        choice = str(input("Please enter the number of the calculator you would like to use: "))

        if choice=='1':
            Basic_Operations()
            break

        elif choice=='2':
            Statistics()
            break


        elif choice=='3':
            print('Okay, thanks for using this program!')
            break
        
        else:
            print('Please enter a valid option')
            continue

menu()