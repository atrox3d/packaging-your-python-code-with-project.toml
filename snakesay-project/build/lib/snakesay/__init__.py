def outerborder(messagelen, margin):
    print('*' * (2 + messagelen + margin * 2))

def innerborder(messagelen, margin):
    print('*' + ' ' * (messagelen + margin * 2) + '*')


def box(message):
    lm = len(message)
    margin = 2
    outerborder(lm, margin)
    innerborder(lm, margin)
    print( '*', end='')
    print(' ' * margin, end='') 
    print(message, end='') 
    print(' ' * margin, end = '') 
    print('*')
    innerborder(lm, margin)
    outerborder(lm, margin)


box('HELLO FROM __INIT__.PY')
