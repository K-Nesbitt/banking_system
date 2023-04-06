global accounts 

accounts={'1234567':{"name": "Keatra N",
                             "PIN": 1214, 
                             "type": "savings"}}

def main():
    print("Welcome to Nesbitt Bank Online (NBO)")

    acct_num = input("Enter your account number (7 digits): ")
    pin = int(input("Enter your PIN (4 digits): "))

    if acct_num in accounts.keys():
        if pin == accounts[acct_num]["PIN"]:
            print("login successful")
        else:
            print("Login Unsuccessful. Incorrect PIN")
    else:
        print("No account found")

if __name__ == '__main__':
    main()