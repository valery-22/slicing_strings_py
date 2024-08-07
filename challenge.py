# 🌟Star Wars Name Generator🌟

# Function to generate Star Wars name
def generate_star_wars_name():
    # Get all inputs in one line, separated by spaces
    user_input = input("Input your first name, last name, mother's maiden name, and the city where you were born, all separated by spaces > ")
    
    # Split the inputs into individual variables
    first_name, last_name, maiden_name, birth_city = user_input.split()
    
    # Generate the Star Wars first name
    star_wars_first = (first_name[:3] + last_name[:3]).title()
    
    # Generate the Star Wars last name
    star_wars_last = (maiden_name[:2] + birth_city[-3:]).title()
    
    # Print the Star Wars name
    print(f"Your Star Wars name is {star_wars_first} {star_wars_last}")

# Call the function
generate_star_wars_name()
