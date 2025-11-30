def yell(*args):
    # uppercased = map(str.upper, map(str, args))
    uppercased = [str(arg).upper() for arg in args]
    # for word in uppercased:
    #     print(word)
    # print(*uppercased)
    return " ".join(uppercased)


print(yell("hello", "world", "python"))