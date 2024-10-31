#Python to take list and return tuple contain sum even and odd

def sum_even_odd():
    numbers = []

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    even_sum = 0
    odd_sum = 0

    # Calculate sums of even and odd numbers
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return (even_sum, odd_sum)


result = sum_even_odd()
print(f"Output: {result}")