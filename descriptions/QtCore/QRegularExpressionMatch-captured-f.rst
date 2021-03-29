.. sip:method-description::
    :status: todo
    :pysig: 2c284ed2dc4bcd82dfc181293d2cc8b2
    :realsig: (int) const
    :digest: a768530da7e45e02632775e7626ff31a

Returns the substring captured by the *nth* capturing group.

If the *nth* capturing group did not capture a string, or if there is no such capturing group, returns a null QString.

**Note:** The implicit capturing group number 0 captures the substring matched by the entire pattern.

.. seealso:: capturedView(), :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.lastCapturedIndex`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength`, QString::isNull().
