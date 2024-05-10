def fosila(word):
    a = word[0:2]
    b = 0
    while b < 2:
        fosila = a + "... "
        print(fosila, end="")
        b += 1
    print(word + "?")

fosila("incredible")
