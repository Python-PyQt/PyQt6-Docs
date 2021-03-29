.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (const QString&) const
    :digest: 87cddce23d548ef40ae9f33a951bcd83

Returns the substring captured by the capturing group named *name*.

If the named capturing group *name* did not capture a string, or if there is no capturing group named *name*, returns a null QString.

.. seealso:: capturedView(), :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength`, QString::isNull().
