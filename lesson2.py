def is_palindrome(word):
    word1=""
    word2=""
    word=word.lower()
    for i in word:
        if(i.isalpha()):
            word1+=i
    for i in word[::-1]:
        if(i.isalpha()):
            word2+=i
    print(word1==word2)

word="Eva, can I see bees in a cave?"
is_palindrome(word)