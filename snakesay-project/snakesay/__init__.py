
import os

print(f'__INIT__.PY | from . import snake')
from . import snake
# import snake
filename = os.path.basename(snake.__file__)
print(f'__INIT__.PY | {filename = }')
a = 5
print(f'__INIT__.PY | end')

