email = input("Enter Your Email: ")
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():          # ❌ was incorrect earlier
                        k = 1
                    elif i.isalpha():
                        if i.isupper():      # ❌ fixed logic
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Invalid Email ❌")
                else:
                    print("Valid Email ✅")
            else:
                print("Wrong email: dot position invalid ❌")
        else:
            print("Wrong email: invalid @ usage ❌")
    else:
        print("Wrong email: first character must be alphabet ❌")
else:
    print("Wrong email: too short ❌")
