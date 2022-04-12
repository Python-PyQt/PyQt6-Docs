.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int) const
    :digest: 72000255ff12572d5d47314727989d94

Returns true if the *nth* capturing group captured something in the subject string, and false otherwise (or if there is no such capturing group).

**Note:** The implicit capturing group number 0 captures the substring matched by the entire pattern.

**Note:** Some capturing groups in a regular expression may not have captured anything even if the regular expression matched. This may happen, for instance, if a conditional operator is used in the pattern:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py

Similarly, a capturing group may capture a substring of length 0; this function will return ``true`` for such a capturing group.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.lastCapturedIndex`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasMatch`.
