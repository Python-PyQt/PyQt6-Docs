.. sip:method-description::
    :status: todo
    :pysig: d4e4feedb68d2ec2d77985b5a70b5661
    :realsig: (QAnyStringView) const
    :digest: 1051796fa1df6e62d14a55d2b72d6045

Returns the offset inside the subject string corresponding to the starting position of the substring captured by the capturing group named *name*. If the capturing group named *name* did not capture a string or doesn't exist, returns -1.

**Note:** In Qt versions prior to 6.8, this function took QString or QStringView, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`.
