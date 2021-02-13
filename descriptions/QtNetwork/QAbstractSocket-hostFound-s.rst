.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 84fa1eaee31e63ca08f01c49c007842e

This signal is emitted after :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost` has been called and the host lookup has succeeded.

**Note:** Since Qt 4.6.3 :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` may emit  directly from the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost` call since a DNS result could have been cached.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected`.
