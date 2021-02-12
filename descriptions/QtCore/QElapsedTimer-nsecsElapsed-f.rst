.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 7816eef57cfd7060ce26a1f6a4928878

Returns the number of nanoseconds since this :sip:ref:`~PyQt6.QtCore.QElapsedTimer` was last started.

Calling this function on a :sip:ref:`~PyQt6.QtCore.QElapsedTimer` that is invalid results in undefined behavior.

On platforms that do not provide nanosecond resolution, the value returned will be the best estimate available.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.start`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.restart`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.invalidate`.
