.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (unsigned long)
    :digest: fbd6f408a75d6aab2a6b5366580106fd

This is an overloaded function, equivalent to calling:

::

    QThread::sleep(std::chrono::milliseconds{msecs});

**Note:** This function does not guarantee accuracy. The application may sleep longer than *msecs* under heavy load conditions. Some OSes might round *msecs* up to 10 ms or 15 ms.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.sleep`, :sip:ref:`~PyQt6.QtCore.QThread.usleep`.
