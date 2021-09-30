.. sip:method-description::
    :status: todo
    :pysig: 76b1d76b58b3fa384e0af90fb23670ee
    :realsig: () const
    :digest: 8ed13642a6081d002dc15a9516491d57

Returns the security parameters used for the initial connection attempt.

The security parameters may be renegotiated between the two parties during or after the connection has been established. If such a change happens it is not reflected in the value of this flag.

On macOS, this flag is always set to :sip:ref:`~PyQt6.QtBluetooth.QBluetooth.Security.Secure`.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QBluetoothSocket.setPreferredSecurityFlags`.
