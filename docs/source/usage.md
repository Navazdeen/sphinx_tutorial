# Usage

## Installation

**To install lumache:**
```console
(.venv) $ pip install lumache
```

## Creates recipes

To create a recipe, you can use {py:func}`lumache.get_random_ingredients` funxtion:

```{eval-rst}
.. autofunction:: lumache.get_random_ingredients(kind=None)

```

Sometimes error will be raised {py:exc}`lumache.InvalidKindError` if kind is invalid:
```{eval-rst}
.. autoexception:: lumache.InvalidKindError
```