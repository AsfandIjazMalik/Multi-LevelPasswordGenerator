import random
import string
from itertools import chain

letters = string.ascii_letters
numbers = string.digits
special_cahrs = string.punctuation

combine = list(chain(letters, numbers, special_cahrs))

password = '' 
pwd_type = ''
pwd_list = []

list_pwd_types = [
    '1️⃣  Numbers Only',
    '2️⃣  Letter Only',
    '3️⃣  Symbol Only',
    '4️⃣  Number & Letters',
    '5️⃣  Numbers & Symbol',
    '6️⃣  Letters & Symbol',
    '7️⃣  Number Letter and Symbols (Recomended)'
]

print('***************************************\n  🟢 WELCOME TO PASSWORD GENERATOR🟢 \n***************************************\n')


def game_instructions():
    print("""
    📌 **Instructions for Using the Password Generator** 📌

    1️⃣   **Numbers Only:**
       - Password will be generated using only numbers (0-9).
       - This is the least secure option as numbers are predictable and can be easily guessed.
       - It is highly recommended not to use this type for sensitive accounts.

    2️⃣   **Letters Only:**
       - Password will use only letters (both uppercase and lowercase).
       - This type is more secure than numbers, but it's still easier for hackers to guess as it lacks variety.
       - Avoid using only letters for strong security; combining them with other characters is better.

    3️⃣   **Symbols Only:**
       - Password will contain only special symbols (e.g., @, #, $, etc.).
       - While symbols are harder to guess, using only symbols can make the password difficult to remember and not mixed enough.
       - This password type can be more secure, but for better security, combining different character types is better.

    4️⃣   **Number & Letters:**
       - Password will combine numbers and letters.
       - Stronger than the previous options as it adds more complexity, but still lacks symbols for optimal security.
       - Consider this type for general use, but if you're looking for top-level security, add symbols too.

    5️⃣   **Numbers & Symbol:**
       - Password will use numbers and special symbols.
       - This is a better option than numbers and letters alone, as adding symbols increases the strength.
       - However, without letters, it's still somewhat weaker compared to using a full mix of all character types.

    6️⃣   **Letters & Symbols:**
       - Password will use letters and special symbols.
       - This is a good balance of complexity and security, but it still lacks numbers, which can make it weaker in some cases.
       - This option is better than a password containing only letters or only symbols, but it’s always better to include all three types.

    7️⃣   **Number, Letters, and Symbols (Recommended):**
       - Best option for creating a strong password. 
       - A combination of numbers, letters, and special symbols is the most secure option.
       - This type of password offers the highest level of protection against brute-force and dictionary attacks, ensuring your account remains safe.

    ➡️  **Security Tips**:
       - Always use a combination of letters, numbers, and symbols for stronger security.
       - Avoid using easily guessable information such as your name, birth date, or common patterns (like "123456").
       - Longer passwords are generally more secure. Aim for at least 12-16 characters.
       - If possible, use a password manager to store your passwords securely instead of reusing the same password across multiple sites.

    🔒  **Recommended Password Length**: 12-16 characters for maximum security.
    
    📚  **For More Tips on Creating Secure Passwords**:
       - Please refer to trusted security guidelines and resources online to learn more about password best practices.
       - Regularly update your passwords, especially for critical accounts (e.g., banking, email).
       - Use multi-factor authentication (MFA) whenever available to add an extra layer of security.

    """)

def taking_user_input():
    # Taking Length OF Password
    while True: 
        global pwd_chars_len
        pwd_chars_len = input('Enter Password Characters Length? 👉 (8-16): ')
        if pwd_chars_len.isdigit():
            pwd_chars_len = int(pwd_chars_len)
            if 8 <= pwd_chars_len <= 16:
                break
            else:
                print('🔴 IMPORTANT NOTE!! : Please Enter Number Length In Given Limit\n')
        else:
            print('🔴 Invalid Input!! Enter Number In Range of (8-16)\n')

    # Taking Type of Password
    while True: 
        global pwd_type
        print('\n*************************************************')
        print('Types Of Password\n')
        for type in list_pwd_types:
            print(f'{type}')
        print('*************************************************\n')
        pwd_type = input('Please Read All Types of Password From Above List &\nSelect one Type Do you want? (1-7): ')
        print('\n')
        if pwd_type.isdigit():
            pwd_type = int(pwd_type)
            if 1 <= pwd_type <= 7:
                break
            else:
                print('🔴 IMPORTANT NOTE!! Please Select Number In Given List\n')
        else:
            print('🔴 Invalid Input!! Enter Number In Range of 👉 (1-7)\n')

    # Display length and type

