.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 97ff92d0fbc13b9df2e46676d12bb2e3

Returns ``true`` if the :sip:ref:`~PyQt6.QtCore.QTemporaryFile` is in auto remove mode. Auto-remove mode will automatically delete the filename from disk upon destruction. This makes it very easy to create your :sip:ref:`~PyQt6.QtCore.QTemporaryFile` object on the stack, fill it with data, read from it, and finally on function return it will automatically clean up after itself.

Auto-remove is on by default.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.setAutoRemove`, remove().
