#simply bangla calculator

operation = input('''

আপনি কি যোগ (+) করবেন?

নাকি বিয়োগ (-) করবেন?

নাকি গুন (*) বা ভাগ (/) করবেন..?

কি করবেন সেটা আগে সিলেক্ট করুন!

''')

number1 = int(input('এবার প্রথম নাম্বারটি দিন:'))

number2 = int(input('এবার দ্বিতীয় নাম্বারটি দিন:'))

if operation == '+':

print('{} + {} = {}'.format(number1, number2,number1 + number2))

elif operation == '-':

print('{} - {} = {}'.format(number1, number2,number1 - number2))

elif operation == '*':

print('{} * {} = {}'.format(number1, number2,number1 * number2))

elif operation == '/':

print('{} / {} = {}'.format(number1,number2,number1 / number2))

else:

print('দুঃখিত আপনি সঠিক ভাবে লিখেন নি! প্লিজ আবার চেষ্টা করুন।')
