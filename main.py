expenses = []


def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, category, amount = line.strip().split(",")
                expenses.append([name, category, float(amount)])
    except FileNotFoundError:
        pass


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter expense amount: "))

    expenses.append([name, category, amount])

    with open("expenses.txt", "a") as file:
        file.write(name + "," + category + "," + str(amount) + "\n")

    print("Expense added.")


def view_expenses():
    print("\nExpenses:")

    for expense in expenses:
        print(expense[0], "-", expense[1], "-", expense[2])


def show_total():
    total = 0

    for expense in expenses:
        total = total + expense[2]

    print("Total expense:", total)


def main():
    load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


main()