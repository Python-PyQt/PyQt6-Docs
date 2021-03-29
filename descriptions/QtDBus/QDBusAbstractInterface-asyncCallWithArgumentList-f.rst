.. sip:method-description::
    :status: todo
    :pysig: 023f12e956eb128e12086ceddf892b38
    :realsig: (const QString&,const QList<QVariant>&)
    :digest: a7bdc0cbc8b09e94b600cee5fab3ad4a

Places a call to the remote method specified by *method* on this interface, using *args* as arguments. This function returns a :sip:ref:`~PyQt6.QtDBus.QDBusPendingCall` object that can be used to track the status of the reply and access its contents once it has arrived.

Normally, you should place calls using :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.asyncCall`.
