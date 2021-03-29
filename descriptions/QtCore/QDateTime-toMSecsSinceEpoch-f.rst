.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: bd45b4d8993b999184bf39988b3e316d

Returns the datetime as the number of milliseconds that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (\ :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`).

On systems that do not support time zones, this function will behave as if local time were :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

The behavior for this function is undefined if the datetime stored in this object is not valid. However, for all valid dates, this function returns a unique value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setMSecsSinceEpoch`.
