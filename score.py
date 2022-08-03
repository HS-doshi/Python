"""
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""

score = input("Enter Score: ")
score1 = (float)(score)

if(score1>=0.9):
    print("A")
elif(score1>=0.8):
    print("B")
elif(score1>=0.7):
    print("C")
elif(score1>=0.6):
    print("D")
elif(score1<0.6):
    print("F")
else:
    print("Please Enter proper input!!(range between 0.0-1.0)")
