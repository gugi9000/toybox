message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output"""
    message = message.split("\n")
    msg = ''
    for x in message:
        msg = msg + x + '|'
    return msg[0:len(msg)-1]


print (split_in_columns(message))
