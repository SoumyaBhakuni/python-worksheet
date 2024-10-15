# Python Program: Combined String Manipulation Utilities

def extract_odd_indices(string):
    """
    Extracts characters at odd indices from the given string.
    
    Parameters:
        string (str): The input string.
        
    Returns:
        str: A new string containing characters from odd indices.
    """
    return string[1::2]

def reverse_string(string):
    """
    Reverses the given string.
    
    Parameters:
        string (str): The input string.
        
    Returns:
        str: The reversed string.
    """
    return string[::-1]

def reverse_alternate_words(sentence):
    """
    Reverses every alternate word in the sentence while keeping other words in their original order.
    
    Parameters:
        sentence (str): The input sentence.
        
    Returns:
        str: The sentence with every alternate word reversed.
    """
    words = sentence.split()
    for i in range(1, len(words), 2):
        words[i] = words[i][::-1]
    return ' '.join(words)

def every_second_character(string):
    """
    Returns every second character from the string, starting from the first character.
    
    Parameters:
        string (str): The input string.
        
    Returns:
        str: A string containing every second character.
    """
    return string[::2]

def extract_reverse(string, start_index, end_index):
    """
    Extracts characters between two indices in the string and returns them in reverse order.
    
    Parameters:
        string (str): The input string.
        start_index (int): The starting index.
        end_index (int): The ending index.
        
    Returns:
        str: The extracted substring in reverse order.
    """
    return string[start_index:end_index][::-1]

def display_menu():
    """
    Displays the menu of available string manipulation options.
    """
    print("\n--- String Manipulation Utilities ---")
    print("1. Extract characters at odd indices")
    print("2. Reverse a string")
    print("3. Reverse every alternate word in a sentence")
    print("4. Return every second character")
    print("5. Extract and reverse characters between two indices")
    print("6. Exit")

def main():
    """
    Main function to run the menu-driven string manipulation program.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            string = input("Enter the string: ")
            result = extract_odd_indices(string)
            print(f"Characters at odd indices: {result}")
        
        elif choice == '2':
            string = input("Enter the string to reverse: ")
            result = reverse_string(string)
            print(f"Reversed string: {result}")
        
        elif choice == '3':
            sentence = input("Enter the sentence: ")
            result = reverse_alternate_words(sentence)
            print(f"Modified sentence: {result}")
        
        elif choice == '4':
            string = input("Enter the string: ")
            result = every_second_character(string)
            print(f"Every second character: {result}")
        
        elif choice == '5':
            string = input("Enter the string: ")
            try:
                start_index = int(input("Enter the start index: "))
                end_index = int(input("Enter the end index: "))
                if start_index < 0 or end_index > len(string) or start_index > end_index:
                    print("Invalid indices. Please try again.")
                    continue
                result = extract_reverse(string, start_index, end_index)
                print(f"Extracted and reversed substring: {result}")
            except ValueError:
                print("Indices must be integers. Please try again.")
        
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
