import os
import langdetect
import sys


class LangMatcher:
    """
    A class that can compare a testfile with language profiles in a folder and give them
    similarity scores. It can also determine the best matching language, i.e. the one with the highest score
    """

    def __init__(self, directory):
        """
        The initializer for the LangMatch class.
        @param directory: (string) location of the profiles
        """
        self.profiles = {}

        # Limit and n are determined by the first file in the directory as they will be the same for all the files
        self.limit = int(os.listdir(directory)[0].split('-')[2])
        self.n = int(os.listdir(directory)[0].split('-')[1])

        for file in os.listdir(directory):
            language = file.split('-')[0]
            ngramtable = langdetect.read_ngrams(directory + r"/" + file)
            self.profiles[language] = ngramtable

    def score(self, text, k_best=1):
        """
        A function to calculate similaruty scores for a given text and language profiles. Text is converted into n-grams of appropriate size and limit.
        The cosine similarity between that n-gram and the each of the language profiles are determined.
        Returns a dictionary of language profiles and their scores, sorted by score.
        @param text: (string) The text for which to calculate scores
        @param k_best=1: (int) The limit of scores to return, default 1.
        """
        ngramTable = langdetect.ngram_table(text, n=self.n, limit=self.limit)
        scores = {}

        for language in self.profiles:
            ngramCompared = self.profiles[language]
            score = langdetect.cosine_similarity(ngramTable, ngramCompared)
            scores[language] = score

        returnedScores = {}
        teller = 0
        for language, score in sorted(scores.items(), reverse=True, key=lambda x: x[1]):
            if teller < k_best:
                returnedScores[language] = score
                teller += 1

        return returnedScores

    def recognize(self, filename, encoding="utf-8"):
        """
        This function takes a file and returns the language with the highest similarity score.
        @param filename: (string) The file in which the text to compare is located.
        @param encoding=utf-8: (string) The type of encoding of the file.
        """
        with open(filename, encoding=encoding) as conn:
            alldata = conn.read()
        return self.score(alldata)


if __name__ == "__main__":
    NumOfArgs = len(sys.argv)

    modelDirectory = sys.argv[1]

    profiles = LangMatcher(modelDirectory)

    for i in range(2, NumOfArgs):
        filename = sys.argv[i].split(r"/")[-1]
        result = profiles.recognize(sys.argv[i])

        for x in result:
            score = result[x]
            match = x

        print("Filename: {}\n\tMost similar language: {}\n\tScore: {}".format(
            filename, match, score))
