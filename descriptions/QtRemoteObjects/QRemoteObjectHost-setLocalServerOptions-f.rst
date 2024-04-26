.. sip:method-description::
    :status: todo
    :pysig: 3510ef69a42bb758cbcf1793b991230b
    :realsig: (QLocalServer::SocketOptions)
    :digest: d67ae8224f187d196a5fea120c1e715d

Sets the socket options for :sip:ref:`~PyQt6.QtNetwork.QLocalServer` backends to *options*.

It must be set before the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` object starts listening. It has no consequence for already listening :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` objects or :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` objects that use different backends than :sip:ref:`~PyQt6.QtNetwork.QLocalServer`. :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` objects start to listen during construction if the *address* argument is non-empty, otherwise when the address is set via :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost.setHostUrl`.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost.setHostUrl`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost`.
