.. sip:method-description::
    :status: todo
    :pysig: 851b74792d703d1281d06e84be3dbf88
    :realsig: (const QString&,QLocale::FormatType) const
    :digest: 021a23c3bc3127224ceae5d35384db31

Parses the time string given in *string* and returns the time. The format of the time string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.timeFormat`).

If the time could not be parsed, returns an invalid time.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.timeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`.
