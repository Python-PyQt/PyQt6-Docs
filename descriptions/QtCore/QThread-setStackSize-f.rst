.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (uint)
    :digest: 98e902139da71582e7b296877731caf9

Sets the stack size for the thread to *stackSize*. If *stackSize* is zero, the operating system or runtime will choose a default value. Otherwise, the thread's stack size will be the value provided (which may be rounded up or down).

On most operating systems, the amount of memory allocated to serve the stack will initially be smaller than *stackSize* and will grow as the thread uses the stack. This parameter sets the maximum size it will be allowed to grow to (that is, it sets the size of the virtual memory space the stack is allowed to occupy).

This function can only be called before the thread is started.

**Warning:** Most operating systems place minimum and maximum limits on thread stack sizes. The thread will fail to start if the stack size is outside these limits.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.stackSize`.
