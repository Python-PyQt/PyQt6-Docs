.. sip:method-description::
    :status: todo
    :pysig: 8575cd542b930d3f2086c7593d54cd6a
    :realsig: (QEventLoop::ProcessEventsFlags,int)
    :digest: 941d24ee83e697f40bac46335d143c74

This function overloads :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.

Processes pending events for the calling thread for *ms* milliseconds or until there are no more events to process, whichever is shorter.

You can call this function occasionally when your program is busy doing a long operation (e.g. copying a file).

Calling this function processes events only for the calling thread.

**Note:** Unlike the processEvents() overload, this function also processes events that are posted while the function runs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`, :sip:ref:`~PyQt6.QtCore.QTimer`, :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents`.
