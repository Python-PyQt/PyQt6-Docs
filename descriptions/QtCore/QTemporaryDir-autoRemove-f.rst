.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: cc30a1ebceecd9faa9ba1ecfa29715d6

Returns ``true`` if the :sip:ref:`~PyQt6.QtCore.QTemporaryDir` is in auto remove mode. Auto-remove mode will automatically delete the directory from disk upon destruction. This makes it very easy to create your :sip:ref:`~PyQt6.QtCore.QTemporaryDir` object on the stack, fill it with files, do something with the files, and finally on function return it will automatically clean up after itself.

Auto-remove is on by default.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryDir.setAutoRemove`, :sip:ref:`~PyQt6.QtCore.QTemporaryDir.remove`.
