def count_even_odd (start, end):
    even_count = 0
    odd_count = 0
    for num in range (start, end + 1):
        if num % 2 ==0:
            even_count += 1
        else:
            odd_count += 1
        
    return even_count, odd_count


start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range:"))

even,odd=count_even_odd(start, end)

print(f"Even numbers: {even}")
print (f"Odd numbers: {odd}")


 
