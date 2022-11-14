
# Week 5
# CodeAlong3

def animal():
    legs = "animal local"
    print(legs)

    global legs

    legs = "Global changed"
    print(legs)


def dog():
    legs = "dog local"
    print(legs)
    animal()
    print(legs)


legs = 'Global'
print(legs)
dog()
print("Global", legs)

