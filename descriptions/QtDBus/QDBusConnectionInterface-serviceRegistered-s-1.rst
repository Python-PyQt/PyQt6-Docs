.. sip:signal-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: eac4722a07dd57ab0baec7f09bfbce5e

This signal is emitted by the D-Bus server when the bus service name (unique connection name or well-known service name) given by *service* is acquired by this application.

Acquisition happens after this application has requested a name using :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.registerService`.
