print("Enter 'x' for exit.");
string = input("Enter any string to reverse it: ")
if string == 'x':
    exit();
else:
    revstring = string[::-1];
    print("\nOriginal String =",string);
    print("Reversed String =",revstring);

