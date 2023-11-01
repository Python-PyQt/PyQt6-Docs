.. sip:method-description::
    :status: todo
    :pysig: f03dcfc4c7a8d7220dad44d76b9e0191
    :realsig: (const QString&)
    :digest: c704a1e328b169897fdc74ab6954d54b

Returns the index of the interface whose name is *name* or 0 if there is no interface with that name. This function should produce the same result as the following code, but will probably execute faster.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkinterface.py
    :lines: 43-43

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceFromName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceNameFromIndex`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.interfaceIndex`.
