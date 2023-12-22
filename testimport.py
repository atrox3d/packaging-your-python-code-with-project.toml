import os, sys
import traceback

filename = os.path.basename(__file__)

def decorator(func):
    funcname = func.__name__

    def reset_modules(module):
        for key in [k for k in sys.modules.keys() if k.startswith('snake')]:
                del sys.modules[key]
        del module
    
    def printmodule(module):
            modulename = module.__name__
            moduleattribs = [item for item in dir(module) if not item.startswith("_")]
            print(f'{funcname} | dir({modulename}) | {moduleattribs}')

    def wrapper():
        try:
            module, say = func()
            say(f'{filename}:{funcname}')
            printmodule(module)            
            reset_modules(module)            
        except Exception as e:
            print(f'{funcname}: {e!r}')
            # traceback.print_exc()
    return wrapper

@decorator
def from_snakesay():
    from snakesay import snake
    print(f'{snake = }')
    return snake, snake.say

@decorator
def import_snakesay_snake():
    import snakesay.snake
    print(f'{snakesay.snake = }')
    return snakesay.snake, snakesay.snake.say

@decorator
def import_snakesay():
    import snakesay
    print(f'{snakesay = }')
    return snakesay.snake, snakesay.snake.say

def main(fn):
    fn()

if __name__ == '__main__':
    print(f'{sys.path[0:2] = }')
    main(from_snakesay)
    # main(import_snakesay_snake)
    main(import_snakesay)
