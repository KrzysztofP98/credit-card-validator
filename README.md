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

#### Example:

```bash
python validate_card.py
