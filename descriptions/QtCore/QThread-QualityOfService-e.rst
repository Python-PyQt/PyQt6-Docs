.. sip:enum-description::
    :status: todo
    :digest: cb7eeef3990570fb45e90c5755c77681

This enum describes the quality of service level of a thread, and provides the scheduler with information about the kind of work that the thread performs. On platforms with different CPU profiles, or with the ability to clock certain cores of a CPU down, this allows the scheduler to select or configure a CPU core with suitable performance and energy characteristics for the thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.Priority.Priority`, :sip:ref:`~PyQt6.QtCore.QThread.serviceLevel`, :sip:ref:`~PyQt6.QtCore.QThreadPool.serviceLevel`.
