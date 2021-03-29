.. sip:method-description::
    :status: todo
    :pysig: ca1e9ddbfa86b74a7894dfd90e3367e8
    :realsig: (int,int) const
    :digest: cdd5b64eab2ea10c377747b6e3209a7d

Returns the number of days in the given *month* of the given *year*.

Months are numbered consecutively, starting with 1 for the first month of each year. If *year* is ``Unspecified`` (its default, if not passed), the month's length in a normal year is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.maximumDaysInMonth`, :sip:ref:`~PyQt6.QtCore.QCalendar.minimumDaysInMonth`.
