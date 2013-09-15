#!/usr/local/bin/python3

import re
import unittest
import extractURIsFromTweets

class TestExtractURIsFromTweets(unittest.TestCase):

    def test_extractURIFromLine(self):

        line = "sometext http://example.com/something?myvar=val&s=1 more text"

        expected = [ "http://example.com/something?myvar=val&s=1" ]

        actual = extractURIsFromTweets.extractURIsFromLine(line)

        self.assertEqual(expected, actual)

    def test_extractURIFromLine2(self):

        line = """sometext http://example.com/something?myvar=val&s=1
            stuff http://twit.po/AEREBE
            more text"""

        expected = [ "http://example.com/something?myvar=val&s=1", "http://twit.po/AEREBE" ]

        actual = extractURIsFromTweets.extractURIsFromLine(line)

        self.assertEqual(expected, actual)

    def test_extractURIFromLine3(self):

        line = "sometext http://example.com/something?myvar=val&s=1"

        expected = [ "http://example.com/something?myvar=val&s=1" ]

        actual = extractURIsFromTweets.extractURIsFromLine(line)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
