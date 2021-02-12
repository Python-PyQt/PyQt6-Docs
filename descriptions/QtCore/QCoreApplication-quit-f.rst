.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: 51530546a873079f3d1c28ffe79d791d

Asks the application to quit.

The request may be ignored if the application prevents the quit, for example if one of its windows can't be closed. The application can affect this by handling the :sip:ref:`~PyQt6.QtCore.QEvent.Type.Quit` event on the application level, or :sip:ref:`~PyQt6.QtCore.QEvent.Type.Close` events for the individual windows.

If the quit is not interrupted the application will exit with return code 0 (success).

To exit the application without a chance of being interrupted, call :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit` directly.

It's good practice to always connect signals to this slot using a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection`. If a signal connected (non-queued) to this slot is emitted before control enters the main event loop (such as before "int main" calls :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`), the slot has no effect and the application never exits. Using a queued connection ensures that the slot will not be invoked until after control enters the main event loop.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qcoreapplication.py
    :lines: 60-61

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.aboutToQuit`.
