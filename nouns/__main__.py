import sys
import json
from functools import reduce
from .nouns import centrality

if not sys.stdin.isatty():
    texts = [sys.stdin.read()]
else:
    texts = [open(arg).read() for arg in sys.argv[1:]]

scores = []
for text in texts:
    scores.append(centrality(text))

noun_lookup = {}
for scoring in scores:
    for record in scoring:
        noun_lookup[record['noun']] = noun_lookup.get(record['noun'], [])
        noun_lookup[record['noun']].append(record)

joined_results = []
for noun, records in noun_lookup.items():
    if len(records) == len(texts):
        score = reduce(lambda a, x: a * x['score'], records, 1)
        if score:
            joined_results.append({
                'noun': noun,
                'score': score,
                'intervals': (
                    [record['intervals'] for record in records]
                    if len(records) > 1
                    else records[0]['intervals']
                ),
            })

print(json.dumps(joined_results))
