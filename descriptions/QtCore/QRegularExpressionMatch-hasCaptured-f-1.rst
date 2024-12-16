.. sip:method-description::
    :status: todo
    :pysig: 469c3d5de45760d2e753a158b05ea5cb
    :realsig: (QAnyStringView) const
    :digest: cac9c11d0300821c69125094fa2f6951

Returns true if the capturing group named *name* captured something in the subject string, and false otherwise (or if there is no capturing group called *name*).

**Note:** Some capturing groups in a regular expression may not have captured anything even if the regular expression matched. This may happen, for instance, if a conditional operator is used in the pattern:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qregularexpression.py

Similarly, a capturing group may capture a substring of length 0; this function will return ``true`` for such a capturing group.

**Note:** In Qt versions prior to 6.8, this function took QString or QStringView, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasMatch`.
