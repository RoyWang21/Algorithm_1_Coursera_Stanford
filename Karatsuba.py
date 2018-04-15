def karatsuba(x, y):
	if len(x) != len(y):
		print("Lengths of two multilier are not equal!")
		return 404
	n = len(x)
	if len(x) == 1:
		return int(x) * int(y)
	elif len(x) % 2 == 1:
		print(f"Number {x} has odd # of digits!")
	elif len(x) % 2 == 0:
		a = x[: -n // 2]
		b = x[-n // 2 : ]
		c = y[: -n // 2]
		d = y[-n // 2 : ]
		multi = (10 ** n) * karatsuba(a , c) + (10 ** (n // 2)) * (karatsuba(a , d) + karatsuba(b , c)) + karatsuba(b , d)
		print(f"x = {x}, y = {y}, a = {a}, b = {b}, c = {c}, d = {d}")#"multi: {x} * {y} = {int(multi)}")
		return int(multi)

def karatsuba1(x, y):
    if x < 10 or y < 10:
        return x * y
    x_array = str(x)
    y_array = str(y)
    half_size = max(len(x_array), len(y_array)) // 2
    firsthalf_x = int(x_array[:-half_size])
    secondhalf_x = int(x_array[-half_size:])
    firsthalf_y = int(y_array[:-half_size])
    secondhalf_y = int(y_array[-half_size:])
    sum_x = firsthalf_x + secondhalf_x
    sum_y = firsthalf_y + secondhalf_y
    first = karatsuba1(firsthalf_x, firsthalf_y)
    second = karatsuba1(sum_x, sum_y)
    third = karatsuba1(secondhalf_x, secondhalf_y)
    return first * 10**(2 * half_size) + (
        (second - first - third) * (10**half_size)) + third
#---------------------------

x = input("Input the first number for multiplication: ")
y = input("Input the second number for multiplication: ")

f = open("karatsuba.txt", 'w')

result = karatsuba(x, y)
#result = karatsuba1(int(x), int(y))

print (f"Final result: {int(result)} ")

f.write(str(int(result)))
f.close()