from collections import Counter
def search4vowels(phrase):
  vowels = ['a','e','i','o','u']
  found = []
  for letter in phrase:
    if letter in vowels:
      if letter not in found:
        found.append(letter)
  for vowel in found:
    print(vowel)
  counter = Counter(found)
  return counter.most_common(5)
