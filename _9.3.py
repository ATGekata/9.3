numbers = input().split()

encountered_numbers = set()

for number in numbers:
    if number in encountered_numbers:
        print("YES")
    else:
        print("NO")
        encountered_numbers.add(number)
