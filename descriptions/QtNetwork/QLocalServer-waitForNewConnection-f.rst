.. sip:method-description::
    :status: todo
    :pysig: da20721ef92ba4580ba440f471645208
    :realsig: (int,bool*)
    :digest: c929fee7e42f25d3df0f5c05454254a0

Waits for at most *msec* milliseconds or until an incoming connection is available. Returns ``true`` if a connection is available; otherwise returns ``false``. If the operation timed out and *timedOut* is not ``nullptr``, \*timedOut will be set to true.

This is a blocking function call. Its use is ill-advised in a single-threaded GUI application, since the whole application will stop responding until the function returns.  is mostly useful when there is no event loop available.

The non-blocking alternative is to connect to the :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection` signal.

If msec is -1, this function will not time out.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.hasPendingConnections`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.nextPendingConnection`.
