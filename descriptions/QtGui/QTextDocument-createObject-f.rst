.. sip:method-description::
    :status: todo
    :pysig: 8745625bdfd9891b7f25d1566c723e8f
    :realsig: (const QTextFormat&)
    :digest: 79e36f1f8af1a00a2855059c504e18fe

Creates and returns a new document object (a :sip:ref:`~PyQt6.QtGui.QTextObject`), based on the given *format*.

QTextObjects will always get created through this method, so you must reimplement it if you use custom text objects inside your document.
