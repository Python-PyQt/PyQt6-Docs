.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: bd9bd52849a12f971c8aa380da5ff4bb

Returns the Unicode text that this key generated.

The text is not limited to the printable range of Unicode code points, and may include control characters or characters from other Unicode categories, including QChar::Other_PrivateUse.

The text may also be empty, for example when modifier keys such as Shift, Control, Alt, and Meta are pressed (depending on the platform). The :sip:ref:`~PyQt6.QtGui.QKeyEvent.key` function will always return a valid value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_KeyCompression`.
