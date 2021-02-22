import random
import math

range = 10_000_000
secret = random.randint(0, range)
search = round(range / 2)
div = math.ceil(range / 4)
print(secret)

def binary_search(search, div, secret):
    if search == secret:
        return search

    elif search > secret:
        return binary_search(search - div, math.ceil(div / 2), secret)

    elif search < secret:
        return binary_search(search + div, math.ceil(div / 2), secret)

search = binary_search(search, div, secret)

print(search)
