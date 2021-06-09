.. sip:method-description::
    :status: todo
    :pysig: 0779f122b0984a5b4ec9045fb49cd9d6
    :realsig: (int)
    :digest: 927f388eeab85826762824fce217858e

Tells the application to exit with a return code.

After this function has been called, the application leaves the main event loop and returns from the call to :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`. The :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec` function returns *returnCode*. If the event loop is not running, this function does nothing.

By convention, a *returnCode* of 0 means success, and any non-zero value indicates an error.

It's good practice to always connect signals to this slot using a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection`. If a signal connected (non-queued) to this slot is emitted before control enters the main event loop (such as before "int main" calls :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`), the slot has no effect and the application never exits. Using a queued connection ensures that the slot will not be invoked until after control enters the main event loop.

Note that unlike the C library function of the same name, this function *does* return to the caller -- it is event processing that stops.

Note also that this function is not thread-safe. It should be called only from the main thread (the thread that the :sip:ref:`~PyQt6.QtCore.QCoreApplication` object is processing events on). To ask the application to exit from another thread, either use :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit` or instead call this function from the main thread with QMetaMethod::invokeMethod().

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`.
