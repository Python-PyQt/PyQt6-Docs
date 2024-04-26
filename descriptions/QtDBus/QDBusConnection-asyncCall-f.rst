.. sip:method-description::
    :status: todo
    :pysig: b921d36ece1c0a461ae26a62c26a1056
    :realsig: (const QDBusMessage&,int) const
    :digest: 3dfc6a5130235aaa6acdb5754fe46e77

Sends the *message* over this connection and returns immediately. This function is suitable for method calls only. It returns an object of type :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall` which can be used to track the status of the reply.

If no reply is received within *timeout* milliseconds, an automatic error will be delivered indicating the expiration of the call. The default *timeout* is -1, which will be replaced with an implementation-defined value that is suitable for inter-process communications (generally, 25 seconds). This timeout is also the upper limit for waiting in QDBusPendingCall::waitForFinished().

See the QDBusInterface::asyncCall() function for a more friendly way of placing calls.

**Note:** Method calls to objects registered by the application itself are never asynchronous due to implementation limitations.
