.. sip:method-description::
    :status: todo
    :pysig: d42f85a3335f7419882f1c84b5f7b770
    :realsig: (const QDBusMessage&,QDBus::CallMode,int) const
    :digest: e3b1c4157b04784ae5dcc9e97367c847

Sends the *message* over this connection and blocks, waiting for a reply, for at most *timeout* milliseconds. This function is suitable for method calls only. It returns the reply message as its return value, which will be either of type :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.ReplyMessage` or :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.ErrorMessage`.

If no reply is received within *timeout* milliseconds, an automatic error will be delivered indicating the expiration of the call. The default *timeout* is -1, which will be replaced with an implementation-defined value that is suitable for inter-process communications (generally, 25 seconds).

See the QDBusInterface::call() function for a more friendly way of placing calls.

**Warning:** If *mode* is :sip:ref:`~PyQt6.QtDBus.QDBus.CallMode.BlockWithGui`, this function will reenter the Qt event loop in order to wait for the reply. During the wait, it may deliver signals and other method calls to your application. Therefore, it must be prepared to handle a reentrancy whenever a call is placed with .
