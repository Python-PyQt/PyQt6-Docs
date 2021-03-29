.. sip:method-description::
    :status: todo
    :pysig: bde832d4e99f6c9ce7d868e858303a6a
    :realsig: (const QString&,QLocale::FormatType) const
    :digest: d28f335051456513389f28b2b755f8d3

Parses the date string given in *string* and returns the date. The format of the date string is chosen according to the *format* parameter (see :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`).

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
