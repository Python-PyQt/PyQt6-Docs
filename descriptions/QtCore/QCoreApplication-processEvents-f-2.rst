.. sip:method-description::
    :status: todo
    :pysig: 7455a82fef3e9d8cd24d18e2f6076c4a
    :realsig: (QEventLoop::ProcessEventsFlags)
    :digest: d3c5992bc4f12715153c96842c261e73

Processes some pending events for the calling thread according to the specified *flags*.

Use of this function is discouraged. Instead, prefer to move long operations out of the GUI thread into an auxiliary one and to completely avoid nested event loop processing. If event processing is really necessary, consider using :sip:ref:`~PyQt6.QtCore.QEventLoop` instead.

In the event that you are running a local loop which calls this function continuously, without an event loop, the :sip:ref:`~PyQt6.QtCore.QEvent.Type.DeferredDelete` events will not be processed. This can affect the behaviour of widgets, e.g. :sip:ref:`~PyQt6.QtWidgets.QToolTip`, that rely on :sip:ref:`~PyQt6.QtCore.QEvent.Type.DeferredDelete` events to function properly. An alternative would be to call :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendPostedEvents` from within that local loop.

Calling this function processes events only for the calling thread, and returns after all available events have been processed. Available events are events queued before the function call. This means that events that are posted while the function runs will be queued until a later round of event processing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`, :sip:ref:`~PyQt6.QtCore.QTimer`, QChronoTimer, :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.sendPostedEvents`.
