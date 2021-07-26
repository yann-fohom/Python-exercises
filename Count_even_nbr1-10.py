# Write a program in python that displays and count all even numbers between 1 and 10:
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers between 1 and 10") 
# Bonus: for odd numbers just modify the if statement and check all the numbers where the modulo (%) is = 1, ie: number%2 ==1
