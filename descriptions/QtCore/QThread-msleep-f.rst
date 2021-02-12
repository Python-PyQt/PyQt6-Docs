.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (unsigned long)
    :digest: 61a9815f3e1b499af7b962765e3e3c72

Forces the current thread to sleep for *msecs* milliseconds.

Avoid using this function if you need to wait for a given condition to change. Instead, connect a slot to the signal that indicates the change or use an event handler (see :sip:ref:`~PyQt6.QtCore.QObject.event`).

**Note:** This function does not guarantee accuracy. The application may sleep longer than *msecs* under heavy load conditions. Some OSes might round *msecs* up to 10 ms or 15 ms.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.sleep`, :sip:ref:`~PyQt6.QtCore.QThread.usleep`.
