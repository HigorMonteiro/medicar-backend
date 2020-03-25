import random
import string


def rando_username():
   letters = string.ascii_lowercase
   return ''.join(
       random.choice(letters) for i in range(5))
