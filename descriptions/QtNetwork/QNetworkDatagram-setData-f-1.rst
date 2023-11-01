.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: a9c9577c0f2fa03215660580d457ff2e

Sets the data payload of this datagram to *data*. It is usually not necessary to call this function on received datagrams. For outgoing datagrams, this function sets the data to be sent on the network.

Since datagrams can empty, an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is a valid value for *data*.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.data`.
