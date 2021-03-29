.. sip:method-description::
    :status: todo
    :pysig: 22e9355fa66f9a58af8f4ee6a81ff093
    :realsig: (const QString&,QLocale::FormatType) const
    :digest: b4aafad02336906a98eb3e0621b50575

Parses the date/time string given in *string* and returns the time. The format of the date/time string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`).

If the string could not be parsed, returns an invalid :sip:ref:`~PyQt6.QtCore.QDateTime`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateTimeFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`.
