.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: f6672020d5afd688008d91b0d2b7fcd0

This signal is emitted when the application is about to quit the main event loop, e.g. when the event loop level drops to zero. This may happen either after a call to :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit` from inside the application or when the user shuts down the entire desktop session.

The signal is particularly useful if your application has to do some last-second cleanup. Note that no user interaction is possible in this state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`.
