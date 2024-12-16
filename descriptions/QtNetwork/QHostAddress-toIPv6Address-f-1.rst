.. sip:method-description::
    :status: todo
    :pysig: c4641409bedea0cf5d7d540a09c3db1e
    :realsig: () const
    :digest: acb80aab8dcca2cd57d9cddbaf20517d

Returns the IPv6 address as a Q_IPV6ADDR structure. The structure consists of 16 unsigned characters.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qhostaddress.py
    :lines: 54-59

This value is valid if the :sip:ref:`~PyQt6.QtNetwork.QHostAddress.protocol` is :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv6Protocol`. If the protocol is :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.NetworkLayerProtocol.IPv4Protocol`, then the address is returned as an IPv4 mapped IPv6 address. (RFC4291)

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QHostAddress.toString`.
