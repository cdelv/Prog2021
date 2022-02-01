import re
from collections import Counter

with open('data.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)

max_key = max(word_counts, key=word_counts.get)
print(max_key)