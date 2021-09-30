.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0433cd185807717ecdc1d7756b82f9a0

Aborts the current connection and resets the socket. Unlike :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnectFromService`, this function immediately closes the socket, discarding any pending data in the write buffer.

**Note:** On Android, aborting the socket requires asynchronous interaction with Android threads. Therefore the associated :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnected` and :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.stateChanged` signals are delayed until the threads have finished the closure.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.disconnectFromService`, :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.close`.
