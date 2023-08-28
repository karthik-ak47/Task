def extract_name_from_email(email):
    username = email.split('@')[0]
    names = username.split('.')
    first_name = names[0].capitalize()
    last_name = names[-1].capitalize()
    return first_name, last_name

def create_user_id(first_name, last_name):
    user_id = first_name[0].lower() + last_name[:3].lower()
    return user_id

# Initialize an empty list to store user records
user_records = []

# Collect information for multiple users
for i in range(5):
    email = input(f"Enter email address for user {i+1}: ")
    first_name, last_name = extract_name_from_email(email)
    user_id = create_user_id(first_name, last_name)
    
    # Create a dictionary for the user record
    user_dict = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'user_id': user_id
    }
    
    # Append the user dictionary to the user_records list
    user_records.append(user_dict)

# Display the details of each user using string formatting
for user in user_records:
    print("User Details:")
    print("Email: {}".format(user['email']))
    print("First Name: {}".format(user['first_name']))
    print("Last Name: {}".format(user['last_name']))
    print("User ID: {}".format(user['user_id']))
    print()  # Print an empty line to separate user details
