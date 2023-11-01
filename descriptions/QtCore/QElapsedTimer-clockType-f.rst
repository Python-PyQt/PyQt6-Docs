.. sip:method-description::
    :status: todo
    :pysig: c062876abd25171fbc65d23011cbad15
    :realsig: ()
    :digest: b43c56e408091c23119f55522864b483

Returns the clock type that this :sip:ref:`~PyQt6.QtCore.QElapsedTimer` implementation uses.

Since Qt 6.6, :sip:ref:`~PyQt6.QtCore.QElapsedTimer` uses ``std::chrono::steady_clock``, so the clock type is always :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.MonotonicClock`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.isMonotonic`.
