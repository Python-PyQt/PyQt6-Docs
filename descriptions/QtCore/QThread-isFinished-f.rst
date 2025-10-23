.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ce454dc14a583e15c58029fd63d1fb24

Returns ``true`` if the thread is finished; otherwise returns ``false``.

A thread is considered finished if it has returned from the :sip:ref:`~PyQt6.QtCore.QThread.run` function and the :sip:ref:`~PyQt6.QtCore.QThread.finished` signal has been emitted.

Note the thread may still run for arbitrary amount of time after the :sip:ref:`~PyQt6.QtCore.QThread.finished` signal is emitted, running clean-up operations such as executing the destructors to ``thread_local`` variables. To synchronize with all effects from the thread, call :sip:ref:`~PyQt6.QtCore.QThread.wait` and verify it returned true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.isRunning`.
