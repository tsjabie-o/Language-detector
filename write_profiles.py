import langdetect
import os


def make_profiles(datafolder, n, limit):
    """
    A function that creates language profiles based on training texts. The profiles are n-gram models.
    @param datafolder: (string) the folder with training texts to base profiles on
    @param n: (int) the type of n-gram
    @param limit: (int) the limit of n-grams per profile
    """
    for file in os.listdir(datafolder):
        filenameSplit = file.split('-')
        language = filenameSplit[0]
        fileEncoding = filenameSplit[1]
        with open(datafolder + r"/" + file, encoding=fileEncoding) as conn:
            alldata = conn.read()
        ngramtable = langdetect.ngram_table(alldata, n, limit)
        try:
            os.makedirs("models/{}-{}".format(n, limit))
        except FileExistsError:
            pass
        langdetect.write_ngrams(
            ngramtable, "models/{}-{}/{}-{}-{}".format(n, limit, language, n, limit))


if __name__ == "__main__":
    make_profiles("./datafiles/training", 3, 200)
    make_profiles("./datafiles/training", 2, 200)
