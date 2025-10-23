.. sip:method-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: () const
    :digest: ff8550b4e17be10caf8e1645fc3c24dd

Returns the font for this character format.

This function takes into account the format's font attributes (such as :sip:ref:`~PyQt6.QtGui.QTextCharFormat.fontWeight` and :sip:ref:`~PyQt6.QtGui.QTextCharFormat.fontPointSize`) and resolves them on top of the default font, defined as follows. If the format is part of a document, that is the document's default font. Otherwise the properties are resolved on top of a default constructed :sip:ref:`~PyQt6.QtGui.QFont`.

For example, if this format's font size hasn't been changed from the default font, :sip:ref:`~PyQt6.QtGui.QTextCharFormat.fontPointSize` returns 0, while ``font().pointSize()`` returns the actual size used for drawing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFont`, :sip:ref:`~PyQt6.QtGui.QTextDocument.defaultFont`.
