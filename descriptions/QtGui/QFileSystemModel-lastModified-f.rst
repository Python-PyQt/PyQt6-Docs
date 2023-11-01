.. sip:method-description::
    :status: todo
    :pysig: 8706187bfdbb6dd54729e49c5f636b9c
    :realsig: (const QModelIndex&) const
    :digest: 37001c735d762103020b4128fee71592

Returns the date and time (in local time) when *index* was last modified.

This is an overloaded function, equivalent to calling:

::

    lastModified(index, QTimeZone::LocalTime);

If *index* is invalid, a default constructed :sip:ref:`~PyQt6.QtCore.QDateTime` is returned.
