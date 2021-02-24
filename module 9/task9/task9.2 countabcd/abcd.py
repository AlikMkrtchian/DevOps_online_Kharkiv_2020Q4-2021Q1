def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

#string = input()
#print(countvowels(string))


def test_abcd():
    assert countvowels('alik') == 3
