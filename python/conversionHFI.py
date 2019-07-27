# Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches

# 1cm = 0.0328084 foot
# 1cm = 0.3937008 inch

def convertor(cm):
    foot = 0.0328084 * cm
    inch = 0.3937008 * cm
    print(foot)
    print(inch)

cm = float(input('Enter the height in cm : '))
convertor(cm)