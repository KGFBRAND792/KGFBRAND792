def login():
    correct_username = "RADHEY"
    correct_password = "T.S.BRAND"
    username = input("correct_username")
    password = input("correct_password")
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect username or password. Please try again.")
login()
