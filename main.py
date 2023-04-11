import mysql.connector

global accounts 

accounts={'1234567':{"name": "Keatra N",
                             "PIN": 1214, 
                             "type": "savings"}}
def display_menu():
    print("\n **Menu**")
    print("1. Check Balance ")
    print("2. Withdrawal")
    print("3. Deposit")
    print("4. Create Account")
    print("5. Delete Account")
    print("6. Edit Account")
    print("7. Exit\n")

# def user_selection():
#     try:
#       user_choice = int(input("Enter a number between 1-5: "))
#     except ValueError:
#       print("\nSorry, Not a Valid Choice. Please try again! \n")
#       user_selection()
#     if user_choice == 1:  #Go to Store Inventory.
#         #print('show inventory')
#         display_inventory()
#         user_selection()
#     elif user_choice == 2:  #Initiate New Product Process.
#         #print('add a new product \n')
#         add_new_product()
#         user_selection()
#     elif user_choice == 3:  #Initiate Buying a New Product.
#         #print("buying a product \n")
#         order_product()
#         user_selection()
#     elif user_choice == 4:  #Initiate Removing a Product.
#         #print('remove a product \n')
#         remove_product()
#         user_selection()
#     elif user_choice == 5:  #Exit the program
#         print("program ends.")
#     else:
#         print("\nSorry, Not a Valid Choice. Please try again! \n")
#         user_selection()

def main():
    print("Welcome to Nesbitt Bank Online (NBO)")
    
    connection = mysql.connector.connect(host = 'localhost',
                                        database = 'example',
                                        user = 'root',
                                        password = 'Y+kTRisJ')
    

    acct_num = input("Enter your account number (7 digits): ")
    pin = int(input("Enter your PIN (4 digits): "))

    if acct_num in accounts.keys():
        if pin == accounts[acct_num]["PIN"]:
            print("login successful")
            display_menu()
        else:
            print("Login Unsuccessful. Incorrect PIN")
            main()
    else:
        print("No account found")
    
    cursor = connection.cursor()
    addData = ("""
    INSERT INTO student_table 
    VALUES (002, 'john doe', 15, 0, 'LBJECHS')
    """)

    cursor.execute(addData)

    connection.commit()

    testQuery = ("SELECT * FROM student_table")

    cursor.execute(testQuery)

    for item in cursor:
        print(item)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()