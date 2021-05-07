.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 079e50134c5e2fbe4252cbe5d9a94af1

Returns ``true`` if data can be written to the device; otherwise returns false.

This is a convenience function which checks if the OpenMode of the device contains the WriteOnly flag.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.openMode`, OpenMode.
