'''
Name: Nayan Yogesh Chavare
Date: 03/10/2025
Lab Title: Simple Expense Tracker
Roll no.: 2501840021
'''
print("Welcome to Simple Expense Tracker.\nProvide me with expense's and I will help you manage it.")

categories=[]
amounts=[]
while True:
    category=input("Enter the category of the product: ")
    amount=input("Enter the amount of the category: ")
    amount=float(amount)
    
    if category in categories:
        index=categories.index(category)
        amounts[index]+=amount
    else:
        categories.append(category)
        amounts.append(amount)


    ch=input("Do you want to cotinue?(Y/N)\n")
    if ch.lower()=='y':
        continue
    elif ch.lower()=="n":
        break
    else:
        print("Sorry wrong input ending the process now!")
        break

print("Expense Summary:")
for i in range(1,len(categories)+1):
    print("---------------------------------")
    print(f"For {categories[i-1]} you have spend {amounts[i-1]}!")
    print("---------------------------------")
print(f"Total expenditure is {sum(amounts)}\nAverage expenditure is {sum(amounts)/len(amounts)}")
print("---------------------------------")

with open('expense.txt','a') as file:
    file.write("Expense Summary: \n")
    for i in range(1,len(categories)+1):
        file.write("---------------------------------\n")
        file.write(f"For {categories[i-1]} you have spend {amounts[i-1]}!\n")
        file.write("---------------------------------\n")
    file.write(f"Total expenditure is {sum(amounts)}\nAverage expenditure is {sum(amounts)/len(amounts)}\n")
    file.write("---------------------------------\n")

print("Expense summary saved in expense.txt...☑")

'''
Output 1:
Welcome to Simple Expense Tracker.
Provide me with expense's and I will help you manage it.
Enter the category of the product: Phone
Enter the amount of the category: 1000
Do you want to cotinue?(Y/N)
y
Enter the category of the product: Cloths
Enter the amount of the category: 200
Do you want to cotinue?(Y/N)
y 
Enter the category of the product: Toys
Enter the amount of the category: 100
Do you want to cotinue?(Y/N)
n
Expense Summary:
---------------------------------
For Phone you have spend 1000.0!
---------------------------------
---------------------------------
For Cloths you have spend 200.0!
---------------------------------
---------------------------------
For Toys you have spend 100.0!
---------------------------------
Total expenditure is 1300.0
Average expenditure is 433.3333333333333
---------------------------------
Expense summary saved in expense.txt...☑

Output 2:
Welcome to Simple Expense Tracker.
Provide me with expense's and I will help you manage it.
Enter the category of the product: Laptop
Enter the amount of the category: 5000
Do you want to cotinue?(Y/N)
y
Enter the category of the product: Bags
Enter the amount of the category: 500
Do you want to cotinue?(Y/N)
y
Enter the category of the product: Food Items
Enter the amount of the category: 1000
Do you want to cotinue?(Y/N)
n
Expense Summary:
---------------------------------
For Laptop you have spend 5000.0!
---------------------------------
---------------------------------
For Bags you have spend 500.0!
---------------------------------
---------------------------------
For Food Items you have spend 1000.0!
---------------------------------
Total expenditure is 6500.0
Average expenditure is 2166.6666666666665
---------------------------------
Expense summary saved in expense.txt...☑'''