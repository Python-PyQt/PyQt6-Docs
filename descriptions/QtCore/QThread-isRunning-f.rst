.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 382c8f644d742a03078032ad8eef1794

Returns ``true`` if the thread is running; otherwise returns ``false``.

A thread is considered to be running if :sip:ref:`~PyQt6.QtCore.QThread` has been started with :sip:ref:`~PyQt6.QtCore.QThread.start` but is not yet finished.

Note the thread may still run for arbitrary amount of time after the :sip:ref:`~PyQt6.QtCore.QThread.finished` signal is emitted, running clean-up operations such as executing the destructors to ``thread_local`` variables. To synchronize with all effects from the thread, call :sip:ref:`~PyQt6.QtCore.QThread.wait` and verify it returned true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.isFinished`.
