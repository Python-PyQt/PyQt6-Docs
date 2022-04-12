.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 3aceb258385bfb1c7534708784925286

Returns the index of the last capturing group that captured something, including the implicit capturing group 0. This can be used to extract all the substrings that were captured:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py
    :lines: 310-314

Note that some of the capturing groups with an index less than  could have not matched, and therefore captured nothing.

If the regular expression did not match, this function returns -1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasCaptured`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength`.
