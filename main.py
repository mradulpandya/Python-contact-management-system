from dbhelper import db

def main():
    DB = db()
    while True:
        print("**********WELCOME**********")
        print()
        print("Press 1 to Insert new user")
        print("Press 2 to Display all user")
        print("Press 3 to Delete user")
        print("Press 4 to update User")
        print("Press 5 to Exit")
        print()
        try:
            choice=int(input())
            if(choice==1):
                uid = int(input("Enter user Id: "))
                uname = input("Enter user Name: ")
                uphone = input("Enter user Phone: ")
                DB.insert_user(uid, uname, uphone)
            elif choice==2:
                DB.fetch_all()
            elif choice==3:
                uid = int(input("Enter USer id to which you want delete: "))
                DB.delete_user(uid)
            elif choice==4:
                uid = int(input("Enter user Id to update: "))
                uname = input("Enter new user Name: ")
                uphone = input("Enter new user Phone: ")
                DB.update_user(uid, uname, uphone)
            elif choice==5:
                break
            else:
                print("Invalid choice : Try again")
        except exception as e:
            print(e)
            print("Invalid detail")

if __name__ == "__main__":
    main()


