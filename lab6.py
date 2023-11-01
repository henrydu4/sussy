
def method8(data):
    index = data.find(":")
    print(data[0:index])
    data = data[index + 1:]
    print(data)

def encoder(password):
    for i in password:
        i = int(i) + 3
        nPass += str(i)

def decoder(password):
    nPass = ""
    for i in password:
        i = int(i) - 3
        nPass += str(i)
    return nPass



def main():
      menu = 
    """Menu
    -------------
    1. Encode
    2. Decode
    3. Quit"""

    while True:
        print(menu)
        menu_option = int(input('Please enter an option: '))

        if menu_option == '1':
            userPass = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')

        elif menu_option == '2':
            print(f'decoded password: {decoder(UserPass)}')

        elif menu_option == '3':
            break


if __name__ == '__main__':
    main()
