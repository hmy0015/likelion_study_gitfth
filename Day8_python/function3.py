def print_root(a, b, c):
	r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) /(2 * a)
	r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) /(2 * a)
	
	print('해는 {} 또는 {}'.fomat(r1, r2))
	
x = 1
y = 2
z = -8

print_root(x, y, z)

x = 2
y = -6
z = -8

print_root(x, y, z)