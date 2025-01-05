def printDict(dictionary:dict) -> None:
    print()
    for key in dictionary:
        print(f'{key} : {' '.join(dictionary[key])}')
    print()