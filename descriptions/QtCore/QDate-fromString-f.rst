.. sip:method-description::
    :status: todo
    :pysig: 348e7d078ca50d1bea4477ed2779569b
    :realsig: (const QString&, Qt::DateFormat)
    :digest: f597ae6028d308b3866b1a1c86a73377

Returns the :sip:ref:`~PyQt6.QtCore.QDate` represented by the *string*, using the *format* given, or an invalid date if the string cannot be parsed.

Note for :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`: only English month names (e.g. "Jan" in short form or "January" in long form) are recognized.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`.
