def numeric_to_letter_grade():


    #get user input of a numerical grade
    grade = input("Enter your grade: ")

    #cast to an int
    grade =int(grade)

    #test the range of the number and print the appropriate letter grade
    if grade >= 90:
        print('A')

    elif grade >= 80:
        print('B')
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('F')

numeric_to_letter_grade()        
    
