.. sip:method-description::
    :status: todo
    :pysig: 1161c2c0c17925334c912c505247fbaa
    :realsig: (QAnyStringView) const
    :digest: ad480213fbe495155c470b98371b59ce

Returns the offset inside the subject string immediately after the ending position of the substring captured by the capturing group named *name*. If the capturing group named *name* did not capture a string or doesn't exist, returns -1.

**Note:** In Qt versions prior to 6.8, this function took QString or QStringView, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedStart`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.capturedLength`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.captured`.
