import os
import unittest

def analyze_text(filename):
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        #return sum(1 for _ in f)
        for line in f:
            lines += 1
            chars += len(line)

    return (lines, chars)

class TrxtAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""

        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war,\n'
                    'testing whether that nation,\n' 
                    'or any nation, so conceived, and so dedicated, can long endure.\n' 
                    'We are met here on a great battlefield of that war.\n' 
                    'We have come to dedicate a portion of it as a final resting place for those who here gave their lives that that nation might live.')

    def tearDown(self):
        """Fixture that deletes the file used in the tests."""
        try:
            os.remove(self.filename)
        except:
            pass # eat an exception for the test file

    def test_function_runs(self):
        """Basic smoke test: does the function run"""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check the line count"""
        self.assertEqual(analyze_text(self.filename)[0], 5)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 316)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function does not delete the file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

unittest.main()
