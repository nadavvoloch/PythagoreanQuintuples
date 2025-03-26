import random
import csv

def return_quad_lst(x):
    a = x
    if a % 2 == 1:
        # Case 1: a is odd
        b = (a ** 2 - 1) / 2
        c = (a ** 4) / 8 + (a ** 2) / 4 - 3 / 8
        d = ((a ** 8) + 4 * (a ** 6) + 14 * (a ** 4) + 20 * (a ** 2) - 39) / 128
        e = d + 1
    else:
        # Case 2: a is even
        b = (a ** 2) / 4 - 1
        if b % 2 == 0:
            # Subcase: b even
            c = (a ** 4) / 64 + (a ** 2) / 8 - 3 / 4
            d = (a ** 8) / 16384 + (a ** 6) / 1024 + (7 * a ** 4) / 512 + (5 * a ** 2 - 39) / 64
            e = d + 2
        else:
            # Subcase: b odd
            c = (a ** 4) / 32 + (a ** 2) / 4
            d = (a ** 8) / 2048 + (a ** 6) / 128 + (a ** 4) / 16 + (a ** 2) / 4
            e = d + 1
    return [round(a), round(b), round(c), round(d), round(e)]

def generate_unique_random_numbers(n):
    if n > (10000 - 3 + 1):
        raise ValueError("Cannot generate more than 9998 unique numbers in the range 3 to 10000.")
    return random.sample(range(3, 101), n)

# Formatting helpers
headers = ['a', 'b', 'c', 'd', 'e','a² + b² + c² + d²', 'e²','Match?']
col_widths = [6, 12, 15, 15, 20, 28, 28, 8]

def format_row(row, widths, align="right"):
    cells = []
    for val, width in zip(row, widths):
        if align == "left" and isinstance(val, str):
            cells.append(f"{val:<{width}}")
        else:
            cells.append(f"{val:>{width}}")
    return "| " + " | ".join(cells) + " |"

# Main execution
z = int(input("How many quintuples do you want? "))
rand = generate_unique_random_numbers(z)

# Print table header
print(format_row(headers, col_widths, align="left"))
print("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")

# Prepare CSV
with open('pythagorean_quintuples.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for number in rand:
        a, b, c, d, e = return_quad_lst(number)
        lhs = a**2 + b**2 + c**2 + d**2
        rhs = e**2
        match = "YES" if lhs == rhs else "NO"

        row_data = [a, b, c, d, e, lhs, rhs, match]
        print(format_row(row_data, col_widths))
        writer.writerow(row_data)

print("\n✅ Results saved to 'pythagorean_quintuples.csv'")
