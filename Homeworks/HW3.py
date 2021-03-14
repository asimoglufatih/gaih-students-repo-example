student = dict()
listOfGrade = []

def getGrade():
    for index in range(5):
        student[index] = {}
        midterm = int(input("Enter midterm grade: "))
        project = int(input("Enter project grade: "))
        final = int(input("Enter final grade: "))
        listOfGrade.insert(index, calculatePassingGrade(midterm,project,final))
        student[index]["midterm"] = midterm
        student[index]["project"] = project
        student[index]["final"] = final
    listOfGrade.sort(reverse = True)

def calculatePassingGrade(midterm, project, final):
    return midterm * (0.3) + project * (0.3) + final * (0.4)

getGrade()
print(listOfGrade)
