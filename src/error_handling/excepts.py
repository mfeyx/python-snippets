
has_error = False
error = None
name = None
age = None

try:
    age = int(input("Age: "))
except ValueError as e:
    print(str(e))
    has_error = True
    error = e
else:
    name = input("Name: ")
finally:
    # print(f"programm finished with error: {has_error}")
    print(f"Name: {name}, age: {age}")

if has_error:
    raise error
