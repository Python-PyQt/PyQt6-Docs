.. sip:method-description::
    :status: todo
    :pysig: 57b9a0dc5206eff9ee859f4714109c09
    :realsig: (int)
    :digest: 2ec05201f53c77272366d11f69554e81

Tells the event loop to exit with a return code.

After this function has been called, the event loop returns from the call to :sip:ref:`~PyQt6.QtCore.QEventLoop.exec`. The :sip:ref:`~PyQt6.QtCore.QEventLoop.exec` function returns *returnCode*.

By convention, a *returnCode* of 0 means success, and any non-zero value indicates an error.

Note that unlike the C library function of the same name, this function *does* return to the caller -- it is event processing that stops.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`, :sip:ref:`~PyQt6.QtCore.QEventLoop.quit`, :sip:ref:`~PyQt6.QtCore.QEventLoop.exec`.
