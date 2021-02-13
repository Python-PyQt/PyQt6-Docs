.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 9dea3e3915e51f90d428fc6c1ea464d4

Returns the code of the key that was pressed or released.

See :sip:ref:`~PyQt6.QtCore.Qt.Key` for the list of keyboard codes. These codes are independent of the underlying window system. Note that this function does not distinguish between capital and non-capital letters, use the :sip:ref:`~PyQt6.QtGui.QKeyEvent.text` function (returning the Unicode text the key generated) for this purpose.

A value of either 0 or :sip:ref:`~PyQt6.QtCore.Qt.Key.Key_unknown` means that the event is not the result of a known key; for example, it may be the result of a compose sequence, a keyboard macro, or due to key event compression.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_KeyCompression`.
