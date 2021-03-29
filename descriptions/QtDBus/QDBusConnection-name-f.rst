.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 93f3b34769b04d1660e1d293a0f434b3

Returns the connection name for this connection, as given as the name parameter to :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectToBus`.

The connection name can be used to uniquely identify actual underlying connections to buses. Copies made from a single connection will always implicitly share the underlying connection, and hence will have the same connection name.

Inversely, two connections having different connection names will always either be connected to different buses, or have a different unique name (as returned by :sip:ref:`~PyQt6.QtDBus.QDBusConnection.baseService`) on that bus.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectToBus`, :sip:ref:`~PyQt6.QtDBus.QDBusConnection.disconnectFromBus`.
