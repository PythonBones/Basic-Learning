# Weight Conversion
print()
print('Convert Units:  ')
print()
unit = input('Enter Unit of Mass:  ')
new = input('Enter New Unit:  ')
# Kilos - Pounds
if unit == 'kg' and new == 'lbs' :
    mass = input('Enter number:  ')
    lb = float(mass) * 2.20462262
    print(f'{lb:.0f}' + 'lbs')
# Pounds - Kilos
elif unit == 'lbs' and new == 'kg' :
    mass = input('Enter number:  ')
    kg = int(mass) / 2.20462262
    print(f'{kg:.2f}' + 'kg')
# Stone and Pounds
elif unit == 'lbs' and new == 'st' :
    mass = input('Enter number:  ')
    st = int(mass) // 14
    lb = int(mass) % 14
    print(f'{st}' + 'st ' + f'{lb}')
# Stone - Pounds
elif unit == 'st' and new == 'lbs' :
    mass = input('Enter number:  ')
    lbs = int(mass) * 14
    print(f'{lbs}' + 'lbs')
# Kilos - Stone
elif unit == 'kg' and new == 'st' :
    mass = input('Enter number:  ')
    ibmass = float(mass) * 2.20462262
    st = int(ibmass) // 14
    lb = int(ibmass) % 14
    print(f'{st}' + 'st ' + f'{lb}')
# Stone - Kilos
elif unit == 'st' and new == 'kg' :
    st = input('Enter Stones:  ')
    lb = input('Enter Pounds:  ')
    totallbs = (int(st) * 14) + int(lb)
    kg = int(totallbs) / 2.20462262
    print(f'{kg:.2f}' + 'kg')
# Grams - Ounces
elif unit == 'g' and new == 'oz' :
    mass = input('Enter number:  ')
    oz = int(mass) / 28.3495231
    print(f'{oz:.2f}' + 'oz')
# Kilos - Ounces
elif unit == 'kg' and new == 'oz' :
    mass = input('Enter number:  ')
    g = float(mass) * 1000
    oz = float(g) / 28.3495231
    print(f'{oz:.2f}' + 'oz')
# Ounces - Grams
elif unit == 'oz' and new == 'g' :
    mass = input('Enter number:  ')
    g = float(mass) * 28.3495231
    print(f'{g:.0f}' + 'g')
# Ounces - Kilos
elif unit == 'oz' and new == 'kg' :
    mass = input('Enter number:  ')
    g = float(mass) * 28.3495231
    kg = float(g) / 1000
    print(f'{kg:.0f}' + 'kg')
