def digitalroot(number=0, shallow=False):
    stringalized = str(number)
    while(len(stringalized) > 1):
        summation = 0
        for char in stringalized:
            summation += int(char)
        stringalized = str(summation)
        if shallow:
            break
    return int(stringalized)
