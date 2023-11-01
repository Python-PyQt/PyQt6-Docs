.. sip:signal-description::
    :status: todo
    :pysig: 31c2d3982cfaf905cac8e2c6560b0db1
    :realsig: (const QString&, const QString&, const QString&)
    :digest: 06a350101274da45e0905295e28c129f

Use :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` instead.

This signal is emitted by the D-Bus server whenever a service ownership change happens in the bus, including apparition and disparition of names.

This signal means the application *oldOwner* lost ownership of bus name *name* to application *newOwner*. If *oldOwner* is an empty string, it means the name *name* has just been created; if *newOwner* is empty, the name *name* has no current owner and is no longer available.

**Note:** connecting to this signal will make the application listen for and receive every single service ownership change on the bus. Depending on how many services are running, this make the application be activated to receive more signals than it needs. To avoid this problem, use the :sip:ref:`~PyQt6.QtDBus.QDBusServiceWatcher` class, which can listen for specific changes.
