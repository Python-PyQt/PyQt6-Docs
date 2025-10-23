.. sip:method-description::
    :status: todo
    :pysig: 26120c39397936c5c42b8dfeb190399c
    :realsig: (QAnyStringView) const
    :digest: 7e4256e2d4f8f04e5db080a45719e09d

Converts the first found header value of *name* to a :sip:ref:`~PyQt6.QtCore.QDateTime` object, following the standard HTTP date formats. If the header does not exist or contains an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`, returns ``std::nullopt``.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.setDateTimeValue`, dateTimeValues(QAnyStringView name), dateTimeValueAt(qsizetype i).
