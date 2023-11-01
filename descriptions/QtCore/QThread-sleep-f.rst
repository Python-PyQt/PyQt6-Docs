.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (unsigned long)
    :digest: d6c2c52a823df248d50bebb0bd3abd75

Forces the current thread to sleep for *secs* seconds.

This is an overloaded function, equivalent to calling:

::

    QThread::sleep(std::chrono::seconds{secs});

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.msleep`, :sip:ref:`~PyQt6.QtCore.QThread.usleep`.
