#Write a Python function to insert a string in the middle of a string.
def insert_string(str,word):
    return str[:3 ]+word+str[ 3:]
print(insert_string("how you?","are"))
