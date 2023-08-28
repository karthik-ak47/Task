def extract_name_from_email(email):
    # Splitting the email address by '@' to get the username part
    username = email.split('@')[0]
    
    # Splitting the username by '.' to get the first name and last name
    names = username.split('.')
    
    # Extracting the first name and last name
    first_name = names[0].capitalize()
    last_name = names[-1].capitalize()
    
    return first_name, last_name

# Taking email input from the user
email = input("Enter your email address: ")

# Extracting the first name and last name from the email
first_name, last_name = extract_name_from_email(email)

# Displaying the extracted names
print("First Name:", first_name)
print("Last Name:", last_name)