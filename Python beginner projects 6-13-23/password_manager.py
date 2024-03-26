from cryptography.fernet import Fernet
import os
import base64

master_pwd = input(
    'What is the master password: ')

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists('key.key'):
        write_key()
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

key = load_key()
try:
    fer = Fernet(key)
except ValueError as e:
    # print("Invalid key:", str(e))
    print("Regenerating a new key...")
    write_key()
    key = load_key()
    fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            split_data = data.split('|')
            if len(split_data) == 2:
                user, password = split_data
                print('User:', user, ', Password:', 
                      fer.encrypt(password.encode()).decode())
            else:
                print('Invalid data:', data)


def create():
    name=input('Account name: ')
    pwd=input('Enter your password: ')

    with open('password.txt',  'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +  '\n')




while True:
    mode = input(
        'Would you like to view an existing password or add a new password? (view/create) Press q to quit: ').lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'create':
        create()
    # else:
    #     print('Invalid mode.')
    #     continue