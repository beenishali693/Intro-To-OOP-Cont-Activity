from school_schedule.student import Student

def test_student_valid_case():
    #Arrange
    name = "Elzara"
    grade = "senior"
    classes = ["bio", "chem", "english"]
    
    #Act 
    elzara = Student(name, grade, classes)

    #Assert 
    assert elzara.name == name
    assert elzara.grade == grade
    assert elzara.classes == classes
    assert len(elzara.classes) == 3

def test_add_class():
    #Arrange
    name = "Elzara"
    grade = "senior"
    classes = ["bio", "chem", "english"]
    new_class = "comp sci"
    
    #Act 
    elzara = Student(name, grade, classes)
    elzara.add_class(new_class)

    #Assert 
    assert elzara.classes == ["bio", "chem", "english", "comp sci"]
    assert len(elzara.classes) == 4

def test_get_num_classes():
    name = "Elzara"
    grade = "senior"
    classes = ["bio", "chem", "english"]
    
    #Act 
    elzara = Student(name, grade, classes)
    result = elzara.get_num_classes()

    #Assert 
    assert result == 3

def test_display_classes():
    name = "Elzara"
    grade = "senior"
    classes = ["bio", "chem", "english"]
    
    #Act 
    elzara = Student(name, grade, classes)
    result = elzara.display_classes()

    #Assert 
    assert result == "bio, chem, english"

def test_summary():
    name = "Elzara"
    grade = "senior"
    classes = ["bio", "chem", "english"]
    
    #Act 
    elzara = Student(name, grade, classes)
    result = elzara.summary()

    #Assert 
    assert result == (f"{name} is a {grade} "
            f"enrolled in {elzara.get_num_classes()} classes: "
            f"{elzara.display_classes()}")
    
def test_student_empty_classes():
    #Arrange
    name = "Elzara"
    grade = "senior"
    classes = []
    
    #Act 
    elzara = Student(name, grade, classes)
    result = elzara.get_num_classes()

    #Assert 
    assert elzara.name == name
    assert elzara.grade == grade
    assert elzara.classes == classes
    assert len(elzara.classes) == 0
    assert result == 0 

def test_add_class_blank_class():
    #Arrange
    name = "Elzara"
    grade = "senior"
    classes = ["bio", "chem", "english"]
    new_class = ""
    
    #Act 
    elzara = Student(name, grade, classes)
    elzara.add_class(new_class)

    #Assert 
    assert elzara.classes == ["bio", "chem", "english", ""]
    assert len(elzara.classes) == 4
