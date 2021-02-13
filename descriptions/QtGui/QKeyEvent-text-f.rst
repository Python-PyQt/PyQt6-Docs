.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 50be0f403d948553f1305602c67b4dd5

Returns the Unicode text that this key generated.

Return values when modifier keys such as Shift, Control, Alt, and Meta are pressed differ among platforms and could return an empty string.

**Note:** :sip:ref:`~PyQt6.QtGui.QKeyEvent.key` will always return a valid value, independent of modifier keys.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_KeyCompression`.
