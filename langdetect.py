import math
from collections import Counter


def prepare(text):
    """
    Returns a list of words in a string.
    Certain characters are replaced by whitespace, and the text is split based on whitespaces.
    @param: text: string (The text of which to return a wordlist)
    """
    badCharacters = ["!", "?", ",", ".", "\"", "(", ")", "<", ">"]
    splitText = [char for char in text]
    for i in range(len(splitText)):
        if splitText[i] in badCharacters:
            splitText[i] = " "
    wordString = ''.join(splitText)
    wordList = wordString.split()
    return wordList


def ngrams(seq, n=3):
    """
    Returns a list of n-grams in a string.
    @param: seq: string (The string for which n-grams must be returned)
    @param: n: int, default: 3 (Type of n-grams to return)
    """
    #! Dit moet makkelijker kunnen
    ngramList = []
    for i in range(len(seq) - (n-1)):
        ngram = ""
        for j in range(n):
            ngram += seq[i + j]
        ngramList.append(ngram)
    return ngramList


def ngram_table(text, n=3, limit=0):
    """
    Returns a table of a text's n-grams and their counts, sorted by their counts.
    @param: text: string (The text for which to make an n-gram table)
    @param: n: int (The type of n-gram)
    @param: limit: int (The maximum amount of n-grams in the returned table)
    """
    Tlist = prepare(text)
    foundNgrams = {}
    for element in Tlist:
        element = ('<' + element + '>')
        ngramList = ngrams(element, n)
        for ngram in ngramList:
            if ngram in foundNgrams:
                foundNgrams[ngram] += 1
            else:
                foundNgrams[ngram] = 1
    sortedNgrams = {}
    teller = 0
    for k, v in sorted(foundNgrams.items(), reverse=True, key=lambda x: x[1]):
        if teller < limit or limit == 0:
            sortedNgrams[k] = v
            teller += 1
    return sortedNgrams


def write_ngrams(table, filename):
    """
    Writes the contents of an n-gram table to a file.
    @param: table: dict (The n-gram table to write to a file)
    @param: filename: string (The name of the file to write to)
    """
    with open(filename, "w", encoding="utf8") as conn:
        for line in table:
            conn.write(str(table[line]))
            conn.write(" ")
            conn.write(str(line))
            conn.write("\n")


def read_ngrams(filename):
    """
    Reads a file and returns an n-gram table with the n-grams and counts in the file.
    @param: filename: string (The name of the file from which to read)
    """
    with open(filename, encoding="utf8") as conn:
        alltext = conn.read()
    splitText = alltext.splitlines()
    table = {}
    for line in splitText:
        splitLine = line.split()
        table[splitLine[1]] = int(splitLine[0])
    return table


def cosine_similarity(table1, table2):
    """
    Calculates and returns the cosine similarity between two tables of n-grams
    @param: table1: dict (The first table to compare)
    @param: table2: dict (The second table to compare)
    """
    a = Counter(table1)
    b = Counter(table2)
    termen = set(a).union(b)
    product = sum(a.get(k, 0) * b.get(k, 0) for k in termen)
    berekeningA = math.sqrt(sum(a.get(k, 0)**2 for k in termen))
    berekeningB = math.sqrt(sum(b.get(k, 0)**2 for k in termen))
    return product / (berekeningA * berekeningB)
