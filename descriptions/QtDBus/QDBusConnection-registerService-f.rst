.. sip:method-description::
    :status: todo
    :pysig: 502f7d3e77c89e5ef63bfbd42eaccbfd
    :realsig: (const QString&)
    :digest: 054cb192d93b0eb03a6e6fec6a6617c0

Attempts to register the *serviceName* on the D-Bus server and returns ``true`` if the registration succeeded. The registration will fail if the name is already registered by another application.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.unregisterService`, :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.registerService`.
