.. sip:signal-description::
    :status: todo
    :pysig: 7e9fe7e96e744aa55dd6d3c9ec39fbd4
    :realsig: (QAbstractSocket::SocketState)
    :digest: 21fd63e8925cd51f93f32e510a44a1d5

This signal is emitted whenever :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`'s state changes. The *socketState* parameter is the new state.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState` is not a registered metatype, so for queued connections, you will have to register it with Q_DECLARE_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.state`, `Creating Custom Qt Types <https://doc.qt.io/qt-6/custom-types.html>`_.
