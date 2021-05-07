.. sip:method-description::
    :status: todo
    :pysig: d16f54dd241f1011d61fddb403fcd41f
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: f7eb4a0a03bb04aa810bcbb5e4fe59f0

This function overloads :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.

Processes pending events for the calling thread for *ms* milliseconds or until there are no more events to process, whichever is shorter.

Use of this function is discouraged. Instead, prefer to move long operations out of the GUI thread into an auxiliary one and to completely avoid nested event loop processing. If event processing is really necessary, consider using :sip:ref:`~PyQt6.QtCore.QEventLoop` instead.

Calling this function processes events only for the calling thread.

**Note:** Unlike the processEvents() overload, this function also processes events that are posted while the function runs.

**Note:** All events that were queued before the timeout will be processed, however long it takes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`, :sip:ref:`~PyQt6.QtCore.QTimer`, :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents`.
