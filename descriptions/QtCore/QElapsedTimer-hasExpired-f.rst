.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (qint64) const
    :digest: ec3e671955d2149d7293cfeaa3078ab8

Returns ``true`` if :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed` exceeds the given *timeout*, otherwise ``false``.

A negative *timeout* is interpreted as infinite, so ``false`` is returned in this case. Otherwise, this is equivalent to ``elapsed() > timeout``. You can do the same for a duration by comparing durationElapsed() to a duration timeout.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`.
