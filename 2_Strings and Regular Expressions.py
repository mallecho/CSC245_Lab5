import re

# Example input text
text = "Contact us at support@example.com or sales@example.org for assistance."

# Define the regular expression pattern for emails
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Use re.findall() to find all email addresses in the text
email_addresses = re.findall(email_pattern, text)

# Check if the list is empty and print appropriate message
if email_addresses:
    print(f"cssCopyEdit{email_addresses}")
else:
    print("No email addresses found in the given text.")
