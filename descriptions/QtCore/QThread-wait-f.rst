.. sip:method-description::
    :status: todo
    :pysig: eff4c19c1c0348623fb90e84a4e9585e
    :realsig: (QDeadlineTimer)
    :digest: 5c79c972c915cecffebd617c5eb71785

Blocks the thread until either of these conditions is met:

* The thread associated with this :sip:ref:`~PyQt6.QtCore.QThread` object has finished execution (i.e. when it returns from :sip:ref:`~PyQt6.QtCore.QThread.run`). This function will return true if the thread has finished. It also returns true if the thread has not been started yet.

* The *deadline* is reached. This function will return false if the deadline is reached.

A deadline timer set to ``QDeadlineTimer::Forever`` (the default) will never time out: in this case, the function only returns when the thread returns from :sip:ref:`~PyQt6.QtCore.QThread.run` or if the thread has not yet started.

This provides similar functionality to the POSIX ``pthread_join()`` function.

**Note:** On some operating systems, this function may return true while the operating system thread is still running and may be executing clean-up code such as C++11 ``thread_local`` destructors. Operating systems where this function only returns true after the OS thread has fully exited include Linux, Windows, and Apple operating systems.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.sleep`, :sip:ref:`~PyQt6.QtCore.QThread.terminate`.
