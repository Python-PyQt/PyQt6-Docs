.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: () const
    :digest: 7a7b5d82d610b12cbb2113fc99538cd1

Returns a pointer to the object that sent the signal, if called in a slot activated by a signal; otherwise it returns ``nullptr``. The pointer is valid only during the execution of the slot that calls this function from this object's thread context.

The pointer returned by this function becomes invalid if the sender is destroyed, or if the slot is disconnected from the sender's signal.

**Warning:** This function violates the object-oriented principle of modularity. However, getting access to the sender might be useful when many signals are connected to a single slot.

**Warning:** As mentioned above, the return value of this function is not valid when the slot is called via a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection` from a thread different from this object's thread. Do not use this function in this type of scenario.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.senderSignalIndex`.
