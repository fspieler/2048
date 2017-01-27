#!/usr/bin/env python2

import random
class LinearPath(object):
    def __init__(self, board, idx, mapper):
        self.board = board
        self.idx = idx
        self.mapper = mapper
    def __getitem__(self, idx):
        point = self.mapper(self.idx, idx)
        return self.board[point[0]][point[1]]
    def __setitem__(self, idx, val):
        point = self.mapper(self.idx, idx)
        self.board[point[0]][point[1]] = val

class Game(object):
    directions = ['up','down','left','right']
    def __init__(self,n=4,target=11,numInitialVals=2):
        """
        :param target: target end score is 2^target.. default 2^11 = 2048
        :param n: board is n by n squares
        """
        self.n = n
        self.board = [ [None] * n for i in xrange(n)]
        for i in xrange(numInitialVals):
            self._place_new_tile()

    def __str__(self):
        lines = []
        for line in self.board:
            lines.append("".join(["_" if x is None else str(x) for x in line]))
        return ("\n").join(lines)

    def __repr__(self):
        return self.__str__()

    def _emptySquares(self):
        ret = []
        for r, row in enumerate(self.board):
            for c, val in enumerate(row):
                if val is None:
                    ret.append((r,c))
        return ret

    def _random_empty_square(self,emptySquares=None):
        if emptySquares is None:
            emptySquares = self._emptySquares()
        return random.choice(emptySquares)

    def _place_new_tile(self,vals=[2,4]):
        newVal = random.choice(vals)
        emptySquares = self._emptySquares()
        if 0 < len(emptySquares):
            newSquare = self._random_empty_square(emptySquares)
            self.board[newSquare[0]][newSquare[1]] = newVal

    def _right(self, idx):
        return LinearPath(
            self.board,
            idx,
            lambda x, y: (x,len(self.board)-y-1)
        )

    def _left(self, idx):
        return LinearPath(
            self.board,
            idx,
            lambda x, y: (x,y)
        )

    def _down(self, idx):
        return LinearPath(
            self.board,
            idx,
            lambda x, y: (len(self.board)-y-1,x)
        )

    def _up(self, idx):
        return LinearPath(
            self.board,
            idx,
            lambda x, y: (y,x)
        )

    def _shift_nonempties_single_path(self, path):
        '''
        This looks quadratic because of nested while's but is actually linear
        because idx and shiftIdx can only move in one direction.
        '''
        idx = 0
        shiftIdx = 1
        while idx < len(self.board) and shiftIdx < len(self.board):
            if path[idx] is not None:
                idx += 1
            else:
                if shiftIdx <= idx:
                    shiftIdx = idx+1
                while shiftIdx < len(self.board):
                    if path[shiftIdx] is not None:
                        path[idx] = path[shiftIdx]
                        path[shiftIdx] = None
                        break
                    shiftIdx += 1

    def _combine_consecutive(self, path):
        idx = 0
        while idx < len(self.board)-1 and path[idx] is not None:
            if path[idx+1] == path[idx]:
                path[idx] *= 2
                path[idx+1] = None
                idx += 1
            idx += 1

    def move(self, direction):
        for i in xrange(len(self.board)):
            self._shift_nonempties_single_path(direction(i))
        for i in xrange(len(self.board)):
            self._combine_consecutive(direction(i))
        for i in xrange(len(self.board)):
            self._shift_nonempties_single_path(direction(i))
        self._place_new_tile()
