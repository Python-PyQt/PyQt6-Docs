.. sip:method-description::
    :status: todo
    :pysig: 59ee54024b6c997b6352518b33c23f4f
    :realsig: (bool)
    :digest: b8c687cc69d559ad12f81cc3a8976123

Enables or disables termination of the current thread based on the *enabled* parameter. The thread must have been started by :sip:ref:`~PyQt6.QtCore.QThread`.

When *enabled* is false, termination is disabled. Future calls to :sip:ref:`~PyQt6.QtCore.QThread.terminate` will return immediately without effect. Instead, the termination is deferred until termination is enabled.

When *enabled* is true, termination is enabled. Future calls to :sip:ref:`~PyQt6.QtCore.QThread.terminate` will terminate the thread normally. If termination has been deferred (i.e. :sip:ref:`~PyQt6.QtCore.QThread.terminate` was called with termination disabled), this function will terminate the calling thread *immediately*. Note that this function will not return in this case.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.terminate`.
