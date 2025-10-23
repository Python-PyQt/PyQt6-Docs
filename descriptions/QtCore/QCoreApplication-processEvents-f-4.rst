.. sip:method-description::
    :status: todo
    :pysig: 24c661348e7a5a8ebe8b239d46db7926
    :realsig: (QEventLoop::ProcessEventsFlags, QDeadlineTimer)
    :digest: e35f57aad7cab2504e0e7eb215dc7ea7

Processes pending events for the calling thread untile *deadline* has expired, or until there are no more events to process, whichever happens first.

Use of this function is discouraged. Instead, prefer to move long operations out of the GUI thread into an auxiliary one and to completely avoid nested event loop processing. If event processing is really necessary, consider using :sip:ref:`~PyQt6.QtCore.QEventLoop` instead.

Calling this function processes events only for the calling thread.

**Note:** Unlike the processEvents() overload, this function also processes events that are posted while the function runs.

**Note:** All events that were queued before the timeout will be processed, however long it takes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`, :sip:ref:`~PyQt6.QtCore.QTimer`, QChronoTimer, :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents`.
