import random
import string


def random_password_generator():
    alphabet = list(string.ascii_letters)
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*'] 
    how_long_password = int(input("How Long Do you Want Your Password To Be? "))
    password = []    
    passwd = ""
    for _ in range(0,how_long_password):
        random_num_alphabet = random.randint(0,50)
        random_num_special_char = random.randint(0,7)
        rn = random.randint(0,9)
        ra = alphabet[random_num_alphabet]
        rsc = special_char[random_num_special_char]
        rc = random.choice([rn,ra,rsc])
        password.append(rc)
    
    for i in password:
        passwd += str(i)

    return passwd
    
print(random_password_generator())
