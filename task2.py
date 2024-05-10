def Wrong_pin(pin):
    if len(pin) not in (4, 6):
        return True
    for char in pin:
        if not char.isdigit():
            return False

num = input("Enter: ->")
if Wrong_pin(num):
    print("wrong")
else:
    print("True")
