.. sip:method-description::
    :status: todo
    :pysig: cfd68ca3cd4a974813d6d12304a7fcdf
    :realsig: (const QString&, QDBusConnectionInterface::ServiceQueueOptions, QDBusConnectionInterface::ServiceReplacementOptions)
    :digest: 0c677cf06429c448e996cb64dbc7b1f3

Requests to register the service name *serviceName* on the bus. The *qoption* flag specifies how the D-Bus server should behave if *serviceName* is already registered. The *roption* flag specifies if the server should allow another application to replace our registered name.

If the service registration succeeds, the :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceRegistered` signal will be emitted. If we are placed in queue, the signal will be emitted when we obtain the name. If *roption* is :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.ServiceReplacementOptions.AllowReplacement`, the :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceUnregistered` signal will be emitted if another application replaces this one.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.unregisterService`.