def generate_pwd():
    global password
    password = ''
    global pwd_list
    pwd_list.clear()
    
    if pwd_type == 1:
        for _ in range(1, pwd_chars_len+1):
            char = random.choice(numbers)
            password += char
            # Display length and type
        selected_type = list_pwd_types[pwd_type - 1]  # Get the full name from the list
        print(f'🔴 Your Password is Generated on Your Requirements\n\nLength is: {pwd_chars_len}\nAnd Type is: {selected_type}\n')
        print(f'🛑 Your Password is 👉 : {password}\n')
        print(f'🛑 Your selected Password Type is weak because it contains only numbers, making it easy to guess and break.\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n') 
    
    elif pwd_type == 2:
        for _ in range(1, pwd_chars_len+1):
            char = random.choice(letters)
            password += char
            # Display length and type
        selected_type = list_pwd_types[pwd_type - 1]  # Get the full name from the list
        print(f'🔴 Your Password is Generated on Your Requirements\n\nLength is: {pwd_chars_len}\nAnd Type is: {selected_type}\n')
        print(f'🛑 Your Password is 👉 : {password}\n')
        print(f'🛑 Your selected password type is weak because Only letters predictable and not secure.\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n')

    elif pwd_type == 3:
        for _ in range(1, pwd_chars_len+1):
            char = random.choice(special_cahrs)
            password += char
            # Display length and type
        selected_type = list_pwd_types[pwd_type - 1]  # Get the full name from the list
        print(f'🔴 Your Password is Generated on Your Requirements\n\nLength is: {pwd_chars_len}\nAnd Type is: {selected_type}\n')
        print(f'🛑 Your Password is 👉 : {password}\n')
        print(f'🛑 Your selected password type is weak because Just symbols; hard to remember and not mixed enough.\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n')

    elif pwd_type == 4:

        print('*********************************************************\n🌟 NOTE 🌟\nEnter the number of digits you desire for your password.\n'
            'The remaining characters will be filled with letters.\n'
            'For example, if you choose 4 digits for a 9-character password\n'
            'The remaining 5 characters will be letters. Please choose accordingly.\n'
            '***********************************************************\n')
        while True:   
            num = input(f'How Many Numbers Do you want in your Password of Length {pwd_chars_len}? (1-{pwd_chars_len - 1}) : ')
            print('\n')
            if num.isdigit():  # Check if input is numeric
                num = int(num)  # Convert to integer after validation
                if 1 <= num <= pwd_chars_len - 1:
                    for _ in range(1, num + 1):
                        char = random.choice(numbers)
                        pwd_list += char
                    break  # Exit loop after valid input
                else:
                    print(f'🔴 IMPORTANT NOTE!! Please Enter Number In Range of 👉 (1-{pwd_chars_len - 1})\n')
            else:
                print(f'🔴 INVALID INPUT!! You Must Enter A Number 👉 (1-{pwd_chars_len - 1})\n')

        for_ltr = pwd_chars_len - num  # No need for int() here, num is already an integer

        for _ in range(1, for_ltr + 1):
            char = random.choice(letters)
            pwd_list += char

        random.shuffle(pwd_list)

        for char in pwd_list:
            password += char

        selected_type = list_pwd_types[pwd_type - 1]
        print(f'🟡  Your Password is Generated on Your Requirements\n\nLength is : {pwd_chars_len}\nAnd Type is : {selected_type}\n')
        print(f'🟡  Your Password is 👉 : {password}\n')
        print(f'⚠️  Your selected password type is Satisfactory Because Includes numbers and letters, but no symbols, so less secure.\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n')

    elif pwd_type == 5:
        print('*************************************************\n🌟 NOTE 🌟\nEnter the number of digits you desire for your password.\n'
              'The remaining characters will be filled with special symbols ( (@#$%^&**()_+) ).\n'
              'For example, if you choose 4 number for a 9-character password\n'
              'The remaining 5 characters will be special symbols. Please choose accordingly.\n'
              '*************************************************\n')
        while True:   
            num = input(f'How Many Numbers Do you want in your Password of Length {pwd_chars_len}? (1-{pwd_chars_len - 1}) : ')
            print('\n')
            if num.isdigit():
                num = int(num)
                if 1 <= num <= pwd_chars_len - 1:
                    for _ in range (1, num+1):
                        char = random.choice(numbers)
                        pwd_list += char
                    break
                else:
                    print(f'🔴 IMPORTANT NOTE!! Please Enter Number In Range of 👉 (1-{pwd_chars_len - 1})\n')
            else:
                print(f'🔴 INVALID INPUT!! You Must Enter A Number 👉 (1-{pwd_chars_len - 1})\n')
                
        for_ltr = pwd_chars_len - num
            
        for _ in range (1, for_ltr+1):
            char = random.choice(special_cahrs)
            pwd_list += char
                
        random.shuffle(pwd_list)
            
        for char in pwd_list:
            password += char
        selected_type = list_pwd_types[pwd_type - 1] 
        print(f'🟡  Your Password is Generated on Your Requirements\n\nLength is : {pwd_chars_len}\nAnd Type is : {selected_type}\n')
        print(f'🟡  Your Password is 👉 : {password}\n')
        print(f'⚠️  Your selected password type is Good because Numbers and symbols make it good, But Not Stronger\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n')
         

    elif pwd_type == 6:
        print('*************************************************\n🌟 NOTE 🌟\nEnter the number of Letters you desire for your password.\n'
              'The remaining characters will be filled with special symbols ( (@#$%^&**()_+) ).\n'
              'For example, if you choose 4 Letter for a 9-character password\n'
              'The remaining 5 characters will be special symbols. Please choose accordingly.\n'
              '*************************************************\n')
        while True:   
            num = input(f'How Many Letters Do you want in your Password of Length {pwd_chars_len}? (1-{pwd_chars_len - 1}) : ')
            print('\n')
            if num.isdigit():
                num = int(num)
                if 1 <= num <= pwd_chars_len - 1:
                    for _ in range (1, num+1):
                        char = random.choice(letters)
                        pwd_list += char
                    break
                else:
                    print(f'🔴 IMPORTANT NOTE!! Please Enter Number In Range of 👉 (1-{pwd_chars_len - 1})\n')
            else:
                print(f'🔴 INVALID INPUT!! You Must Enter A Number 👉 (1-{pwd_chars_len - 1})\n')
                
        for_ltr = int(pwd_chars_len) - int(num)
            
        for _ in range (1, for_ltr+1):
            char = random.choice(special_cahrs)
            pwd_list += char
                
        random.shuffle(pwd_list)
            
        for char in pwd_list:
            password += char
        selected_type = list_pwd_types[pwd_type - 1] 
        print(f'🟡  Your Password is Generated on Your Requirements\n\nLength is : {pwd_chars_len}\nAnd Type is : {selected_type}\n')
        print(f'🟡  Your Password is 👉 : {password}\n')
        print(f'⚠️  Your selected password type is Good because letter and symbols make it good, But Not Stronger\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n')
            
    elif pwd_type == 7:
        print('*************************************************\n🌟 NOTE 🌟\nEnter the number of Letters and Numbers you desire for your password.\n'
            'The remaining characters will be filled with special symbols ( (@#$%^&**()_+) ).\n'
            'For example, if you choose 4 Letter and 2 Numbers for a 9-character password\n'
            'The remaining 3 characters will be special symbols. Please choose accordingly.\n'
            '*************************************************\n')

        while True:   
            ltr = input(f'How Many Letters Do you want in your Password of Length {pwd_chars_len}? (1-{pwd_chars_len - 2}) : ')
            if ltr.isdigit():
                ltr = int(ltr)
                if 1 <= ltr <= pwd_chars_len - 2:  # Ensure room for at least 1 number and 1 symbol
                    for _ in range(1, ltr + 1):
                        char = random.choice(letters)
                        pwd_list += char
                    break
                else:
                    print(f'🔴 IMPORTANT NOTE!! Please Enter Number In Range of 👉 (1-{pwd_chars_len - 2})\n')
            else:
                print(f'🔴 INVALID INPUT!! You Must Enter A Number 👉 (1-{pwd_chars_len - 2})\n')

        remaining_len = pwd_chars_len - ltr

        while True:
            num = input(f'How Many Numbers Do you want in your Password of Remaining Length {remaining_len}? (1-{remaining_len - 1}) : ')
            if num.isdigit():
                num = int(num)
                if 1 <= num <= remaining_len - 1:  # Ensure room for at least 1 symbol
                    for _ in range(1, num + 1):
                        char = random.choice(numbers)
                        pwd_list += char
                    break
                else:
                    print(f'🔴 IMPORTANT NOTE!! Please Enter Number In Range of 👉 (1-{remaining_len - 1})\n')
            else:
                print(f'🔴 INVALID INPUT!! You Must Enter A Number 👉 (1-{remaining_len - 1})\n')

        # Remaining characters will be symbols
        for_sym = pwd_chars_len - (ltr + num)
        for _ in range(1, for_sym + 1):
            char = random.choice(special_cahrs)
            pwd_list += char

        random.shuffle(pwd_list)

        for char in pwd_list:
            password += char

        selected_type = list_pwd_types[pwd_type - 1]
        print(f'🟢  Your Password is Generated on Your Requirements\n\nLength is : {pwd_chars_len}\nAnd Type is : {selected_type}\n')
        print(f'🟢  Your Password is 👉 : {password}\n')
        print(f'✅ Your selected password type is Strong 💯 because Has all types (numbers, letters, symbols); very hard to crack. Recommended!\n📕 If you want to read all password instructions, please visit the instruction section of the app.\n')

# Main Menu          
while True:
    task = input('1️⃣  Enter G or 1 To Generate Password (G or 1):\n'
                 '2️⃣  Enter I or 2 To Read Instructions (I or 2):\n'
                 '3️⃣  Enter E or 3 To Exit (E or 3):\n'
                 '\nEnter (G/I/E) or (1/2/3) 👉 : ').lower()

    if task in ['g', '1']:
        taking_user_input()
        generate_pwd()
    elif task in ['i', '2']:
        game_instructions()
    elif task in ['e', '3']:
        print('❌ You Exit The App See You 🔜\nTHANK YOU!!! 😊')
        break
    else:
        print('🔴 Invalid Input! Please Select (G/I/E) or (1/2/3)\n')