.. sip:method-description::
    :status: todo
    :pysig: 263b7898f9ddda8006881fa7011ebb3d
    :realsig: (const QString&, const QList<QVariant>&)
    :digest: 3376a699c163917b51b56c5958490783

Places a call to the remote method specified by *method* on this interface, using *args* as arguments. This function returns a :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall` object that can be used to track the status of the reply and access its contents once it has arrived.

Normally, you should place calls using :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.asyncCall`.

**Note:** Method calls to objects registered by the application itself are never asynchronous due to implementation limitations.
