#Day 9

#Students grades 
students_Scores ={
    "Bahaa": 99,
    "Muneera": 100,
    "Sara": 98,
    "Ahmed": 77,
    "Ali": 46,
    "Hussain": 85,
    "Hussam": 64,
}

for student in students_Scores:
    if students_Scores[student] > 90:
        print(f"{student} got an A")
        students_Scores[student] = "Outstanding"
    elif students_Scores[student] > 80:
        print(f"{student} got an B")
        students_Scores[student] = "Exceeds Expectations"
    elif students_Scores[student] > 70:
        print(f"{student} got an C")
        students_Scores[student] = "Acceptable"
    elif students_Scores[student] > 60:
        print(f"{student} got an D")
        students_Scores[student] = "Pass"
    else:
        print(f"{student} got an F")
        students_Scores[student] = "Fail"

print(students_Scores)
    

# Silent Auction Program
