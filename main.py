import mysql.connector

def account_exists(connection, acct_num):
    cursor = connection.cursor()

    Query=("""
    SELECT acct_num 
    FROM accounts 
    """)

    cursor.execute(Query)
    rows = cursor.fetchall()
    for row in rows:
            if row[0]==acct_num:
                cursor.close()
                return True
    cursor.close()
    return False

def acct_details(connection, acct_info):
    cursor = connection.cursor()
    query = (""" SELECT * FROM accounts WHERE acct_num= %s""")
    cursor.execute(query, (acct_info[0],))
    row = cursor.fetchone()
    if row == None:
        print("Account doesn't exist")
        cursor.close()
        return None

    else:
        print(f"Account details: ")
        cursor.close()
        return row

def login(connection):
    cursor = connection.cursor()
    acct_num = int(input("Enter your account number (7 digits): "))
    pin = int(input("Enter your PIN (4 digits): "))
    acct_info = (acct_num, pin)

    login_Query=("""
    SELECT acct_num , pin 
    FROM accounts 
    WHERE acct_num=%s AND pin=%s
    """)
    cursor.execute(login_Query, acct_info)
    row = cursor.fetchone()
    if row == None:
        print("Login Unsuccessful")
        cursor.close()
        return None

    else:
        print("Login Successful")
        cursor.close()
        return acct_info


def create_account(connection):
    cursor = connection.cursor()
    acct_num = int(input("Enter your account number (7 digits): "))
    name = str(input("Enter the name for the account: "))
    pin = int(input("Enter your PIN (4 digits): "))
    acct_type = str(input("Enter the type of account (checking or savings): "))
    address = str(input("Enter your address including city, state, and zip code: "))
    balance = float(input("Enter your starting account balance: "))

    vars = (acct_num, name, pin, acct_type, address, balance)
    Query = ("""INSERT INTO accounts
    VALUES (%s, %s, %s, %s, %s, %s)
    
    """)
    cursor.execute(Query, vars)
    connection.commit()

    if account_exists(connection, acct_num):
        print("Account successfully created")
    else:
        print("Account not created")

    cursor.close()
    return None

def get_balance(connection, acct_info):
    cursor = connection.cursor()
    balance_Query=("""
        SELECT acct_balance
        FROM accounts
        WHERE acct_num=%s AND pin=%s
        """)
    cursor.execute(balance_Query, acct_info)
    row = cursor.fetchone()
    if row == None:
        cursor.close()
        return 0
    else:
        cursor.close()
        return row[0]        
    
def withdrawal(connection, acct_info):
    cursor = connection.cursor()
    money = int(input("Enter the amount to withdrawal: "))
    current_balance = get_balance(connection, acct_info)
    if money <= current_balance:
        new_balance = current_balance - money
        query = ("""UPDATE accounts
        SET acct_balance = %s
        WHERE acct_num= %s
        """)
        cursor.execute(query, (new_balance, acct_info[0]))
        connection.commit()
    else:
        print("Insufficient Funds")
   
    print(f"Current Balance: ${get_balance(connection, acct_info)}") 
    cursor.close()
    return None


def deposit(connection, acct_info):
    cursor = connection.cursor()
    money = int(input("Enter the amount to deposit: "))
    current_balance = get_balance(connection, acct_info)
    new_balance = current_balance + money

    query = ("""UPDATE accounts
    SET acct_balance = %s
    WHERE acct_num= %s
    """)
    cursor.execute(query, (new_balance, acct_info[0]))
    connection.commit()
    
    print(f"Current Balance: ${get_balance(connection, acct_info)}") 
    cursor.close()
    return None

def delete_account(connection, acct_info):
    cursor = connection.cursor()

    Query = ("""DELETE FROM accounts 
    WHERE acct_num=%s
    """)
    cursor.execute(Query, (acct_info[0],))
    connection.commit()

    if not account_exists(connection, acct_info[0]):
        print("Account successfully deleted")
    else:
        print("Account not deleted")

    cursor.close()
    return None
    

def edit_account(connection, acct_info):
    cursor = connection.cursor()
    column = str(input("Enter the data you want to edit (name, PIN, acct_type, or address): "))
    value = str(input("Enter the new value: "))
    
    if column == 'name':
        Query = (""" UPDATE accounts
        SET name = %s
        WHERE acct_num = %s
        """)
        cursor.execute(Query, (column, value, acct_info[0]))
        connection.commit()
        acct_details(connection, acct_info)
        cursor.close()
        return None

    elif column == 'PIN':
        value = int(value)
        Query = (""" UPDATE accounts
        SET PIN = %s
        WHERE acct_num = %s
        """)
        cursor.execute(Query, (value, acct_info[0]))
        connection.commit()
        acct_details(connection, acct_info)
        cursor.close()
        return None
    
    elif column == 'acct_type':
        Query = (""" UPDATE accounts
        SET acct_type = %s
        WHERE acct_num = %s
        """)
        cursor.execute(Query, (value, acct_info[0]))
        connection.commit()
        acct_details(connection, acct_info)
        cursor.close()
        return None
    
    elif column == 'address':
        Query = (""" UPDATE accounts
        SET address = %s
        WHERE acct_num = %s
        """)
        cursor.execute(Query, (value, acct_info[0]))
        connection.commit()
        acct_details(connection, acct_info)
        cursor.close()
        return None
    
    else:
        print("Invalid option")
        return None

    

def display_menu():
    print("\n **Menu**")
    print("1. Create Account")
    print("2. Check Balance ")
    print("3. Withdrawal")
    print("4. Deposit")
    print("5. Delete Account")
    print("6. Edit Account")
    print("7. Exit\n")

def user_selection(connection):
    display_menu()
    try:
      user_choice = int(input("Enter a number between 1-7: "))
    except ValueError:
      print("\nSorry, Not a Valid Choice. Please try again! \n")
      user_selection(connection)
    
    if user_choice == 1:  #Add new row.
        create_account(connection)
        user_selection(connection)

    elif user_choice == 2:  #Return Account Balance
        acct_info = login(connection)
        if acct_info:
            b = get_balance(connection, acct_info)
            print(f"Current Account Balance: ${b}")
            user_selection(connection)
        else:
            user_selection(connection)

    elif user_choice == 3:  #decrease account balance
        acct_info = login(connection)
        if acct_info:
            withdrawal(connection, acct_info)
            user_selection(connection)
        else:
            user_selection(connection)

    elif user_choice == 4:  #increase account balance
        acct_info = login(connection)
        if acct_info:
            deposit(connection, acct_info)
            user_selection(connection)
        else:
            user_selection(connection)
        
    elif user_choice == 5:  #remove row
        acct_info = login(connection)
        if acct_info:
            delete_account(connection, acct_info)
            user_selection(connection)
        else:
            user_selection(connection)
    
    elif user_choice == 6:  #edit row
        acct_info = login(connection)
        if acct_info:
            edit_account(connection, acct_info)
            user_selection(connection)
        else:
            user_selection(connection)

    elif user_choice == 7:  #exit
        print("Logout Successful. Bye!")
    
    else:
        print("\nSorry, Not a Valid Choice. Please try again! \n")
        user_selection(connection)

def main():
    print("Welcome to Nesbitt Bank Online (NBO)")
    
    connection = mysql.connector.connect(host = 'localhost',
                                        database = 'example',
                                        user = 'root',
                                        password = 'Y+kTRisJ')
    
    user_selection(connection=connection)
    
    connection.close()

if __name__ == '__main__':
    main()



