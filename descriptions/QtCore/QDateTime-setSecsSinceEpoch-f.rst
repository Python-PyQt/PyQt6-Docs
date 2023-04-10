.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 861711b6569e7df4de26ebb18f800288

Sets the datetime to represent a moment a given number, *secs*, of seconds after the start, in UTC, of the year 1970.

On systems that do not support time zones, this function will behave as if local time were :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.toSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromSecsSinceEpoch`.
