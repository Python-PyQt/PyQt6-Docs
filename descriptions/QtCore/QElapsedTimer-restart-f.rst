.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: 517a1e95db7ba1d51a07fe9945286901

Restarts the timer and returns the number of milliseconds elapsed since the previous start. This function is equivalent to obtaining the elapsed time with :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed` and then starting the timer again with :sip:ref:`~PyQt6.QtCore.QElapsedTimer.start`, but it does so in one single operation, avoiding the need to obtain the clock value twice.

Calling this function on a :sip:ref:`~PyQt6.QtCore.QElapsedTimer` that is invalid results in undefined behavior.

The following example illustrates how to use this function to calibrate a parameter to a slow operation (for example, an iteration count) so that this operation takes at least 250 milliseconds:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qelapsedtimer-main.py

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.start`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.invalidate`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.isValid`.
