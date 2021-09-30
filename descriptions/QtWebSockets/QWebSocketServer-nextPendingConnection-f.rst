.. sip:method-description::
    :status: todo
    :pysig: 72efbf33b244dcd2392c9f5f0aab71a2
    :realsig: ()
    :digest: ac8763f775c135150884cacd4a4b1c6a

Returns the next pending connection as a connected :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` object. :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer` does not take ownership of the returned :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` object. It is up to the caller to delete the object explicitly when it will no longer be used, otherwise a memory leak will occur. nullptr is returned if this function is called when there are no pending connections.

Note: The returned :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` object cannot be used from another thread.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.hasPendingConnections`.
