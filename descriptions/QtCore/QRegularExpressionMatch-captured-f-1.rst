.. sip:method-description::
    :status: todo
    :pysig: 6c5df4072896077791688531fc13e62e
    :realsig: (QAnyStringView) const
    :digest: 19b413cea88f992450c1b50c6e02a0eb

Returns the substring captured by the capturing group named *name*.

If the named capturing group *name* did not capture a string, or if there is no capturing group named *name*, returns a null QString.

**Note:** In Qt versions prior to 6.8, this function took QString or QStringView, not QAnyStringView.

.. seealso:: capturedView(), :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength`, QString::isNull().
