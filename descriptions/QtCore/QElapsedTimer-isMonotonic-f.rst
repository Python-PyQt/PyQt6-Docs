.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: ()
    :digest: 1473f61304153b3648040f07bb1f84d6

Returns ``true`` if this is a monotonic clock, false otherwise. See the information on the different clock types to understand which ones are monotonic.

Since Qt 6.6, :sip:ref:`~PyQt6.QtCore.QElapsedTimer` uses ``std::chrono::steady_clock``, so this function now always returns true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.clockType`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType`.
