upper_limit = int(input("Enter the upper limit: "))  # Get the upper limit from the user

# Iterate from 1 to the upper limit, but only print odd numbers
for num in range(1, upper_limit + 1):
  if num % 2 != 0:
    print(num)

x = int(input("Enter the upper limit of the range: "))

i = 1
while i <= x:
  if i % 2 != 0:
    print(i)
  i += 1
