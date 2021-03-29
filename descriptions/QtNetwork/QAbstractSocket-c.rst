.. sip:class-description::
    :status: todo
    :brief: The base functionality common to all socket types
    :digest: 3e135a602976409e48b739892693f325

The :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` class provides the base functionality common to all socket types.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` is the base class for :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` and :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` and contains all common functionality of these two classes. If you need a socket, you have two options:

* Instantiate :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` or :sip:ref:`~PyQt6.QtNetwork.QUdpSocket`.

* Create a native socket descriptor, instantiate :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`, and call :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setSocketDescriptor` to wrap the native socket.

TCP (Transmission Control Protocol) is a reliable, stream-oriented, connection-oriented transport protocol. UDP (User Datagram Protocol) is an unreliable, datagram-oriented, connectionless protocol. In practice, this means that TCP is better suited for continuous transmission of data, whereas the more lightweight UDP can be used when reliability isn't important.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`'s API unifies most of the differences between the two protocols. For example, although UDP is connectionless, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost` establishes a virtual connection for UDP sockets, enabling you to use :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` in more or less the same way regardless of the underlying protocol. Internally, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` remembers the address and port passed to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`, and functions like read() and write() use these values.

At any time, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` has a state (returned by :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.state`). The initial state is :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.UnconnectedState`. After calling :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`, the socket first enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.HostLookupState`. If the host is found, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectingState` and emits the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.hostFound` signal. When the connection has been established, it enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` and emits :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connected`. If an error occurs at any stage, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.errorOccurred` is emitted. Whenever the state changes, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.stateChanged` is emitted. For convenience, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.isValid` returns ``true`` if the socket is ready for reading and writing, but note that the socket's state must be :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` before reading and writing can occur.

Read or write data by calling read() or write(), or use the convenience functions readLine() and readAll(). :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` also inherits getChar(), putChar(), and ungetChar() from :sip:ref:`~PyQt6.QtCore.QIODevice`, which work on single bytes. The bytesWritten() signal is emitted when data has been written to the socket. Note that Qt does not limit the write buffer size. You can monitor its size by listening to this signal.

The readyRead() signal is emitted every time a new chunk of data has arrived. :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.bytesAvailable` then returns the number of bytes that are available for reading. Typically, you would connect the readyRead() signal to a slot and read all available data there. If you don't read all the data at once, the remaining data will still be available later, and any new incoming data will be appended to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`'s internal read buffer. To limit the size of the read buffer, call :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setReadBufferSize`.

To close the socket, call :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnectFromHost`. :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ClosingState`. After all pending data has been written to the socket, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` actually closes the socket, enters :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.UnconnectedState`, and emits :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnected`. If you want to abort a connection immediately, discarding all pending data, call :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.abort` instead. If the remote host closes the connection, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` will emit :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.errorOccurred`\ (\ :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketError.RemoteHostClosedError`), during which the socket state will still be :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState`, and then the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnected` signal will be emitted.

The port and address of the connected peer is fetched by calling :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerPort` and :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerAddress`. :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerName` returns the host name of the peer, as passed to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`. :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localPort` and :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localAddress` return the port and address of the local socket.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` provides a set of functions that suspend the calling thread until certain signals are emitted. These functions can be used to implement blocking sockets:

* :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.waitForConnected` blocks until a connection has been established.

* :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.waitForReadyRead` blocks until new data is available for reading.

* :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.waitForBytesWritten` blocks until one payload of data has been written to the socket.

* :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.waitForDisconnected` blocks until the connection has closed.

We show an example:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-network-tcpwait.py
    :lines: 64-75

If :sip:ref:`~PyQt6.QtCore.QIODevice.waitForReadyRead` returns ``false``, the connection has been closed or an error has occurred.

Programming with a blocking socket is radically different from programming with a non-blocking socket. A blocking socket doesn't require an event loop and typically leads to simpler code. However, in a GUI application, blocking sockets should only be used in non-GUI threads, to avoid freezing the user interface. See the `fortuneclient <https://doc.qt.io/qt-6/qtnetwork-fortuneclient-example.html>`_ and `blockingfortuneclient <https://doc.qt.io/qt-6/qtnetwork-blockingfortuneclient-example.html>`_ examples for an overview of both approaches.

**Note:** We discourage the use of the blocking functions together with signals. One of the two possibilities should be used.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` can be used with :sip:ref:`~PyQt6.QtCore.QTextStream` and :sip:ref:`~PyQt6.QtCore.QDataStream`'s stream operators (operator<<() and operator>>()). There is one issue to be aware of, though: You must make sure that enough data is available before attempting to read it using operator>>().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer`.
