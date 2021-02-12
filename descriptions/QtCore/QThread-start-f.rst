.. sip:method-description::
    :status: todo
    :pysig: 16d2158e41b5abe2ad32038cef0ab9d3
    :realsig: (QThread::Priority)
    :digest: ef558089d267703575350d4e885c742e

Begins execution of the thread by calling :sip:ref:`~PyQt6.QtCore.QThread.run`. The operating system will schedule the thread according to the *priority* parameter. If the thread is already running, this function does nothing.

The effect of the *priority* parameter is dependent on the operating system's scheduling policy. In particular, the *priority* will be ignored on systems that do not support thread priorities (such as on Linux, see the `sched_setscheduler <http://linux.die.net/man/2/sched_setscheduler>`_ documentation for more details).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.run`, :sip:ref:`~PyQt6.QtCore.QThread.terminate`.
