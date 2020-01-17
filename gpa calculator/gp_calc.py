#getting the individual courses
#getting their scores over 100
#getting the equivalent unit of the score over 100
#getting the grade of the score over 100
#getting the individual unit of the course
#for the claculation, total units followed by = a
#unit of grade attained multiplied by unit of course = b
#b/a

all_scores = [0]
all_units = [0]

def greeting():
    print('Welcome to the gpa calculator programe')
def getGrade():
    
    totalCourses = input('Enter your total number of courses:')
    for i in range(1,int(totalCourses)+1):
        print("enter your score for course ",i)
        score = int(input())
        print("enter your unit for course ",i)
        unit = int(input())
        all_units.append(unit)
        all_scores.append(score)

    units_of_courses = list(map(unitEquiv,all_scores))

    weights = [0,0] 
    for i,j in zip(units_of_courses,all_units):
        weights[0] +=  i*j
        weights[1] += j
    return  weights[0]/weights[1]

def unitEquiv(score):
    if score > 69 and score < 101:
        return 5
    elif score > 59 and score < 70:
        return  4
    elif score > 49 and score < 60:
        return  3
    elif score > 44 and score < 50:
        return  2
    elif score > 39 and score < 45:
        return  1
    else:
         return  0    

greeting()
reply = input('Choose y or n to run this programme: ')
while reply  == 'y':
    x = getGrade()
    print(x)
    break







    