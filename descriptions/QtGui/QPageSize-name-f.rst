.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 98e66bd535d39790379c2828852d2d9a

Returns a localized human-readable name for the page size.

If the :sip:ref:`~PyQt6.QtGui.QPageSize` instance was obtained from a print device then the name used is that provided by the print device. Note that a print device may not support the current default locale language.

If the :sip:ref:`~PyQt6.QtGui.QPageSize` is invalid then the name will be an empty string.
