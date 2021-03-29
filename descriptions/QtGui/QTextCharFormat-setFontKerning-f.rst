.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: c040ce46054908355bdae901e75e4a8d

Enables kerning for this font if *enable* is true; otherwise disables it.

When kerning is enabled, glyph metrics do not add up anymore, even for Latin text. In other words, the assumption that width('a') + width('b') is equal to width("ab") is not neccesairly true.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat.fontKerning`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFont`.
