
dic={}

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    category = input(f"Enter category for expense {i+1}: ")
    amount = float(input(f"Enter amount for {category}: "))
    if category in dic.keys():
        dic[category]+=amount
    else:
        dic[category]=amount
c=list(dic.keys())
a=list(dic.values())
total = sum(a)
average = total / len(a) if a else 0


print("\n--- Expense Summary ---")
for i in range(len(c)):
    print(f"{i+1}. {c[i]:<15} : ₹{a[i]:.2f}")

print(f"\nTotal Expense   : ₹{total}\n")
print(f"Average Expense : ₹{average}")

with open("expenses.txt", "a") as file:
    file.write("--- Expense Summary ---\n")
    for i in range(len(c)):
        file.write(f"{i+1}. {c[i]:<15} : ₹{a[i]:.2f}\n")
    file.write(f"\nTotal Expense   : ₹{total}\n")
    file.write(f"Average Expense : ₹{average}\n")

print("\nExpenses saved to 'expenses.txt'")
