"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    parameters
    ----------
    kind : list[str] or None
        Optional "kind" of ingredients

    Returns
    --------
    list[str]
        The ingredients lists.
    """
    return ["shells", "gorgonzola", "parsley"]
