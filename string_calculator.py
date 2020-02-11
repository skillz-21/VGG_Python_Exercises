def string_counter(word):
    upper_case = ''
    lower_case = ''
    for chars in word:
        if chars.isupper():
            upper_case += chars
        elif chars.islower():
            lower_case += chars
    print(f"The no of upppercase is: {len(upper_case)}")
    print(f"The no of lowercase letters is: {len(lower_case)}")
word = input("Enter string: ")
string_counter(word)