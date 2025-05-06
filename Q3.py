print("Number divisible by 3: ")
for i in range(1,101):
	if i % 3 == 0:
		print(i)

print("\nNumber divisible by 5:")

for i in range(1,101):
	if i % 5 == 0:
		print(i)

print("\nNumbers divisible by both 3 and 5:")
for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		print(i)
