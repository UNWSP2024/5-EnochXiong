def kilometer_conversion(kilometers):
    miles = 0.0

    miles = kilometers * 0.60934

    print()
    return miles

if __name__ == '__main__':
    print('in main')

    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometer_conversion(kilometers)
    print("Distance in miles:", miles)
