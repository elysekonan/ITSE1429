#global variables
senior_citizens=0
non_seniors=0

Age=int(input("How old are you? "))
if (Age>=65):
    senior_citizens=senior_citizens+1
else:
    non_seniors=non_seniors+1
print(senior_citizens, "seniors citizens")
print(non_seniors, "non seniors")
