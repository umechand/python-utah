
#Exercise #1

# 1. What are the parent and child classes here?

#Answer: The parent class is Spell, child classes are Accio and Confundo.

# 2. What does the code print out? (Try figuring it out without running it in Python)

#Answer:
    # Accio
    # Summoning Charm Accio
    # No description
    # Confundus Charm Confundo
    # Causes the victim to become confused and befuddled.


# 3. Which get description method is called when ‘study spell(Confundo())’ is executed? Why?

#Answer:

# The method inside the Confundo class is called because methods in the child class override those in the
# parent class if they happen to exist in both the classes.

# 4. What do we need to do so that ‘print Accio()’ will print the appropriate description
# (‘This charm summons an object to the caster, potentially over a significant distance’)?
# Write down the code that we need to add and/or change.

class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

    def get_description(self):
        return "No description"

    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")

    def get_description(self):
	    return 'This charm summons an object to the caster, potentially over a significant distance'

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

class Confundo(Spell):

    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def  get_description(self):
        return "Causes the victim to become confused and befuddled."

def study_spell(spell):
        print(spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

