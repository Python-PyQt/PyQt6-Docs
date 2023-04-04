:orphan:

.. sip:class:: PyQt6.QtNetwork.QUdpSocket
    :inherits: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`
    :description: QtNetwork/QUdpSocket-c.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtNetwork/QUdpSocket-__init__-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.hasPendingDatagrams
        :returns:
            bool
        :description: QtNetwork/QUdpSocket-hasPendingDatagrams-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.joinMulticastGroup
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :returns:
            bool
        :description: QtNetwork/QUdpSocket-joinMulticastGroup-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.joinMulticastGroup
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :returns:
            bool
        :description: QtNetwork/QUdpSocket-joinMulticastGroup-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.leaveMulticastGroup
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
        :returns:
            bool
        :description: QtNetwork/QUdpSocket-leaveMulticastGroup-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.leaveMulticastGroup
        :args:
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :returns:
            bool
        :description: QtNetwork/QUdpSocket-leaveMulticastGroup-f-1.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.multicastInterface
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :description: QtNetwork/QUdpSocket-multicastInterface-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.pendingDatagramSize
        :returns:
            int
        :description: QtNetwork/QUdpSocket-pendingDatagramSize-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.readDatagram
        :args:
            int
        :returns:
            bytes
            :sip:ref:`~PyQt6.QtNetwork.QHostAddress`
            int
        :description: QtNetwork/QUdpSocket-readDatagram-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.receiveDatagram
        :args:
            maxSize: int = -1
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram`
        :description: QtNetwork/QUdpSocket-receiveDatagram-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.setMulticastInterface
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkInterface`
        :description: QtNetwork/QUdpSocket-setMulticastInterface-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.writeDatagram
        :args:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkDatagram`
        :returns:
            int
        :description: QtNetwork/QUdpSocket-writeDatagram-f.rst

    .. sip:method:: PyQt6.QtNetwork.QUdpSocket.writeDatagram
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
            Union[:sip:ref:`~PyQt6.QtNetwork.QHostAddress`, :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress`]
            int
        :returns:
            int
        :description: QtNetwork/QUdpSocket-writeDatagram-f-2.rst
