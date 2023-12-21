from snakesay import snake

try:
    start = __file__.rindex('/') + 1
except ValueError as ve:
    start = __file__.rindex('\\') + 1

filename = __file__[start:]

snake.say(f'hello from {filename}')