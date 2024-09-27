# Terminal-based Registration Form

def registration_form():
    print("Welcome to the Registration Form")
    
    # Collect user information
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone Number: ")
    password = input("Enter your Password: ")
    
    # Display the information
    print("\n--- Registered Information ---")
    print(f"Name: {first_name} {last_name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    
    # Return or store information in a file or database
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'password': password
    }
    
    print("\nThank you for registering!")

# Call the function
registration_form()
