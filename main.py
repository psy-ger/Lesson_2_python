number_user = int(input('Enter your number: '))

#v1
print(number_user // 1000)
print(number_user % 1000 // 100)
print(number_user % 100 // 10)
print(number_user % 10)
#v2
for queue in str(number_user):
    print(queue)