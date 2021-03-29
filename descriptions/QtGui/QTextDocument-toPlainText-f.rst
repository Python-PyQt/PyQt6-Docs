.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 58f3c2644e6794764f0b62777f6d4e45

Returns the plain text contained in the document. If you want formatting information use a :sip:ref:`~PyQt6.QtGui.QTextCursor` instead.

This function returns the same as :sip:ref:`~PyQt6.QtGui.QTextDocument.toRawText`, but will replace some unicode characters with ASCII alternatives. In particular, no-break space (U+00A0) is replaced by a regular space (U+0020), and both paragraph (U+2029) and line (U+2028) separators are replaced by line feed (U+000A). If you need the precise contents of the document, use :sip:ref:`~PyQt6.QtGui.QTextDocument.toRawText` instead.

**Note:** Embedded objects, such as images, are represented by a Unicode value U+FFFC (OBJECT REPLACEMENT CHARACTER).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.toHtml`.
