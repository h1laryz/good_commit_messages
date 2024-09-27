# Good commit messages

A plugin for [pre-commit](https://github.com/pre-commit/pre-commit) to verify commit messages.

## Allowed commit prefixes

* feat:
* fix:
* style:
* refactor:
* test:
* docs:
* chore:
* ci:
* build:
* revert:

## Usage example

To use this plugin you have to create .pre-commit-config.yaml in root of your project and add inside following strings:

```
repos:
-   repo: https://github.com/h1laryz/good_commit_messages
    rev: v1.0.0
    hooks:
    -   id: good-commit-messages
```
