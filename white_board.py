#input/output: string
v = 'aeiou'

def vowels(string):
    for x in string:
        for y in v:
            if y == x:
                string = string.replace(x, "")
    return string

print(vowels('hello'))