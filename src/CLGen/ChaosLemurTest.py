#!/bin/python
#ChaosLemurConfigGeneratorTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaos as cl
import sys
import os
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class ChaosLemurTest(unittest.TestCase):

    def testTakeDownRandomNode(self):
        running_CL = cl.ChaosLemur()
        node_taken_down = running_CL.takeDownRandomNode()
        print "\nTaking down node %s..\n" % (node_taken_down)
        time.sleep(2)
        print "Table after takedown... \n"
        time.sleep(1)
        running_CL.showAliveIPRoute(node_taken_down)
        time.sleep(2)
        print "\nReversing all failures... \n"
        time.sleep(2)
        running_CL.reverseFailures()

if __name__ == '__main__':
    unittest.main()

