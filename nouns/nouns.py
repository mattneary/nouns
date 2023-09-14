import spacy
import itertools
import networkx as nx

nlp = spacy.load("en_core_web_sm")

def centrality(text):
    doc = nlp(text)

    noun_sets = []
    for sent in doc.sents:
        gathering = []
        for chunk in sent.noun_chunks:
            if chunk.root.pos_ != 'PRON':
                start, end = (chunk.start + (1 if doc[chunk.start].pos_ == 'DET' else 0), chunk.end)
                gathering.append(doc[start:end])
        if gathering:
            noun_sets.append(gathering)

    noun_lookup = {}
    for phrase in noun_sets:
        for noun in phrase:
            noun_lookup[noun.text] = noun_lookup.get(noun.text, [])
            noun_lookup[noun.text].append(noun)

    edges = [
        tuple(x.text for x in edge)
        for phrase in noun_sets
        for edge in itertools.combinations(phrase, 2)
    ]
    G = nx.Graph(edges)
    central_nodes = sorted(nx.betweenness_centrality(G).items(), key=lambda x:x[1], reverse=True)

    top_nouns = []
    for word, score in central_nodes:
        top_nouns.append({
            'noun': word,
            'score': score,
            'intervals': [
                (doc[x.start].idx, doc[x.start].idx + len(doc[x.start:x.end].text))
                for x in noun_lookup[word]
            ],
        })

    return top_nouns
