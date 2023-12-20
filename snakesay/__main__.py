import sys

print(f'{sys.path[0] = }')

try:
    # import snake
    from snakesay import snake

    snake.say(" ".join(sys.argv[1:]))
except ModuleNotFoundError as mnfe:
    print(f'{mnfe!r}')    