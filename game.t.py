#!/usr/bin/env python2

import unittest
from game import Game

class GameTest(unittest.TestCase):
    def assertDirectionEqual(self,vals,direction):
        for idx, val in enumerate(vals):
            self.assertEqual(val, direction[idx])

    def testShiftingNonEmptyTiles(self):
        game = Game(6)
        game.board = [[1,None,None,2,None,None],\
                      [None,None,None,None,None,3],\
                      [4,5,6,7,8,9],\
                      [3,3,None,None,3,3],\
                      [None,1,None,2,None,3],\
                      [1,2,3,None,None,None]]
        game._shift_nonempties_single_path(game._left(0))
        self.assertDirectionEqual([1,2,None,None,None,None],game._left(0))

        game._shift_nonempties_single_path(game._left(1))
        self.assertDirectionEqual([3,None,None,None,None,None],game._left(1))

        game._shift_nonempties_single_path(game._left(2))
        self.assertDirectionEqual([4,5,6,7,8,9],game._left(2))

        game._shift_nonempties_single_path(game._left(3))
        self.assertDirectionEqual([3,3,3,3,None,None],game._left(3))

        game._shift_nonempties_single_path(game._left(4))
        self.assertDirectionEqual([1,2,3,None,None,None],game._left(4))

        game._shift_nonempties_single_path(game._left(5))
        self.assertDirectionEqual([1,2,3,None,None,None],game._left(5))

    def test_combine_consecutive(self):
        game = Game()
        game.board = [[2,2,2,2],\
                      [3,3,2,2],\
                      [5,5,10,None],\
                      [1,2,3,4]]
        game._combine_consecutive(game._left(0))
        self.assertDirectionEqual([4,None,4,None],game._left(0))

        game._combine_consecutive(game._left(1))
        self.assertDirectionEqual([6,None,4,None],game._left(1))

        game._combine_consecutive(game._left(2))
        self.assertDirectionEqual([10,None,10,None],game._left(2))

        game._combine_consecutive(game._left(3))
        self.assertDirectionEqual([1,2,3,4],game._left(3))

class LinearDirectionTest(unittest.TestCase):
    def assertDirectionEqual(self,vals,direction):
        for idx, val in enumerate(vals):
            self.assertEqual(val, direction[idx])
    def testRight(self):
        game = Game()
        game.board = \
                [[1, 2, 3 ,4], \
                 [5, 6, 7 ,8],\
                 [9, 10,11,12],\
                 [13,14,15,16]]
        self.assertDirectionEqual([4,3,2,1],game._right(0))
        self.assertDirectionEqual([8,7,6,5],game._right(1))
        self.assertDirectionEqual([12,11,10,9],game._right(2))
        self.assertDirectionEqual([16,15,14,13],game._right(3))
    def testLeft(self):
        game = Game()
        game.board = \
                [[1, 2, 3 ,4], \
                 [5, 6, 7 ,8],\
                 [9, 10,11,12],\
                 [13,14,15,16]]
        self.assertDirectionEqual([1,2,3,4],game._left(0))
        self.assertDirectionEqual([5,6,7,8],game._left(1))
        self.assertDirectionEqual([9,10,11,12],game._left(2))
        self.assertDirectionEqual([13,14,15,16],game._left(3))
    def testDown(self):
        game = Game()
        game.board = \
                [[1, 2, 3 ,4], \
                 [5, 6, 7 ,8],\
                 [9, 10,11,12],\
                 [13,14,15,16]]
        self.assertDirectionEqual([13,9,5,1],game._down(0))
        self.assertDirectionEqual([14,10,6,2],game._down(1))
        self.assertDirectionEqual([15,11,7,3],game._down(2))
        self.assertDirectionEqual([16,12,8,4],game._down(3))
    def testUp(self):
        game = Game()
        game.board = \
                [[1, 2, 3 ,4], \
                 [5, 6, 7 ,8],\
                 [9, 10,11,12],\
                 [13,14,15,16]]
        self.assertDirectionEqual([1,5,9,13],game._up(0))
        self.assertDirectionEqual([2,6,10,14],game._up(1))
        self.assertDirectionEqual([3,7,11,15],game._up(2))
        self.assertDirectionEqual([4,8,12,16],game._up(3))

if __name__ == '__main__':
    unittest.main()
