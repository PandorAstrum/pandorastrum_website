# currently working in
#\Users\Ana Ash\Desktop\WebFinal\Django\main\main


from .base import *

from .production import *

try:
   from .local import *
except:
   pass