def main():
    total_spent = 0.0

    print("--- Expense Tracker ---")
    print("Enter expense amounts one by one.")
    print("Type 'done' or '0' when you are finished.\n")

    while True:
        user_input = input("Enter expense: ").strip()

        if user_input.lower() == "done" or user_input == "0":
            break

        try:
            expense = float(user_input)

            if expense < 0:
                print("Please enter a positive expense amount.\n")
                continue

            total_spent = total_spent + expense
            print(f"Added ${expense:.2f} | Running Total: ${total_spent:.2f}\n")

        except ValueError:
            print("Invalid input. Please enter a numerical value (e.g., 50, 20.50).\n")

    print("-----------------------")
    print(f"Total Spent: ${total_spent:.2f}")
    print("-----------------------")


if __name__ == "__main__":
    main()