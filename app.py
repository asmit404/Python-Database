# Importing Libraries
from prettytable import PrettyTable

# Initialising Variables
student_data = {}

# Function to Add Data
def add_student_data():
    print()
    number_of_entries = int(input("Enter the number of entries to be inserted: "))
    for _ in range(number_of_entries):
        student_name = input("Enter the name of the student: ")
        while not student_name:
            print("Enter a valid name--->")
            student_name = input("Enter the name of the student: ")

        student_phone_number = input("Enter the mobile number of the student: ")
        while len(student_phone_number) < 10:
            print("Enter a valid number--->")
            student_phone_number = input("Enter the mobile number of the student: ")

        student_email_address = input("Enter the email address of the student: ")
        while "@" not in student_email_address:
            print("Enter a valid email address---> ")
            student_email_address = input("Enter the email address of the student: ")

        student_data[student_name] = {"Phone Number": student_phone_number, "Email Address": student_email_address}
    main()

# Function to Display Data
def display_student_data():
    pretty_table = PrettyTable()
    print()
    print("Displaying all entries in the repository: ")
    pretty_table.field_names = ["Name", "Phone Number", "E-mail Address"]
    for name, data in student_data.items():
        pretty_table.add_row([name, data["Phone Number"], data["Email Address"]])
    print(pretty_table)
    main()

# Function to Search Entries
def search_student_data():
    print()
    print("Search Using: ")
    print("1. Name ")
    print("2. Phone Number ")
    print("3. Email Address ")

    choice = input("Enter your choice: ")
    if choice == "1":
        student_name = input("Enter the name of the student ---> ")
        data = student_data.get(student_name, {})
        print(f"The linked phone number is: {data.get('Phone Number', 'Entry not found.')}") 
        print(f"The linked email address is: {data.get('Email Address', 'Entry not found.')}") 
    elif choice == "2":
        student_phone_number = input("Enter the phone number of the student ---> ")
        for name, data in student_data.items():
            if data["Phone Number"] == student_phone_number:
                print(f"The linked name is: {name}")
                print(f"The linked email address is: {data['Email Address']}")
                break
        else:
            print("Entry not found.")
    elif choice == "3":
        student_email_address = input("Enter the email address of the student ---> ")
        for name, data in student_data.items():
            if data["Email Address"] == student_email_address:
                print(f"The linked name is: {name}")
                print(f"The linked phone number is: {data['Phone Number']}")
                break
        else:
            print("Entry not found.")
    else:
        print("Enter a valid number as choice: ")
        search_student_data()
    main()

# Main Function
def main():
    print()
    print("What do you want to do:")
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Exit")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        add_student_data()
    elif user_choice == "2":
        display_student_data()
    elif user_choice == "3":
        search_student_data()
    elif user_choice == "4":
        exit()
    else:
        print("Enter a valid number as choice:")
        main()

if __name__ == "__main__":
    main()

# Can you believe that I got full marks for this piece of shit?