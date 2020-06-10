import unittest


def replace_punctuations_with_whitespace(text):
    word = (
        text.replace("'", " ")
        .replace(".", " ")
        .replace(":", " ")
        .replace(",", " ")
        .replace(";", " ")
    )
    if len(word) > 2 and word.endswith("es"):
        return word[:-2]
    if len(word) > 1 and word.endswith("s"):
        return word[:-1]
    return word


def normalize_word(word):
    return word.lower()


def count_words(words_list, exclude_words):
    word_count_dict = {}
    max_count = 0
    for word in words_list:
        word_normalized = normalize_word(word)
        if word_normalized not in exclude_words:
            if word_normalized not in word_count_dict:
                word_count_dict[word_normalized] = 1
            else:
                word_count_dict[word_normalized] += 1

            if word_count_dict[word_normalized] > max_count:
                max_count = word_count_dict[word_normalized]
    return word_count_dict, max_count


def retrieveMostFrequentlyUsedWords(helpText, wordsToExclude):
    words_list = replace_punctuations_with_whitespace(helpText).split()
    exclude_words = set(wordsToExclude)
    word_count_dict, max_count = count_words(words_list, exclude_words)
    result = []
    for key, value in word_count_dict.items():
        if value == max_count:
            result.append(key)
    return result


class TestWordCount(unittest.TestCase):
    def test_word_count1(self):
        self.assertCountEqual(
            retrieveMostFrequentlyUsedWords(
                "Rose is a flower red rose are flower", ["is", "are", "a"]
            ),
            ["flower", "rose"],
        )

    def test_word_count2(self):
        self.assertCountEqual(
            retrieveMostFrequentlyUsedWords(
                "Jack and Jill went to the market to buy bread and cheese."
                " Cheese is Jack's and Jill's favourite food",
                ["and", "he", "the", "to", "is"],
            ),
            ["cheese", "jack", "jill", "s"],
        )


if __name__ == "__main__":
    unittest.main()
