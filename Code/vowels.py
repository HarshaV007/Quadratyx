import os
import sys
import pandas as pd
import re
os.chdir("C:\\Users\Harsha Vardhan\OneDrive\Desktop\Code")
File=sys.argv[1]
def countCharacterType(filename):

    f = open(filename,'r')
    t = f.read()
    l = []
    res = re.findall(r'\w+', t)
    for i in range(len(res)):

        input = res[i]
        # Initiating values
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        consonant = 0

        for n in range(0, len(input)):

            ch = input[n]
            if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):


                ch = ch.lower()

                if (ch == 'a'):

                    a += 1
                elif (ch == 'e'):
                    e += 1
                elif (ch == 'i'):
                    i += 1
                elif (ch == 'o'):
                    o += 1
                elif (ch == 'u'):
                    u += 1
                else:
                    consonant += 1

        d = {"Word": input, "A": a, "E": e, "I": i, "O": o, "U": u, "Consonants": consonant}
        l.append(d)
        df = pd.DataFrame.from_records(l)
    return df

print(countCharacterType(filename=File))



