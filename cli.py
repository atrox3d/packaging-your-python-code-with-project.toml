import sys

try:
    import snake
except ModuleNotFoundError:
    snake = lambda: None
    snake.say = print

snake.say(" ".join(sys.argv[1:]))