.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b7f62f5576c0205f4acf84e85763b0f7

Terminates the execution of the thread. The thread may or may not be terminated immediately, depending on the operating system's scheduling policies. Use :sip:ref:`~PyQt6.QtCore.QThread.wait` after , to be sure.

When the thread is terminated, all threads waiting for the thread to finish will be woken up.

**Warning:** This function is dangerous and its use is discouraged. The thread can be terminated at any point in its code path. Threads can be terminated while modifying data. There is no chance for the thread to clean up after itself, unlock any held mutexes, etc. In short, use this function only if absolutely necessary.

Termination can be explicitly enabled or disabled by calling :sip:ref:`~PyQt6.QtCore.QThread.setTerminationEnabled`. Calling this function while termination is disabled results in the termination being deferred, until termination is re-enabled. See the documentation of :sip:ref:`~PyQt6.QtCore.QThread.setTerminationEnabled` for more information.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.setTerminationEnabled`.
