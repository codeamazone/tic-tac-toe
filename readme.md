# Tic Tac Toe

Tic Tac Toe, or Xs and Os, for two players.

I programmed this game as part of the Python Developer Path by JetBrains Academy (https://hyperskill.org).

The first version was the beginners' project, the object-oriented version was part of an advanced project where you can choose between playing against the computer (easy or medium) or another user, or you could even watch the computer play against itself.

An unbeatable computer-player is yet to be built.

## How to play

Make sure you have Python 3 installed.

Fork/clone the repository and open the project folder in your shell.
Change into the tictactoe folder

```
cd tictactoe
```

### Choose which version you want to play:

### <i>Simple version</i>

```
python tictactoe_v1.py
```

Coordinates range from 1 to 3. Start counting in the bottom left, first count to the right, then to the top.
Take turns entering your coordinates on one line, separated by a space.

### <i>Advanced version</i>

```
python tictactoe_oop_v1.py
```

Possible commands: "start" or "exit".
If you choose "start", enter the mode you want to play in by adding the first and the second player after the "start" command, separated by spaces.

Options for players are: <i>user, easy, medium</i>.

#### Example:

```
start user medium
```

You can also let the computer play against itself or enter "user" twice to play against someone else or yourself.

Coordinates range from 1 to 3. Start counting in the top left, first count from top to bottom, then from left to right. Enter your coordinates on one line, separated by a space.
