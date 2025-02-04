expenses=[]
def add_expense(expense,category):
    expenses.append((expense,category))
    print(f"{expense} has been added to category: {category}")
def view_expenses():
    if not expenses:
        print("No expenses added yet")
    else:
        print("Your expenses:")
        for index, (expense,category) in enumerate(expenses, start=1):
            print(f"{index}. {expense} - {category}")
def total_expenses():
    total= sum(amount for amount,category in expenses)
    print(f"Your total expenses are : {total}")
def highest_expense():
    highest= max(expenses, key=lambda x:x[0])
    print(f"Your highest expense is {highest[0]} in category {highest[1]}")
def lowest_expense():
    lowest=min(expenses, key=lambda x:x[0])
    print(f"Your lowest expense is {lowest[0]} in category {lowest[1]}")
def expenses_by_category():
    category_total={}
    for amount,category in expenses:
        category_total[category]=category_total.get(category,0)+amount
    print(f"Your expenses by category are:")
    for category, total in category_total.items():
            print(f"{category} : {total}")
while True:
    print("1.Add an expense")
    print("2.View expenses")
    print("3.Total expenses")
    print("4.Highest expense")
    print("5.Lowest expense")
    print("6.Expenses by category")
    print("7.Exit")
    choice =int(input("Enter your choice:"))
    if choice==1:
        expense=float(input("Enter the amount:"))
        category=input("Enter the category:")
        add_expense(expense,category)
    elif choice==2:
        view_expenses()
    elif choice==3:
        total_expenses()
    elif choice==4:
        highest_expense()
    elif choice==5:
        lowest_expense()
    elif choice==6:
        expenses_by_category()
    elif choice==7:
        print("You have exited expense tracker")
        break
    else:
        print("Invalid choice")


