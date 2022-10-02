.. sip:class-description::
    :status: todo
    :brief: Allows the user to watch for a bus service change
    :digest: 23ca629babffdbd33cac41871d0fb31b

The :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` class allows the user to watch for a bus service change.

A :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` object can be used to notify the application about an ownership change of a service name on the bus. It has three watch modes:

* Watching for service registration only.

* Watching for service unregistration only.

* Watching for any kind of service ownership change (the default mode).

Besides being created or deleted, services may change owners without a unregister/register operation happening. So the :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.serviceRegistered` and :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher.serviceUnregistered` signals may not be emitted if that happens.

This class is more efficient than using the QDBusConnectionInterface::serviceOwnerChanged() signal because it allows one to receive only the signals for which the class is interested in.

Ending a service name with the character '\*' will match all service names within the specified namespace.

For example "com.example.backend1\*" will match

* com.example.backend1

* com.example.backend1.foo

* com.example.backend1.foo.bar

Substrings in the same domain will not be matched, i.e "com.example.backend12".

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusConnection`.
