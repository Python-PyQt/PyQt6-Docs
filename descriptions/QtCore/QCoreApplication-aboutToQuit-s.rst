.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 63f5359d8ee4b03a4d67110ebe98715f

This signal is emitted when the application is about to quit the main event loop, e.g. when the event loop level drops to zero. This may happen either after a call to :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit` from inside the application or when the user shuts down the entire desktop session.

The signal is particularly useful if your application has to do some last-second cleanup. Note that no user interaction is possible in this state.

**Note:** At this point the main event loop is still running, but will not process further events on return except :sip:ref:`~PyQt6.QtCore.QEvent.Type.DeferredDelete` events for objects deleted via deleteLater(). If event processing is needed, use a nested event loop or call :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents` manually.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`.
