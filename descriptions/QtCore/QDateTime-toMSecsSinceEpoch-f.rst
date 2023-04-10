.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 7a3f443d7c1c8fd09f8c94f2205a0bda

Returns the datetime as a number of milliseconds after the start, in UTC, of the year 1970.

On systems that do not support time zones, this function will behave as if local time were :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

The behavior for this function is undefined if the datetime stored in this object is not valid. However, for all valid dates, this function returns a unique value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromMSecsSinceEpoch`.
