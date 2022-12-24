def cheker(data):
    if type (data) != str:
        raise TypeError(f"Тексу не має!Ваші дані є {type(data)},а має бути str")
    else:
        return data

num = 5
text = "Hello"
cheker(text)

