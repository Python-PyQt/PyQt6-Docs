.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (const QByteArray&)
    :digest: a9c9577c0f2fa03215660580d457ff2e

Sets the data payload of this datagram to *data*. It is usually not necessary to call this function on received datagrams. For outgoing datagrams, this function sets the data to be sent on the network.

Since datagrams can empty, an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is a valid value for *data*.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.data`.
