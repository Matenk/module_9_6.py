def all_variants(text):
    for k in text:
        yield k


a = all_variants('abc')
for i in a:
    print(i)