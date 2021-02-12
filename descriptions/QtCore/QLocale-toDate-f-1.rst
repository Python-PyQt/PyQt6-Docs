.. sip:method-description::
    :status: todo
    :pysig: e371e8fc1e62696de05c9576e4b347ce
    :realsig: (const QString&,const QString&) const
    :digest: 55b153caf2aca07f0ad6168add6b4142

Parses the date string given in *string* and returns the date. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for information on the expressions that can be used with this function.

This function searches month names and the names of the days of the week in the current locale.

If the date could not be parsed, returns an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.dateFormat`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`.
