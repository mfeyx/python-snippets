from base import log

@log(level="debug")
def hello(name: str = "world") -> None:
    """
    # Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    .. deprecated:: 1.6.0
          `ndobj_old` will be removed in NumPy 2.0.0, it is replaced by
          `ndobj_new` because the latter works also with array subclasses.

    .. hint::
        This is just a hint!

    example

        hello("james")



    Parameters
    ----------
    name : str : *world*
        Description of parameter `name`.

    Args:
        name: An open smalltable.Table instance.

    Returns:
        None

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
    print("hello " + name) # prints the name


hello("james")
