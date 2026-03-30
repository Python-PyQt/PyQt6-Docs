.. sip:method-description::
    :status: todo
    :pysig: a0827794a76cf4ca473e3e5f98d4e241
    :realsig: (QAnyStringView) const
    :digest: 7e4256e2d4f8f04e5db080a45719e09d

Converts the first found header value of *name* to a :sip:ref:`~PyQt6.QtCore.QDateTime` object, following the standard HTTP date formats. If the header does not exist or contains an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`, returns ``std::nullopt``.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.setDateTimeValue`, dateTimeValues(QAnyStringView name), dateTimeValueAt(qsizetype i).
