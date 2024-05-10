def replaceVowel(test_str, a):
    vowels = 'AEIOUYaeiouy'
    for ele in vowels:
        test_str = test_str.replace(ele, a)
    return test_str

word = input()
a = "#"
result = replaceVowel(word, a)
print(result)
