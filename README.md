# nouns

> Centering resonance analysis (CRA) is a new text analysis method that has
> broad scope and range and can be applied to large quantities of written text
> and transcribed conversation. It identifies discursively important words and
> represents these as a network, then uses structural properties of the network
> to index word importance. CRA networks can be directly visualized and can be
> scored for resonance with other networks to support a number of spatial
> analysis methods. (Steven R. Corman et al., 2002)

## Setup

```sh
$ poetry install
$ poetry run python -m spacy download en
$ poetry run python -m nouns
```

## Usage

This module expects a text document as input. You can run on one document to
compute central nouns, like this:

```sh
$ cat example.txt | poetry run python -m nouns
[
  {
    "noun": "Google",
    "score": 0.4908464955370267,
    "intervals": [
      [
        3186,
        3199
      ]
    ]
  },
  ...
```

Or you can pass it multiple documents to compute resonance:

```sh
$ poetry run python -m nouns file1.txt file2.txt
```
