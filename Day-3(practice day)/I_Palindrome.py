number = int(input())
# print(type(number))
n = number

sum = 0 
# print(type(sum))
while n!=0 : 
    digit = n % 10
    # print("digit: ", digit)
    sum = sum * 10 + digit
    # print("sum:  ",sum)

    n = n // 10 
    # print("n: ",n)


if sum == number:
    print(sum)
    print("YES\n")
else: 
    print(sum)
    print("NO\n")

