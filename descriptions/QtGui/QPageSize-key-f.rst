.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: f6620bbaf789fd08eedb21ea2c0755c4

Returns the unique key of the page size.

By default this is the PPD standard mediaOption keyword for the page size, or the PPD custom format key. If the :sip:ref:`~PyQt6.QtGui.QPageSize` instance was obtained from a print device then this will be the key provided by the print device and may differ from the standard key.

If the :sip:ref:`~PyQt6.QtGui.QPageSize` is invalid then the key will be an empty string.

This key should never be shown to end users, it is an internal key only. For a human-readable name use :sip:ref:`~PyQt6.QtGui.QPageSize.name`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPageSize.name`.
