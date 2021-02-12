.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (qint64) const
    :digest: 4ceafbb0fe7e6797ea9dfb010309ef0a

Returns ``true`` if this :sip:ref:`~PyQt6.QtCore.QElapsedTimer` has already expired by *timeout* milliseconds (that is, more than *timeout* milliseconds have elapsed). The value of *timeout* can be -1 to indicate that this timer does not expire, in which case this function will always return false.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`.
