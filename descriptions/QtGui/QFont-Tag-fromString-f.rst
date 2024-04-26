.. sip:method-description::
    :status: todo
    :pysig: f8248e216d915f7aaaecc465d21e292f
    :realsig: (QAnyStringView)
    :digest: 7de614e32fd9accc51f2818428d840a6

Returns a tag constructed from the string in *view*. The string must be exactly four characters long.

Returns ``std::nullopt`` if the input is not four characters long, or if the tag produced would be invalid.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont.Tag.isValid`, :sip:ref:`~PyQt6.QtGui.QFont.Tag.fromValue`.
