.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 829ad431f5d1341db4bc3eed837c02e2

Returns ``true`` if data can be read from the device; otherwise returns false. Use :sip:ref:`~PyQt6.QtCore.QIODevice.bytesAvailable` to determine how many bytes can be read.

This is a convenience function which checks if the OpenMode of the device contains the ReadOnly flag.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.openMode`, OpenMode.
