def balanced(str):
    s = list()

    for ch in str:
        if ch == "(" or ch == "{" or ch == "[" :
            s.append(ch)
        if ch == ")" or ch == "}" or ch == "]":
            if not s:
                return False
            s.pop()

    return not s

if __name__ == "__main__" :
    str = input("enter brackets [{()}]:  ")

    if balanced(str):
        print(str,"is balanced")
    else:
        print(str,"is not balanced")