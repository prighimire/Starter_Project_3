import unittest
import sys

from boggle_solver import Boggle


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
    # ADD 4x4, 5x5, 6x6, 7x7...13x13, and LARGER Dictionaries
    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # testing on a 4X4 grid
    def test_4x4_grid(self):
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "Z", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get",
                      "net", "new", "newt", "prat",
                      "pry", "qua", "quart", "quartz",
                      "rat", "tar", "tarp", "ten",
                      "went", "wet", "arty", "not", "quar"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["ART", "EGO", "GENT", "GET", "NET",
                    "NEW", "NEWT", "PRAT", "PRY", "QUA",
                    "QUART", "QUARTZ", "RAT", "TAR", "TARP",
                    "TEN", "WENT", "WET", "QUAR"]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # testing on 7X7 grid
    def test_7x7_grid(self):
        grid = [
            ["H", "A", "R", "B", "O", "R", "S"],
            ["T", "R", "A", "V", "E", "L", "S"],
            ["W", "I", "N", "T", "E", "R", "S"],
            ["S", "N", "O", "W", "F", "A", "L"],
            ["B", "R", "I", "S", "K", "S", "L"],
            ["C", "O", "L", "D", "S", "E", "A"],
            ["B", "E", "A", "C", "H", "S", "S"]
        ]
        dictionary = ["harbor", "travels", "winter",
                      "snowfall", "brisk", "cold",
                      "beach", "seas"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["HARBOR", "WINTER", "COLD", "BEACH"]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_13x13_grid_no_words_found(self):
        """Test Boggle solver with a 13x13 grid and
        a dictionary where no words can be formed."""
        grid = [
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"],
            ["Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"],
            ["Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"],
            ["Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"],
            ["Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"],
            ["Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"],
            ["Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y"],
            ["X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X", "Y", "X"]
        ]

        dictionary = [
            "HELLO", "WORLD", "PYTHON", "UNITTEST",
            "OPENAI", "CHATGPT", "ALGORITHM", "DATA",
            "STRUCTURE", "FUNCTION", "VARIABLE", "CLASS"
        ]

        mygame = Boggle(grid, dictionary)
        solution = [word.upper() for word in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    # ADD MANY SIMPLE TEST CASES
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # testing when there is no word in dictionary
    # or no word is considered valid
    def test_EmptyDictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuite_Complete_Coverage(unittest.TestCase):

    # ADD MANY COMPLEXED TEST CASES
    # no words from the dictionary can be formed
    def test_NoWordsFromDictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["xyz", "mno", "pqr"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # only a few words can be formed from the dictionary
    def test_PartialWordsFromDictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "cfi", "xyz", "ghi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["ABC", "CFI", "GHI"]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # All words from the dictionary can be formed
    def test_AllWordsFromDictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "cfi", "beh", "def", "ghi", "adg", "aei", "ceg"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [word.upper() for word in solution]
        expected = ["ABC", "CFI", "BEH", "DEF", "GHI", "ADG", "AEI", "CEG"]
        solution_sorted = sorted(solution)
        expected_sorted = sorted(expected)
        self.assertEqual(expected_sorted, solution_sorted)


class TestSuite_Qu_and_St(unittest.TestCase):
    # Test case with grid containing both "QU" and "ST" as multi-letter cells
    def test_GridWithMultipleMultiLetterCellsValidWords(self):
        grid = [["St", "A", "R"], ["Qu", "E", "T"], ["F", "G", "H"]]
        dictionary = ["star", "start", "quest", "quiet", "rat", "hat", "set"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["STAR", "START", "QUEST", "RAT"]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # Test case with more complex words formed from "QU" and "ST"
    def test_GridWithMoreComplexWords(self):
        grid = [["St", "A", "R"], ["Qu", "E", "T"], ["F", "G", "H"]]
        dictionary = ["stqufgearth", "startequfgh", "star",
                      "start", "quest", "quiet", "rat", "hat", "set"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["STAR", "START", "QUEST", "RAT",
                    "STARTEQUFGH", "STQUFGEARTH"]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


if __name__ == '__main__':
    unittest.main()
