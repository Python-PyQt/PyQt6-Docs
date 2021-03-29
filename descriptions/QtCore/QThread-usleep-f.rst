.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (unsigned long)
    :digest: bd32bfbd81554d2a8ee5d733deed90f9

Forces the current thread to sleep for *usecs* microseconds.

Avoid using this function if you need to wait for a given condition to change. Instead, connect a slot to the signal that indicates the change or use an event handler (see :sip:ref:`~PyQt6.QtCore.QObject.event`).

**Note:** This function does not guarantee accuracy. The application may sleep longer than *usecs* under heavy load conditions. Some OSes might round *usecs* up to 10 ms or 15 ms; on Windows, it will be rounded up to a multiple of 1 ms.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.sleep`, :sip:ref:`~PyQt6.QtCore.QThread.msleep`.
