# python-credit-card
# Credit Card Validator

This is a Python script that validates credit card numbers using **Luhn's Algorithm**, a common checksum formula used to validate card numbers. The script also determines the card type (Visa, Mastercard, American Express, or Discover) based on the first few digits of the card number.

## Features
- Validates credit card numbers using **Luhn's Algorithm**.
- Supports multiple card types:
  - Visa (starts with 4)
  - Mastercard (starts with 5)
  - American Express (starts with 37)
  - Discover (starts with 6)
- Detects valid and invalid card numbers.

## How it Works
The validation process involves:
1. Checking if the card number is between 13 and 16 digits long.
2. Using **Luhn's Algorithm** to process the digits:
   - Doubling every second digit from the right.
   - Subtracting 9 from any doubled digit that results in a value greater than 9.
3. Adding the processed digits together, along with the check digit (the last digit of the card number).
4. Checking if the total sum is divisible by 10. If so, the card is valid.
5. Identifying the card type by checking the first digits.

## Usage

### Prerequisites
- Python 3.x installed on your machine.

### Running the Script
1. Clone or download the script to your local machine.
2. Open a terminal/command prompt and navigate to the directory containing the script.
3. Run the script by providing a credit card number as input.

### Output

    For valid cards, it will return:
        "valid (Visa)", "valid (Mastercard)", "valid (American Express)", or "valid (Discover)" depending on the card type.
    For invalid cards, it will return:
        "invalid"

### Code Breakdown

    validate_number(number): This function accepts a credit card number as input, processes it using Luhn's Algorithm, and returns whether the card is valid and what type it is.
    if __name__ == '__main__':: This block allows you to test the script by running it directly. Two sample card numbers are tested: one valid and one invalid.

### Example Credit Card Numbers for Testing

Here are a few card numbers to test the script with:

Card Type	Card Number	Validity
Visa	4388576018410707	Valid
Mastercard	5500000000000004	Valid
American Express	371449635398431	Valid
Discover	6011111111111117	Valid
Invalid Number	4388576018402626	Invalid

### Contributions
Krzysztof Piotrowski

### Licence 
This project under the MIT licence. See the LICENCE for details. 

### Contact 
For any questions or issues, please contact krzysztof.piotrowski.in@gmail.com

