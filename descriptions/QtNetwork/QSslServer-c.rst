.. sip:class-description::
    :status: todo
    :brief: Implements an encrypted, secure TCP server over TLS
    :digest: 54ad5b7d09f70013e1dbde018bbe68f5

Implements an encrypted, secure TCP server over TLS.

Class to use in place of :sip:ref:`~PyQt6.QtNetwork.QTcpServer` to implement TCP server using Transport Layer Security (TLS).

To configure the secure handshake settings, use the applicable setter functions on a :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object, and then use it as a argument to the :sip:ref:`~PyQt6.QtNetwork.QSslServer.setSslConfiguration` function. All following incoming connections handled will use these settings.

To start listening to incoming connections use the listen() function inherited from :sip:ref:`~PyQt6.QtNetwork.QTcpServer`. Other settings can be configured by using the setter functions inherited from the :sip:ref:`~PyQt6.QtNetwork.QTcpServer` class.

Connect to the signals of this class to respond to the incoming connection attempts. They are the same as the signals on :sip:ref:`~PyQt6.QtNetwork.QSslSocket`, but also passes a pointer to the socket in question.

When responding to the pendingConnectionAvailable() signal, use the nextPendingConnection() function to fetch the next incoming connection and take it out of the pending connection queue. The :sip:ref:`~PyQt6.QtNetwork.QSslSocket` is a child of the :sip:ref:`~PyQt6.QtNetwork.QSslServer` and will be deleted when the :sip:ref:`~PyQt6.QtNetwork.QSslServer` is deleted. It is still a good a good idea to destroy the object explicitly when you are done with it, to avoid wasting memory.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket`.
