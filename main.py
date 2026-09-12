from read import read_file
from write import write_file
from operation import buy, sell

def display_product(file_data):
    print("\n================ PRODUCT LIST ================\n")
    print("ID\tName\t\tBrand\t\tStock\tPrice\t\tOrigin")
    print("-" * 90)
    for i in file_data:
        print(f"{i[0]}\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t{i[4]}\t\t{i[5]}")
    print("-" * 90)


def main():
    print("SpeedWearz \nInventory management system")
    print("---------------------------------")
    print("Choose an option:")
    print("1. Buy")
    print("2. Sell")
    print("3. Quit Program")
    while True:
        user_choice = input(": ")
        try:
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > 3:
                print("The number has to be between 1 and 3.")
                continue
        except ValueError:
            print("The input has to be a number.")
            continue

        if user_choice == 1:
            print("---------------------------------")
            inventory = read_file('Information.txt')
            display_product(inventory)
            buy(inventory, 'Information.txt')
            print("---------------------------------")
        elif user_choice == 2:
            print("---------------------------------")
            inventory = read_file('Information.txt')
            display_product(inventory)
            sell(inventory, "Information.txt")
            print("---------------------------------")
        elif user_choice == 3:
            exit()


main()