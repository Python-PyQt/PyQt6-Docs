.. sip:method-description::
    :status: todo
    :pysig: d4e4feedb68d2ec2d77985b5a70b5661
    :realsig: (QAnyStringView) const
    :digest: e609f1065ee3b5faa4ecf0cdf9db2096

Returns the length of the substring captured by the capturing group named *name*.

**Note:** This function returns 0 if the capturing group named *name* did not capture a string or doesn't exist.

**Note:** In Qt versions prior to 6.8, this function took QString or QStringView, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedEnd`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`.
