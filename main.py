import secrets
import json
from datetime import datetime

class RandomNumber:
    def __init__(self):
        self.current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.five_digit_number = None
        self.two_digit_number = None

    def generate_numbers(self):
        self.five_digit_number = secrets.randbelow(90000) + 10000
        self.two_digit_number = secrets.randbelow(90) + 10

    def save_to_json(self):
        data = {
            self.current_date: {
                "five_digit_number": self.five_digit_number,
                "two_digit_number": self.two_digit_number
            }
        }
        try:
            with open("numbers.json", "r+") as file:
                file_data = json.load(file)
                # Search and update duplicates when saving
                self.search_and_update_duplicates(file_data, self.five_digit_number, self.two_digit_number)
                file_data.update(data)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        except FileNotFoundError:
            with open("numbers.json", "w") as file:
                json.dump(data, file, indent=4)

    def search_and_update_duplicates(self, file_data, five, two):
        # Count appearances of each number
        five_count = sum(1 for date, numbers in file_data.items() if "duplicates" not in date and numbers["five_digit_number"] == five)
        two_count = sum(1 for date, numbers in file_data.items() if "duplicates" not in date and numbers["two_digit_number"] == two)

        if "duplicates" not in file_data:
            file_data["duplicates"] = {}

        # Alert and update duplicates only if there is more than one occurrence
        if five_count > 0:
            print(f"Notice: The five-digit number {five} has already been generated before and appears {five_count + 1} times.")
            file_data["duplicates"].setdefault("five_digit_number", {}).setdefault(five, 0)
            file_data["duplicates"]["five_digit_number"][five] = five_count + 1

        if two_count > 0:
            print(f"Notice: The two-digit number {two} has already been generated before and appears {two_count + 1} times.")
            file_data["duplicates"].setdefault("two_digit_number", {}).setdefault(two, 0)
            file_data["duplicates"]["two_digit_number"][two] = two_count + 1

# Example of using the class
generator = RandomNumber()
generator.generate_numbers()
print(f"Generated numbers: {generator.five_digit_number} (5 digits), {generator.two_digit_number} (2 digits)")
generator.save_to_json()
