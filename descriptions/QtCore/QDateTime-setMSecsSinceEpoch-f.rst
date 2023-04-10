.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: dac03b741379c14533e26e7f31dae66a

Sets the datetime to represent a moment a given number, *msecs*, of milliseconds after the start, in UTC, of the year 1970.

On systems that do not support time zones, this function will behave as if local time were :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

Note that passing the minimum of ``qint64`` (``std::numeric_limits<qint64>::min()``) to *msecs* will result in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.toMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromMSecsSinceEpoch`.
