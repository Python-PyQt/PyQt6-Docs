.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 6fb07945bb30b643e32ea3de46fbcb9c

Sets the hypertext link for the text format to the given *value*. This is typically a URL like "http://example.com/index.html".

The anchor will be displayed with the *value* as its display text; if you want to display different text call :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchorNames`.

To format the text as a hypertext link use :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchor`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat.anchorHref`.
