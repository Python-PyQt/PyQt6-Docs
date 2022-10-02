.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 09f7190671ea875e8806cf7ee2675cce

This function returns the same as :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toRawText`, but will replace some unicode characters with ASCII alternatives. In particular, no-break space (U+00A0) is replaced by a regular space (U+0020), and both paragraph (U+2029) and line (U+2028) separators are replaced by line feed (U+000A). If you need the precise contents of the document, use :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toRawText` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toHtml`, :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toMarkdown`, :sip:ref:`~PyQt6.QtGui.QTextDocumentFragment.toRawText`.
