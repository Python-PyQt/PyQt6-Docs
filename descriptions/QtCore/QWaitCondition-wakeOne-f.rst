.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: c00c107775a2821b23a08a7201208795

Wakes one thread waiting on the wait condition. The thread that is woken up depends on the operating system's scheduling policies, and cannot be controlled or predicted.

If you want to wake up a specific thread, the solution is typically to use different wait conditions and have different threads wait on different conditions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll`.
