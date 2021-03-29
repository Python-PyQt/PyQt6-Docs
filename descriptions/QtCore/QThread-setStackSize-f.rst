.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (uint)
    :digest: 7801db93fb609206e21ae1b9db84d87c

Sets the maximum stack size for the thread to *stackSize*. If *stackSize* is greater than zero, the maximum stack size is set to *stackSize* bytes, otherwise the maximum stack size is automatically determined by the operating system.

**Warning:** Most operating systems place minimum and maximum limits on thread stack sizes. The thread will fail to start if the stack size is outside these limits.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.stackSize`.
