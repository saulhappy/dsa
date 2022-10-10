"""
Define a fancy_cleanup function that accepts a single string argument
The function should clean up the whitespace on both sides of the
argument. It should also replace every occurrence of the letter "g" with the
letter "z" and every occurence of a space with an exclamation point (!).
"""

def strip_clean_text(text):
    return text.strip().replace("g", "z").replace(" ", "!")


print(strip_clean_text("       geronimo crikey  ")) # -> zeronimo!crikey
print(strip_clean_text("       nonsense  ")) # -> nonsense
print(strip_clean_text("grade")) # -> zrade
