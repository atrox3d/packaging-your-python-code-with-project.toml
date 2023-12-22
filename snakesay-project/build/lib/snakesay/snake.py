SNAKE = r"""  \
   \    __
    \  {oo}
       (__)\ 
        "  \\ 
           _\\__
          (_____)_
         (________)Oo°
"""

def bubble(message: str) -> str:
    length = len(message) + 2
    return f'''
 {'_'  * length}
( {message} )
 {'¯' * length}
    '''


def say(message: str) -> None:
    print(bubble(message))
    print(SNAKE)