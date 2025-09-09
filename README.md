# Welcome to my Projects Website!

This repository holds the source code for the website, which uses plain HTML/CSS/JS and a Flask backend (PostgreSQL DB). The source code for each of my projects is also available in this repository, with specific implementation details being left out on some games to ensure they are not reproduced. Each project is also available separately on my Github profile.

A full list of each project, ordered by date of completion, is available below:

| Date | Title | Brief Description |
| ----------- | ----------- | ----------- |
| 7/5/25 | Website Homepage | The index page offers navigation to each project, with each being displayed in a grid-like manner. Users may choose to login to save statistics when interacting with different projects. |
| 9/9/25 | Lasker Morris Game | Lasker Morris is very similar to the game *Nine Men's Morris*, and is in the middle of Tic Tac Toe and Chess in terms of complexity. I developed an AI player using a modified Minimax alpha/beta algorithm which plays at a near perfect level (it may be possible to beat, I have only managed to stalemate it!). |

If you wish to clone the repository to use for offline use, simply install the requirements using `pip` (ensure you are using Python 3.9 or newer!):

```
pip install -r requirements.txt
```

To run, use
```
flask run
```
Please note that API keys, along with a few files (as mentioned earlier) are not included in the repository. Most projects should still work as intended; in the above table, projects requiring API keys are marked with `[K]` and projects with hidden files are marked with `[F]`.

If you spot any errors in the website or any of the projects' source code, or wish to contact me for any other reason, you can reach me at <asabramson@outlook.com>!