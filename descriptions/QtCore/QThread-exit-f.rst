.. sip:method-description::
    :status: todo
    :pysig: 57b9a0dc5206eff9ee859f4714109c09
    :realsig: (int)
    :digest: 1dff29a4bba2f81f785e1e3154c901a2

Tells the thread's event loop to exit with a return code.

After calling this function, the thread leaves the event loop and returns from the call to :sip:ref:`~PyQt6.QtCore.QEventLoop.exec`. The :sip:ref:`~PyQt6.QtCore.QEventLoop.exec` function returns *returnCode*.

By convention, a *returnCode* of 0 means success, any non-zero value indicates an error.

Note that unlike the C library function of the same name, this function *does* return to the caller -- it is event processing that stops.

No QEventLoops will be started anymore in this thread until :sip:ref:`~PyQt6.QtCore.QThread.exec` has been called again. If the eventloop in :sip:ref:`~PyQt6.QtCore.QThread.exec` is not running then the next call to :sip:ref:`~PyQt6.QtCore.QThread.exec` will also return immediately.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.quit`, :sip:ref:`~PyQt6.QtCore.QEventLoop`.
