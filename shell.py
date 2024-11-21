import basic

while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>',text)
    if error: print(error.as_str())
    else: print (result)