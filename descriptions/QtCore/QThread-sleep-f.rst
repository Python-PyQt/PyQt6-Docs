.. sip:method-description::
    :status: todo
    :pysig: 5cd04cdbb9ebf068a865ec63c9099761
    :realsig: (unsigned long)
    :digest: 6c795c7505246122bf943e40e0e3daaf

Forces the current thread to sleep for *secs* seconds.

Avoid using this function if you need to wait for a given condition to change. Instead, connect a slot to the signal that indicates the change or use an event handler (see :sip:ref:`~PyQt6.QtCore.QObject.event`).

**Note:** This function does not guarantee accuracy. The application may sleep longer than *secs* under heavy load conditions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.msleep`, :sip:ref:`~PyQt6.QtCore.QThread.usleep`.
