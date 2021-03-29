.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 91b5fda42ca0d9325e8eb4588ce4f931

Returns the datetime as the number of seconds that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (\ :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`).

On systems that do not support time zones, this function will behave as if local time were :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

The behavior for this function is undefined if the datetime stored in this object is not valid. However, for all valid dates, this function returns a unique value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setSecsSinceEpoch`.
