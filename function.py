def validate(nomre):
    if (len(nomre)!=9):
        message="Your car's license plate number's length can't be longer or shorter than 9!"
    elif (type(int(nomre[0:2])) is not int):
        message="You must enter numbers!"
    elif (type(int(nomre[6:9])) is not int):
        message="You must enter numbers!"
    elif (nomre[3:5].isalpha() is not True):
        message="You must enter letters!"
    elif (nomre[3:5].upper() is False):
        message="Letters must be capitalized!"
    elif ("-"!=nomre[2] or "-"!=nomre[5]):
        message="You must enter -"
    else:
        message="You entered car's license plate number succesfully!"
    return message

print(validate("12-HE-203"))
