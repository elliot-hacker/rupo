# -*- coding: utf-8 -*-
# Автор: Гусев Илья
# Описание: Тесты марковских цепей.

import os
import unittest

from rupo.generate.markov import MarkovModelContainer
from rupo.main.vocabulary import Vocabulary
from rupo.settings import EXAMPLES_DIR, MARKUP_XML_EXAMPLE


class TestMarkov(unittest.TestCase):
    def test_markov(self):
        vocab_dump_file = os.path.join(EXAMPLES_DIR, "vocab.pickle")
        markov_dump_file = os.path.join(EXAMPLES_DIR, "markov.pickle")
        vocabulary = Vocabulary(vocab_dump_file, MARKUP_XML_EXAMPLE)
        markov = MarkovModelContainer(markov_dump_file, vocabulary, MARKUP_XML_EXAMPLE)
        self.assertTrue(os.path.exists(vocab_dump_file))
        self.assertTrue(os.path.exists(markov_dump_file))
        os.remove(vocab_dump_file)
        os.remove(markov_dump_file)
        self.assertEqual(vocabulary.size(), len(markov.transitions))
        self.assertEqual(sum([sum(transition.values()) for transition in markov.transitions]), vocabulary.size()-1)