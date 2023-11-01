.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (unsigned long)
    :digest: b625e52bd960d90f59aee1b252270252

This is an overloaded function, equivalent to calling:

::

    QThread::sleep(std::chrono::microseconds{secs});

**Note:** This function does not guarantee accuracy. The application may sleep longer than *usecs* under heavy load conditions. Some OSes might round *usecs* up to 10 ms or 15 ms; on Windows, it will be rounded up to a multiple of 1 ms.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.sleep`, :sip:ref:`~PyQt6.QtCore.QThread.msleep`.
