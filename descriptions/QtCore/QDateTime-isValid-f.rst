.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d3b50af9ca4c5181520a5b21f4848927

Returns ``true`` if both the date and the time are valid and they are valid in the current :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`, otherwise returns ``false``.

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` or :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then the date and time are checked to see if they fall in the Standard Time to Daylight-Saving Time transition hour, i.e. if the transition is at 2am and the clock goes forward to 3am then the time from 02:00:00 to 02:59:59.999 is considered to be invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.YearRange`, :sip:ref:`~PyQt6.QtCore.QDate.isValid`, :sip:ref:`~PyQt6.QtCore.QTime.isValid`.
