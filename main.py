import pi_file_utils

while True:
    print("1. Store file")
    print("2. Restore file")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        file_path = input("Enter file path: ")
        pi_file_utils.store_file(file_path)
    elif choice == "2":
        file_name = input("Enter file name: ")
        pi_file_utils.restore_file(file_name)
    elif choice == "3":
        break
    else:
        print("Invalid choice")