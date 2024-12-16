.. sip:method-description::
    :status: todo
    :pysig: 7a792ec7fc75acdd989096b04406cda5
    :realsig: (const QString&, QObject*)
    :digest: 6a35342898aae1b14bfb3d354833a10f

Registers a single object to the :sip:ref:`~PyQt6.QtWebChannel.QWebChannel`.

The properties, signals and public methods of the *object* are published to the remote clients. There, an object with the identifier *id* is then constructed.

A property that is ``BINDABLE`` but does not have a ``NOTIFY`` signal will have working property updates on the client side, but no mechanism to register a callback for the change notifications.

**Note:** A current limitation is that objects must be registered before any client is initialized.

.. seealso:: :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.registerObjects`, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.deregisterObject`, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.registeredObjects`.
