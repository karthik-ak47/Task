def extract_name_from_email(email):

    username = email.split('@')[0]
    
    names = username.split('.')
    
    first_name = names[0].capitalize()
    last_name = names[-1].capitalize()
    
    return first_name, last_name

def create_user_id(first_name, last_name):
    user_id = first_name[0].lower() + last_name[:3].lower()
    return user_id

email = input("Enter your email address: ")

first_name, last_name = extract_name_from_email(email)

# Creating user ID
user_id = create_user_id(first_name, last_name)

# Displaying user ID
print("Your User ID:", user_id)