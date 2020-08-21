"""
URL: http://www.pythonchallenge.com/pc/def/map.html

"""


clue = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
""".replace('\n', ' ').strip()


def maketrans(secret):
    literals = set([' ', ')', '(', '.', "'"])
    out = []
    for i in secret:
        if i in literals:
            out.append(i)
        else:
            ni = ord(i) + 2
            if ni > 122:
                di = ni - 122 - 1
                ni = 97 + di
            out.append(chr(ni))
    return ''.join(out)


print(maketrans(clue))
print(maketrans('map'))
