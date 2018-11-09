import re
string="Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."

def get_vowel_count(string):
    regex=re.compile("/|(a)|(e)|(i)|(o)|(u)|/")
    match=regex.findall(string)
    out={
        "a":0,"e":0,"i":0,"o":0,"u":0
    }
    for t in match:
        out["".join(t)]+=1

    return out

assert get_vowel_count("aaaaa")["a"] is 5
assert get_vowel_count("eeeee")["e"] is 5
assert get_vowel_count("iiiii")["i"] is 5
assert get_vowel_count("ooooo")["o"] is 5
assert get_vowel_count("uuuuu")["u"] is 5
assert get_vowel_count("cdfgh")["a"] is 0