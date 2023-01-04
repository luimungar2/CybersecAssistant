"""
Scan Test Suite
Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import sys
import logging
import unittest
from unittest import TestCase
import sys
sys.path.insert(0, '/home/kali/Desktop/CybersecAssistant/scanner/')
from nmap import Scanner

class Testing(unittest.TestCase):
    def setUp(self):
        self.ip  = "127.0.0.1"
        self.file = "ejemplo.txt"
        self.pos_result = True
        self.neg_result = False
        self.scanner = Scanner(self.ip,self.file)

    def test_scan(self):
        ''' It should return True when the IP target is up, and False in other cases'''
        # check scan works
        self.assertEqual(self.scanner.scan_services(), self.pos_result)

    def test_read(self):
        ''' It should return True when the file is read'''
        #check the file is read
        self.assertEqual(self.scanner.analyze_results(), self.pos_result)
        

if __name__ == '__main__':
    unittest.main()