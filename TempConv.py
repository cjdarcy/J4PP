def main():
    fahr = float(input("Enter the temperature in F: "))
    cel = (fahr - 32) * 5.0/9.0
    print("The temperature in C is: ", str(cel))
