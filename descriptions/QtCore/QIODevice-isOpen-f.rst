.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: a8c0d25e82557198bebc542f8136fbe3

Returns ``true`` if the device is open; otherwise returns ``false``. A device is open if it can be read from and/or written to. By default, this function returns ``false`` if :sip:ref:`~PyQt6.QtCore.QIODevice.openMode` returns ``NotOpen``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.openMode`, OpenMode.
