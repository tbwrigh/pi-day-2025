import os
from sympy import N, pi

def store_file(file_path):
    file_name = "pi_storage_" + os.path.basename(file_path)

    pi_str = str(N(pi, 100))
    pi_str = pi_str.replace(".", "")

    os.makedirs("stored", exist_ok=True)

    os.makedirs(os.path.join("stored", file_name), exist_ok=True)

    with open(file_path, 'rb') as input_file:
        out_files = [open(os.path.join("stored", file_name, f'{i}'), 'wb') for i in range(10)]
        digit = 0
        while True:
            if digit == len(pi_str):
                pi_str = str(N(pi, 2*len(pi_str)))
                pi_str = pi_str.replace(".", "")
            
            data = input_file.read(int(pi_str[digit]) % 10 + 1)
            if not data:
                break
            out_files[int(pi_str[digit]) % 10].write(data)
            digit += 1
    
    print("File stored with n = ", digit)

def restore_file(file_name):
    stored_file_name = "pi_storage_" + file_name
    os.makedirs("restored", exist_ok=True)
    with open(os.path.join("restored", file_name), 'wb') as output_file:
        in_files = [open(os.path.join("stored", stored_file_name, f'{i}'), 'rb') for i in range(10)]
        digit = 0
        pi_str = str(N(pi, 100))
        pi_str = pi_str.replace(".", "")
        while True:
            if digit == len(pi_str):
                pi_str = str(N(pi, 2*len(pi_str)))
                pi_str = pi_str.replace(".", "")
            try:
                data = in_files[int(pi_str[digit]) % 10].read(int(pi_str[digit]) % 10 + 1)
            except:
                print("something went wrong")
                break
            if not data:
                break
            output_file.write(data)
            digit += 1

    print("File restored with n = ", digit)
