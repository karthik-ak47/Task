email_list = []

for i in range(5):
    email = input(f"Enter your email address {i+1}: ")
    email_list.append(email)

# Display the collected email addresses
print("Collected email addresses:")
for email in email_list:
    print(email)