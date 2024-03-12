DB = {}
def getLongUrl(shortUrl):
    # https://www.c.in.abcde -> abcde    key = shortUrl.split('/')[-1]
    if key in DB:
        return DB[key]
    else:
        print("Short URL doesn't exist")

getLongUrl("https/www.google.com/abc")
print(DB)