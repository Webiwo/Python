def calculate():
    while True:
        try:
            age = int(input("Please, provide your age:"))
            value = 10 / age
        except ValueError:
            print("Please provide a number")
        except ZeroDivisionError as zero_err:
            print(f"Age can not be zero: {zero_err}")
        else:
            print("Thank you")
            break


calculate()
