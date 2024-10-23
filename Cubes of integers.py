def sum_of_cubes(m, n):
    if m > n:
        print("M is greater than N, returning 0")
        return 0
    else:
        return sum(i**3 for i in range(m, n+1))

print(sum_of_cubes(2, 4))  
print(sum_of_cubes(5, 5))  
print(sum_of_cubes(7, 3))  
  

