def find_last_alphabetical_word():

    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    word3 = input("Enter third word: ")

    last_word = max(word1, word2, word3)

    print(f"The word that comes last alphabetically is: {last_word}")

find_last_alphabetical_word()