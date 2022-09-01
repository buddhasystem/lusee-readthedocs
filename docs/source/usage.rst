Usage
=====

.. _installation:

Installation
------------

To use luseepy, go to the GitHub repo

.. code-block:: console

   (.venv) $ # commands here

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"python"`` or ``"c++"``.
Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lusee.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

