def area(radius):
    return 3.142 * radius * radius

def vol(area, length):
    print (area * length)

radius = int(input('Enter a radius '))
length = int(input('Enter a length '))

vol(area(radius),length)
