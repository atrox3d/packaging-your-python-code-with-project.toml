import os, sys
import traceback

filename = os.path.basename(__file__)

def decorator(func):
    def wrapper():
        try:
            funcname = func.__name__
            module, say = func()
            modulename = module.__name__
            moduleattribs = [item for item in dir(module) if not item.startswith("_")]
            print(f'{funcname} | dir({modulename}) | {moduleattribs}')
            say(f'{filename}:{funcname}')
            for key in [k for k in sys.modules.keys()]:
                if key.startswith('snake'):
                    del sys.modules[key]
            del module
        except Exception as e:
            print(f'{funcname}: {e!r}')
            # print(traceback.format_exc())
            # raise

    return wrapper

@decorator
def from_snakesay():
    from snakesay import snake
    return snake, snake.say

@decorator
def import_snakesay_snake():
    import snakesay.snake
    return snakesay.snake, snakesay.snake.say

@decorator
def import_snakesay():
    import snakesay
    return snakesay.snake, snakesay.snake.say

def main(fn):
    fn()

if __name__ == '__main__':
    print(f'{sys.path[0:2] = }')
    main(from_snakesay)
    main(import_snakesay_snake)
    main(import_snakesay)
    