
import os
import matchlang

languages = {"da": "Danish", "de": "German", "el": "Greek", "en": "English", "es": "Spanish",
             "fi": "Finnish", "fr": "French", "it": "Italian", "nl": "Dutch", "pt": "Portuguese",
             "sv": "Swedish"}


def eval(model_path, test_path):
    """
    Evaluetes a model by comparing it to the files in test_path and checking if the language was guessed correctly. 
    @param: model_path: directory of the model
    @param: test_path:  directory of the test files
    """
    correct = 0
    incorrect = 0
    x = 0
    sent = test_path.split("-")
    word = sent[1]

    n_text = int(os.listdir(model_path)[0].split('-')[1])

    ngram_tester = matchlang.LangMatcher(
        model_path)

    for file in os.listdir(test_path):
        filesplit = file.split(".")
        suffix = filesplit[1]

        result = ngram_tester.recognize(
            test_path + r"/" + file, encoding="utf-8")

        for key in result:
            if key == languages[suffix]:
                print(file, "Guess: {}".format(key))
                correct += 1
            else:
                print(file, "Guess: {} ERROR: {}".format(
                    key, languages[suffix]))
                incorrect += 1

    print("{}-gram models for {}-word sentences: {} correct, {} incorrect".format(n_text,
                                                                                  word, correct, incorrect))


if __name__ == "__main__":
    eval("./models/2-200", "./datafiles/test/europarl-10")
    eval("./models/2-200", "./datafiles/test/europarl-30")
    eval("./models/2-200", "./datafiles/test/europarl-90")
    eval("./models/3-200", "./datafiles/test/europarl-10")
    eval("./models/3-200", "./datafiles/test/europarl-30")
    eval("./models/3-200", "./datafiles/test/europarl-90")
