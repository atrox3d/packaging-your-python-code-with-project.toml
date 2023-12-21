import os, sys

filename = os.path.basename(__file__)

def from_snakesay():
    name = from_snakesay.__name__
    from snakesay import snake
    print(f'{name} | dir(snake) | {[item for item in dir(snake) if not item.startswith("_")]}')
    snake.say(f'{filename}:{name}')

def import_snakesay_snake():
    # import snakesay as ss
    name = import_snakesay_snake.__name__
    import snakesay.snake
    print(f'{name} | dir(snakesay.snake) | {[item for item in dir(snakesay.snake) if not item.startswith("_")]}')
    snakesay.snake.say(f'{filename}:{name}')

def import_snakesay():
    name = import_snakesay.__name__
    print(f'{name} | import snakesay')
    import snakesay
    print(f'{name} | dir(snakesay) | {[item for item in dir(snakesay) if not item.startswith("_")]}')
    # print(f'{snakesay.__file__ = }')
    snakesay.snake.say(f'{filename}:{name}')

def main(fn):
    try:
        fn()
    except Exception as e:
        print(f'{fn.__name__}: {e!r}')
        # quit()

if __name__ == '__main__':
    print(f'{sys.path[0:2] = }')
    main(import_snakesay)
    main(import_snakesay_snake)
    main(from_snakesay)