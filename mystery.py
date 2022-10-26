"mystery.py"
def mystery():
    """mystery.py"""
    num = 10 * 3

    if num == 10:
        print(f"Num was equal to {num}")
        num = num * 10
    if num == 20:
        print(f"Num was equal to {num}")
        num = num * 20
    if num == 30:
        print(f"Num was equal to {num}")
        num = num * 30

    print(f"Value of returned num is: {num}")
    return num

mystery()
