def details(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)

details(name="shashi",age = 18,city = "hyderabad")