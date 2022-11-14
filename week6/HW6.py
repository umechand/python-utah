
# Exercise #1:

try:
    word = open("most_popular_words_in_english.txt", "r")
    contents = word.read().splitlines()
    word.close()
    word = input("Enter a word in English: ").lower()
    if word in contents:
        print("Entered word is one of the most 100 popular English words")
    else:
        print("Entered word is not present in the list.")
except:
    print("Something went wrong!")


