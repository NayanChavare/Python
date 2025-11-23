import os                      
class Books:
    def display(self):
        if os.path.exists("library.txt"):
            with open("library.txt",'r') as f:
                lines=f.readlines()
                for i in lines:
                    lis=i.split(",")
                    print(f"Book's Name : {lis[0]}\nAuthor's Name : {lis[1]}\nBook's ISBN : {lis[2]}\nBook's Status : {lis[3]}")
        else:
            print("No data found to display...")
    def add(self):
        t=input("Enter the Book's Title : ")
        a=input("Enter the name of the author : ")
        ib=input("Enter the Book's ISBN : ")
        s=input("Enter the status : ")
        if os.path.exists("library.txt"):
            with open("library.txt",'a') as file:
                file.write(f"{t},{a},{ib},{s}\n")
            print("Data saved...")
        else:
            with open("library.txt",'a') as file:
                file.write(f"{t},{a},{ib},{s}\n")
            print("Data saved...")
    
    def remove(self):
        if os.path.exists("library.txt"):
            with open("library.txt",'r') as f:
                lines=f.readlines()
            with open("library.txt",'w') as f:
                isbn=input("Enter the Book's ISBN to remove : ")
                for i in lines:
                    lis=i.split(",")
                    
                    if lis[2] != isbn:
                        f.write(i)
            print("Data removed...")
        else:
            print("No data found to remove...")
    
    def search(self):
        if os.path.exists("library.txt"):
            with open("library.txt",'r') as f:
                lines=f.readlines()
                found=False
                isbn=input("Enter the Book's ISBN to search : ")
                for i in lines:
                    lis=i.split(",")
                    if lis[2]==isbn:
                        print(f"Book's Name : {lis[0]}\nAuthor's Name : {lis[1]}\nBook's ISBN : {lis[2]}\nBook's Status : {lis[3]}")
                        found=True
                if not found:
                    print("Book not found...")
        else:
            print("No data found to search...")
    
    def issue(self):
        if os.path.exists("library.txt"):
            with open("library.txt",'r') as f:
                lines=f.readlines()
            with open("library.txt",'w') as f:
                isbn=input("Enter the Book's ISBN to issue : ")
                for i in lines:
                    lis=i.split(",")
                    if lis[2]==isbn:
                        lis[3]="Issued\n"
                        f.write(",".join(lis))
                    else:
                        f.write(i)
            print("Book issued...")
        else:
            print("No data found to issue...")
    
    def edit(self):
        print("What do you want to edit?\n1. Title\n2. Author\n3. ISBN\n4. Status")
        choice=int(input("Enter your choice : "))
        if os.path.exists("library.txt"):
            with open("library.txt",'r') as f:
                lines=f.readlines()
            with open("library.txt",'w') as f:
                isbn=input("Enter the Book's ISBN to edit : ")
                for i in lines:
                    lis=i.split(",")
                    if lis[2]==isbn:
                        if choice==1:
                            new_title=input("Enter the new title : ")
                            lis[0]=new_title
                        elif choice==2:
                            new_author=input("Enter the new author : ")
                            lis[1]=new_author
                        elif choice==3:
                            new_isbn=input("Enter the new ISBN : ")
                            lis[2]=new_isbn
                        elif choice==4:
                            new_status=input("Enter the new status : ")
                            lis[3]=new_status+"\n"
                        f.write(",".join(lis))
                    else:
                        f.write(i)
            print("Book details updated...")
        else:
            print("No data found to edit...")
    
    def return_book(self):
        if os.path.exists("library.txt"):
            with open("library.txt",'r') as f:
                lines=f.readlines()
            with open("library.txt",'w') as f:
                isbn=input("Enter the Book's ISBN to return : ")
                for i in lines:
                    lis=i.split(",")
                    if lis[2]==isbn:
                        lis[3]="Available\n"
                        f.write(",".join(lis))
                    else:
                        f.write(i)
            print("Book returned...")
        else:
            print("No data found to return...")


def main():
    b=Books()
    while True:
        print("\n1. Display Books\n2. Add Book\n3. Remove Book\n4. Search Book\n5. Issue Book\n6. Return Book\n7. Exit")
        choice=int(input("Enter your choice : "))
        if choice==1:
            b.display()
        elif choice==2:
            b.add()
        elif choice==3:
            b.remove()
        elif choice==4:
            b.search()
        elif choice==5:
            b.issue()
        elif choice==6:
            b.return_book()
        elif choice==7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

'''Output:
1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 2
Enter the Book's Title : Harry Potter
Enter the name of the author : JK
Enter the Book's ISBN : HP001
Enter the status : Available
Data saved...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 2
Enter the Book's Title : Dark Matter
Enter the name of the author : BC
Enter the Book's ISBN : BC001
Enter the status : Available
Data saved...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 2
Enter the Book's Title : Kill Joy
Enter the name of the author : HJ
Enter the Book's ISBN : HJ001
Enter the status : Available
Data saved...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 1
Book's Name : Dark Matter
Author's Name : DB
Book's ISBN : DM001
Book's Status : A

Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available

Book's Name : Dark Matter
Author's Name : BC
Book's ISBN : BC001
Book's Status : Available

Book's Name : Kill Joy
Author's Name : HJ
Book's ISBN : HJ001
Book's Status : Available


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 4
Enter the Book's ISBN to search : JK001
Book not found...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 4
Enter the Book's ISBN to search : HP001
Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 5
Enter the Book's ISBN to issue : HJ001
Book issued...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 1
Book's Name : Dark Matter
Author's Name : DB
Book's ISBN : DM001
Book's Status : A

Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available

Book's Name : Dark Matter
Author's Name : BC
Book's ISBN : BC001
Book's Status : Available

Book's Name : Kill Joy
Author's Name : HJ
Book's ISBN : HJ001
Book's Status : Issued


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 6
Enter the Book's ISBN to return : HJ001
Book returned...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 1
Book's Name : Dark Matter
Author's Name : DB
Book's ISBN : DM001
Book's Status : A

Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available

Book's Name : Dark Matter
Author's Name : BC
Book's ISBN : BC001
Book's Status : Available

Book's Name : Kill Joy
Author's Name : HJ
Book's ISBN : HJ001
Book's Status : Available


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 3
Enter the Book's ISBN to remove : HJ001
Data removed...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 1
Book's Name : Dark Matter
Author's Name : DB
Book's ISBN : DM001
Book's Status : A

Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available

Book's Name : Dark Matter
Author's Name : BC
Book's ISBN : BC001
Book's Status : Available


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 5
Enter the Book's ISBN to issue : DM001
Book issued...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 1
Book's Name : Dark Matter
Author's Name : DB
Book's ISBN : DM001
Book's Status : Issued

Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available

Book's Name : Dark Matter
Author's Name : BC
Book's ISBN : BC001
Book's Status : Available


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 6
Enter the Book's ISBN to return : DM001
Book returned...

1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 1
Book's Name : Dark Matter
Author's Name : DB
Book's ISBN : DM001
Book's Status : Available

Book's Name : Harry Potter
Author's Name : JK
Book's ISBN : HP001
Book's Status : Available

Book's Name : Dark Matter
Author's Name : BC
Book's ISBN : BC001
Book's Status : Available


1. Display Books
2. Add Book
3. Remove Book
4. Search Book
5. Issue Book
6. Return Book
7. Exit
Enter your choice : 7
Exiting...
'''