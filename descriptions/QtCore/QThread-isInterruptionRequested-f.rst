.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 24ce8bd829fd2da97c515b13bb3af423

Return true if the task running on this thread should be stopped. An interruption can be requested by :sip:ref:`~PyQt6.QtCore.QThread.requestInterruption`.

This function can be used to make long running tasks cleanly interruptible. Never checking or acting on the value returned by this function is safe, however it is advisable do so regularly in long running functions. Take care not to call it too often, to keep the overhead low.

::

    void long_task() {
         forever {
            if ( QThread::currentThread()->isInterruptionRequested() ) {
                return;
            }
        }
    }

**Note:** This can only be called within the thread itself, i.e. when it is the current thread.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.currentThread`, :sip:ref:`~PyQt6.QtCore.QThread.requestInterruption`.
