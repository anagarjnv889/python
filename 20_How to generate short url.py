import string
import random
DB = {}
def urlsh(Longurl):
    """
    given a long URL, return a short URl
    """
    l = random.randint(4,6)
    chars = string.ascii_letters
    shortUrl = ''.join([random.choice(chars) for i in range(5)])
    if shortUrl in DB:
        return urlsh((Longurl))
    else:
        DB[shortUrl] = Longurl

    result = "cm.in/"+shortUrl
    return result
url = "https://www.codingminutes.com"

print("Short url is ",urlsh(url))
print("Database data is",DB)


