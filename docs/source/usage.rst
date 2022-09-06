Usage
======================

.. _installation:

Installation
------------

To use luseepy, go to the GitHub repo

.. code-block:: console

   (.venv) $ # commands here

Getting packages
----------------

To retrieve a list of random ingredients,
you can use the ``lusee.get_packages()`` function:

.. autofunction:: lusee.get_packages

The ``kind`` parameter should be either ``"python"`` or ``"c++"``.
Otherwise, :py:func:`lusee.get_packages` will raise an exception.

.. autoexception:: lusee.InvalidKindError

For example:

>>> import lusee
>>> lusee.get_packages()
['python', 'c++']


.. autofunction:: lusee.return_true

Misc
----

Expandability.
