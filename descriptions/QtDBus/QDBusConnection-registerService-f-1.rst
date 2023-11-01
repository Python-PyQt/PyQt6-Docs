.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 054cb192d93b0eb03a6e6fec6a6617c0

Attempts to register the *serviceName* on the D-Bus server and returns ``true`` if the registration succeeded. The registration will fail if the name is already registered by another application.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.unregisterService`, :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.registerService`.
