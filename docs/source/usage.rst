Usage
=====

.. _installation:

Installation
------------

To use luseepy, go to the GitHub repo

.. code-block:: console

   (.venv) $ # commands here

Getting packages
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lusee.get_packages

The ``kind`` parameter should be either ``"python"`` or ``"c++"``.
Otherwise, :py:func:`lusee.get_random_ingredients` will raise an exception.

.. autoexception:: lusee.InvalidKindError

For example:

>>> import lusee
>>> lusee.get_packages()
['python', 's++']

