import re

# Define function for numeric value sum
def add(input_string):
    str_to_list = re.findall('-?[0-9]+', input_string)

    # Negative not allowed
    for i in str_to_list:
       if  i.startswith("-") and int(i) < 0:
        print(f"Negative not allowed {i}")
    
    # Numeric value sum
    num_list = []
    for i in str_to_list:
        if i.isnumeric():
            num_list.append(int(i))

    # Check null string
    if len(str_to_list) == 0:
        val = 0 
    else:
        val = sum(num_list)
    
    return val

input1 = input("Enter the input: ")
result = add(input1)
print("Sum of postive integer is {}".format(result))
