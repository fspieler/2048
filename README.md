# Simple Python 2048 game

Very simple, proof-of-concept.

How to play:

```python
>>> game = Game()
>>> game
____
____
_4__
___4
>>> game.move(game._up)
>>> game
_4_4
__4_
____
____
>>> game.move(game._up)
>>> game
_444
_2__
____
____
>>> game.move(game._right)
>>> game
_248
___2
____
____
>>> game.move(game._left)
>>> game
248_
2___
____
___2
>>> game.move(game._up)
>>> game
4482
____
____
2___
>>> game.move(game._left)
>>> game
882_
____
4___
2___
```
