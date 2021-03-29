.. sip:method-description::
    :status: todo
    :pysig: 987ec54c89dbe263ad1a0e64e4c06ea9
    :realsig: (QDBus::CallMode,const QString&,const QList<QVariant>&)
    :digest: e183a70032a622819b8b0c03c665a66d

Places a call to the remote method specified by *method* on this interface, using *args* as arguments. This function returns the message that was received as a reply, which can be a normal :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.ReplyMessage` (indicating success) or :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.ErrorMessage` (if the call failed). The *mode* parameter specifies how this call should be placed.

If the call succeeds, :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.lastError` will be cleared; otherwise, it will contain the error this call produced.

Normally, you should place calls using :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.call`.

**Warning:** If you use ``UseEventLoop``, your code must be prepared to deal with any reentrancy: other method calls and signals may be delivered before this function returns, as well as other Qt queued signals and events.
