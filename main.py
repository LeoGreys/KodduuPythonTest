import unittest
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


def get_most_common_words(text, num_common_words):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    filtered_text = [word for word in word_tokens if not word in stop_words]

    word_counter = Counter(filtered_text)

    output_strings = []

    for word, count in word_counter.most_common(num_common_words):
        output_string = f'Слово "{word}" встречается {count} раз(а)'
        output_strings.append(output_string)

    return '\n'.join(output_strings)


class TestGetMostCommonWords(unittest.TestCase):
    expected_result = [
        'Слово "ipsum" встречается 4 раз(а)',
        'Слово "amet" встречается 2 раз(а)',
        'Слово "elit" встречается 2 раз(а)'
    ]

    def test_for_text_without_punctuation(self):
        text = "Lorem ipsum amet dolor ipsum elit sit amet ipsum, consectetur ipsum adipiscing elit."
        result = get_most_common_words(text, 3)
        self.assertListEqual(result.split('\n'), TestGetMostCommonWords.expected_result)

    # тест не пройдет, потому что get_most_common_words учитывает знаки препинания как слова
    def test_for_text_with_punctuation(self):
        text = "Lorem, amet, dolor, ipsum, elit. Sit amet. ipsum, consectetur. ipsum adipiscing. elit."
        result = get_most_common_words(text, 3)
        self.assertListEqual(result.split('\n'), TestGetMostCommonWords.expected_result)

    # тест не пройдет, потому что get_most_common_words не учитывает регистр одинаковых слов
    def test_for_text_with_case(self):
        text = "Lorem Ipsum Amet Dolor ipsum Elit Sit amet Ipsum, Consectetur ipsum Adipiscing elit."
        result = get_most_common_words(text, 3)
        self.assertListEqual(result.split('\n'), TestGetMostCommonWords.expected_result)


if __name__ == '__main__':
    unittest.main()
