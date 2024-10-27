'''
6) Convert Pascal Case string into snake_case (4 ქულა)

You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

Examples:
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7 Test"        -->  "app7_test"
1                 -->  "1"


'''






def a(b):
    c = " "
    for i in b:
        if i.isupper():
            c += "_" + i.lower()
        else:
            c += i.lower()
        print(c) 
a("TestController") # gameoreba raotm xdeba ver  da dasawyishi _ daikidet ise xom sworea :( ? 