.. sip:class-description::
    :status: todo
    :brief: Access to the D-Bus bus daemon service
    :digest: 6874176e4d977cc05cdfdb6fed339ced

The :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface` class provides access to the D-Bus bus daemon service.

The D-Bus bus server daemon provides one special interface ``org.freedesktop.DBus`` that allows clients to access certain properties of the bus, such as the current list of clients connected. The :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface` class provides access to that interface.

The most common uses of this class are to register and unregister service names on the bus using the :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.registerService` and :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.unregisterService` functions, query about existing names using the :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.isServiceRegistered`, :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.registeredServiceNames` and :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceOwner` functions, and to receive notification that a client has registered or de-registered through the :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceRegistered`, :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceUnregistered` and :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceOwnerChanged` signals.
