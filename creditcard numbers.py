#define the function using Luhn's algorithm
def validate_number(number):
    # Check if the number length is between 13 and 16 digits and positive
    while 13 <= len(str(number)) <= 16 and number > 0:

        # Get the last digit of the number (check digit)
        check_digit = number % 10

        # Remove the last digit from the number
        number //= 10

        # Convert the remaining number to a list of digits and reverse the list
        card_number = list(str(number))
        card_number.reverse()

        # Initialize an empty list to store processed digits
        processed_digits = []

        # Loop through each digit and its index
        for index, digit in enumerate(card_number):
            # Double every second digit starting from the right (now reversed, so index 0, 2, 4,...)
            if index % 2 == 0:
                even_digit = int(digit) * 2

                # If doubling a digit results in a number greater than 9, subtract 9
                if len(str(even_digit)) > 1:
                    even_digit = even_digit - 9

                # Append the processed even digit to the list
                processed_digits.append(even_digit)

            else:
                # For other digits, append them directly to the list
                processed_digits.append(int(digit))

        # Calculate the total sum of processed digits and the check digit
        total = int(check_digit) + sum(processed_digits)

        # Reverse the card number back to its original order for validation
        card_number.reverse()

        # Print the card number being validated (excluding the check digit)
        print("\nThe card number", number, "is")

        # Determine the card type based on the first digits and check if the total is divisible by 10
        if (total % 10 == 0 and card_number[0] == '4'):
            return "valid (Visa)"  # Visa cards start with 4

        elif total % 10 == 0 and card_number[0] == '5':
            return "valid (Mastercard)"  # Mastercard cards start with 5

        elif total % 10 == 0 and card_number[0] == '3' and card_number[1] == '7':
            return "valid (American Express)"  # Amex cards start with 37

        elif total % 10 == 0 and card_number[0] == '6':
            return "valid (Discover)"  # Discover cards start with 6

        else:
            # If the total isn't divisible by 10 or it doesn't match a known card type, it's invalid
            return "invalid"


# This block runs the code only if the script is executed directly.
# It tests the validate_number function with sample credit card numbers.
if __name__ == '__main__':
    validate = validate_number(4388576018410707)
    print(validate)

    validate1 = validate_number(4388576018402626)
    print(validate1)
