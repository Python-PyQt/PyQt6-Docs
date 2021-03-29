.. sip:method-description::
    :status: todo
    :pysig: a04d2855f9abbc11436e089eb4f6ec88
    :realsig: (QThread::Priority)
    :digest: f8e270f94fc2e1ea5b122e6176fcf945

This function sets the *priority* for a running thread. If the thread is not running, this function does nothing and returns immediately. Use :sip:ref:`~PyQt6.QtCore.QThread.start` to start a thread with a specific priority.

The *priority* argument can be any value in the ``QThread::Priority`` enum except for ``InheritPriority``.

The effect of the *priority* parameter is dependent on the operating system's scheduling policy. In particular, the *priority* will be ignored on systems that do not support thread priorities (such as on Linux, see http://linux.die.net/man/2/sched_setscheduler for more details).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.Priority.Priority`, :sip:ref:`~PyQt6.QtCore.QThread.priority`, :sip:ref:`~PyQt6.QtCore.QThread.start`.
