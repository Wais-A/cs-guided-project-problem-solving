"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    # Your code here
    import math
    count = []
    length = len(list(input_str))
    i = 1
    while i <= length:
        count.append(i)
        i += 1
    Sum = sum(count)
    x = int(Sum / length)
    if length % 2 == 0:
        return input_str[x -1: x + 1]
    else:
        return input_str[x - 1: x ]
    
        

    


print(get_middle('test'))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle('Almakaleh'))
print(get_middle('floccinaucinihilipilification'))
print(get_middle('pneumonoultramicroscopicsilicovolcanoconiosis'))
print(get_middle('lopado­temacho­selacho­galeo­kranio­leipsano­drim­hypo­trimmato­silphio­parao­melito­katakechy­meno­kichl­epi­kossypho­phatto­perister­alektryon­opte­kephallio­kigklo­peleio­lagoio­siraio­baphe­tragano­pteryg'))


#if the  length is even and the average is 2.5 the first number should be floored to 2 and minus 1 and the 2nd is ceil() to 3
#if the length is odd and the average is 3.5 the first number should be floored to 3 and the 2nd maxed to 4
# print(math.ceil(3.5))
