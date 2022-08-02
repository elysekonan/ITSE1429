#! python
import os
import numbers

#Declare variables
courses=[]
students=[]
registrations=[]
name=[]
sel=0

#Method - Display header divider
def displayHeader(title):
    # Clear the screen.
    os.system('cls')
    print(title)
    print("==================================================================")

#Method - Display section/footer end line
def displayFooter(title):
        print("       {0}            ".format(title))

#Method - Press any key to continue
def displayPressKeyContinue():
    input("Press any key to continue: ")

#Method - Display error message
def displayErrorMessage(errorMsg):
    displayHeader("Error Encountered!!")
    print(errorMsg)
    displayFooter("End of message")
    displayPressKeyContinue()

#Method - Display successful confirmation message
def displaySuccessConfirm(confirmMsg):
    displayHeader("Operation Successful")
    print(confirmMsg)
    displayFooter("End of message")
    displayPressKeyContinue()

#Method - Check duplicate course id
def checkDuplicateCourseId(courseId, displayError):
    isCourseDup = False
    for course in courses:
        if (course['courseId'] == courseId):
            isCourseDup = True
    if ((isCourseDup == True) and (displayError == True)):
        displayErrorMessage("{0} already exist, enter a different course id".format(courseId))
    return isCourseDup

#Method - Check duplicate registration
def checkDuplicateRegistration(courseId, studentId):
    isDuplicate = False
    for reg in registrations:
        if((reg['courseId'] == courseId) and (reg['studentId'] == studentId)):
            isDuplicate = True
    return isDuplicate

#Method - Validate if value is a number
def isValueNumber(val):
    try:
        val = int (val)
        return True
    except ValueError:
        return False

#Method - Check duplicate student
def checkDuplicateStudentInfo(studentId):
    isStudentDup = False
    for student in students:
        if (student['studentId'] == studentId):
            isStudentDup = True
    return isStudentDup

#Method - Display Main Menu
def displayMainMenu():
    displayHeader("Welcome to Richland College Course Registration/Management Program")
    print("1. Add Course")
    print("2. Manage Course")
    print("3. Display Courses")
    print("4. Exit") 
    sel=input("Enter a selection:")
    if(sel !=""):
        isNumber = isValueNumber(sel)
        if (isNumber == True):
            sel=int(sel)
            validateMainMenuSelection(sel)
        else:
            displayErrorMessage("{0} is not a number. Enter a numeric selection from the main menu.".format(sel))
            displayMainMenu()
    else:
        displayMainMenu()

#Method - Display Manage Course Menu
def displayCourseMenu():
    displayHeader("Manage Course")
    print("1. Back to Main Menu")
    print("2. Add Student to Course")
    print("3. Display Students Enrolled in Course")
    sel=input("Enter a selection:")
    if(sel !=""):
        isNumber = isValueNumber(sel)
        if (isNumber == True):
            sel=int(sel)
            validateCourseManageSelection(sel)
        else:
            displayErrorMessage("{0} is not a number. Enter a numeric selection from the manage course menu.".format(sel))
            displayCourseMenu()
    else:
        displayCourseMenu()


#Method - Validate Manage Course Selection
def validateCourseManageSelection(_sel):
    if (_sel == 1):
        displayMainMenu()
    elif (_sel == 2):
        addStudentCourseStep1()  
    elif (_sel == 3):
        displayCourseEnrollment()   
    else:
        displayCourseMenu()  

# Exit the program
def Exit():
    SystemExit()
    
#Method - Validate Main Menu Selection
def validateMainMenuSelection(_sel):
    if(_sel == 1):
        addCourse()  
    elif (_sel == 2):
        displayCourseMenu()
    elif (_sel == 3):
        displayCourses() 
    elif (_sel == 4):
        Exit()
    else:
        displayErrorMessage("{0} is an invalid option. Enter a valid option from the main menu".format(_sel))
        displayMainMenu()



#Method - Add course 
def addCourse():
    displayHeader("Add Course")
    courseId = input("Enter course id, e.g. \"ITSC101\"? ")
    if (courseId != ""):
        isCourseDup = checkDuplicateCourseId(courseId, True)
        if(isCourseDup == False):
            courseName = input("Enter course name for {0}, e.g. \"Intro to Accounting\"? ".format(courseId))
            if (courseName != ""):
                courses.append({'courseId': courseId, 'courseName': courseName})
                displaySuccessConfirm("{0} added into the system".format(courseId))
                displayMainMenu()
            else:
                addCourse()
    else:
        addCourse()

#Method - Display list of courses
def displayCourses():
    displayHeader("Active Course List - {0} record(s)".format(len(courses)))
    seqNo = 1
    for course in courses:
        print("{0}. {1} - {2}".format(seqNo, course['courseId'], course['courseName']))
        seqNo=seqNo + 1
    displayFooter("End of report")
    displayPressKeyContinue()
    displayMainMenu()

#Method - Add student to course - pick course
def addStudentCourseStep1():
    displayHeader("Add Student to Course")
    courseId = input("Enter course id, e.g. ITSC101? ")
    if (courseId != ""):
        isCourseExist = checkDuplicateCourseId(courseId, False)
        if(isCourseExist == True):
            addStudentCourseStep2(courseId)
        else:
            displayErrorMessage("{0} doesn't exist in our system, enter a different course id".format(courseId))
            displayCourseMenu()
    else:
        addStudentCourseStep1()

#Method - Add student to course - enter student
def addStudentCourseStep2(courseId):
    displayHeader("Add Student to Course: {0}".format(courseId))
    studentId = input("Enter the six digit student id, e.g. 234555? ")
    if (studentId != ""):
        isStudentExist = checkDuplicateStudentInfo(studentId)
        if(isStudentExist == False):
            studentName = input("Enter student full name for student id: {0}, e.g. John M Smith? ".format(studentId))
            name.append(studentName)
            students.append({'studentId': studentId, 'studentName': studentName})
            isDuplicate = checkDuplicateRegistration(courseId, studentId)
            if (isDuplicate == True):
                displayErrorMessage("student id {0} - {1} is already enrolled in {2}".format(studentId, studentName, courseId))
                displayCourseMenu()    
            registrations.append({'courseId':courseId, 'studentId': studentId})
            displaySuccessConfirm("{0} - {1} added to {2}".format(studentId, studentName, courseId))
            displayCourseMenu()
    else:
        addStudentCourseStep2(courseId)


#Method - Display students enrolled in course - Enter course
def displayCourseEnrollment():
    displayHeader("Display Course Enrollement")
    courseId = input("Enter course id, e.g. ITSC101? ")
    isCourseExist = checkDuplicateCourseId(courseId, False)
    if(isCourseExist == True):
        displayCourseEnrollmentStep2(courseId)
    else:
        displayErrorMessage("{0} doesn't exist in our system, enter a different course id".format(courseId))
        displayCourseMenu()


#Method - Display students enrolled in course - Step 2
def displayCourseEnrollmentStep2(courseId):
    _students = []
    for reg in registrations:
        if (reg['courseId'] == courseId):   
            _students.append(reg['studentId'])
    seqNo = 1
    displayHeader("{0} Course Registration - {1} student(s)".format(courseId, len(_students)))
    n = 0
    for student in _students:
        print("{0}. {1}".format(seqNo, student), name[n])
        seqNo = seqNo + 1
        n += 1
    displayPressKeyContinue()
    displayCourseMenu()

#Display Main Menu
displayMainMenu()
