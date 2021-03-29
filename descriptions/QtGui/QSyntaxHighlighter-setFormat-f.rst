.. sip:method-description::
    :status: todo
    :pysig: 567a2a799642b0d3c6d64ebccb07fec8
    :realsig: (int,int,const QTextCharFormat&)
    :digest: d3843fab505ec97cff5c3a763260b91b

This function is applied to the syntax highlighter's current text block (i.e. the text that is passed to the :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.highlightBlock` function).

The specified *format* is applied to the text from the *start* position for a length of *count* characters (if *count* is 0, nothing is done). The formatting properties set in *format* are merged at display time with the formatting information stored directly in the document, for example as previously set with :sip:ref:`~PyQt6.QtGui.QTextCursor`'s functions. Note that the document itself remains unmodified by the format set through this function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.format`, :sip:ref:`~PyQt6.QtGui.QSyntaxHighlighter.highlightBlock`.
