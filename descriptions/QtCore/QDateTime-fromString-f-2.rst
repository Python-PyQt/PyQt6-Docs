.. sip:method-description::
    :status: todo
    :pysig: a81abec3e84d3c79f493f2f85f401b84
    :realsig: (const QString&, Qt::DateFormat)
    :digest: 4b5a9be6742e2e04ce32399a68569a50

Returns the :sip:ref:`~PyQt6.QtCore.QDateTime` represented by the *string*, using the *format* given, or an invalid datetime if this is not possible.

Note for :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`: only English short month names (e.g. "Jan" in short form or "January" in long form) are recognized.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toString`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`.
