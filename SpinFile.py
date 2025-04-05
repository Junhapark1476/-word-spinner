# Assignment: A4 Word Spinner
# Names: junha Park
# github: https://github.com/Junhapark1476/-

import string
from Spinner import Spinner

# Function to clean text: lowercase conversion and punctuation removal
def clean_text(text):
    print("Cleaning text...")  # Debug message
    text = text.lower()  # Convert to lowercase
    for ch in string.punctuation:
        text = text.replace(ch, '')  # Remove punctuation
    return text

# Main function to read input, process it, and generate variations
def main():
    print("Reading essay.txt...")  # Debug message
    with open('essay.txt', 'r') as file:
        original = file.read()  # Read original essay content

    # Clean the text (lowercase + remove punctuation)
    cleaned = clean_text(original)

    print("Loading synonym file and initializing spinner...")  # Debug message
    spinner = Spinner('test-synonyms.txt')  # Create Spinner object with synonym file

    print("Generating outputs...")  # Debug message
    with open("results.txt", "w") as output:
        # Write the original cleaned text
        output.write("Original:\n")
        output.write(cleaned + "\n\n")

        # Generate and write three spun versions
        for i in range(1, 4):
            spun = spinner.spin(cleaned)  # Create a randomized version of the text
            output.write(f"Option {i}:\n")
            output.write(spun + "\n\n")
            print(f"Option {i} generated.")  # Debug message

    print("All done. Results saved to results.txt.")  # Final confirmation

if __name__ == "__main__":
    main()


