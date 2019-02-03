# Data Engineer challenge

## Description
This is meant to solve the data engineer challenge.

## Install git client Hooks

1. Open with a terminal and execute
```bash
$ git config core.hooksPath git-hooks
```

The command above set git to use hooks saved in `git-hooks` instead of the default `.git/hooks/`.
This installation is required because [git doesn't track git client hooks.](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)


## Installation and Requirements

Python 3.6:
```
pip install -r requirements.txt
```