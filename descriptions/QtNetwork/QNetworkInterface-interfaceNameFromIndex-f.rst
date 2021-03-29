.. sip:method-description::
    :status: todo
    :pysig: 41c238740a2f878c320aa2b884ab22b5
    :realsig: (int)
    :digest: 75b3aeff15f1a40cacefbf4920459f08

Returns the name of the interface whose index is *index* or an empty string if there is no interface with that index. This function should produce the same result as the following code, but will probably execute faster.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_kernel_qnetworkinterface.py
    :lines: 47-47

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceFromIndex`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface.interfaceIndexFromName`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram.interfaceIndex`.
