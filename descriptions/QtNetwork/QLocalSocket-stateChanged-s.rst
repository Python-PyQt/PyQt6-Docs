.. sip:signal-description::
    :status: todo
    :pysig: 4e0d13c15a06b071fcfa8ecd7a77fbe4
    :realsig: (QLocalSocket::LocalSocketState)
    :digest: 011109acb79e4da37cfd9149c05b62f1

This signal is emitted whenever :sip:ref:`~PyQt6.QtNetwork.QLocalSocket`'s state changes. The *socketState* parameter is the new state.

QLocalSocket::SocketState is not a registered metatype, so for queued connections, you will have to register it with Q_DECLARE_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.state`, `Creating Custom Qt Types <https://doc.qt.io/qt-6/custom-types.html>`_.
