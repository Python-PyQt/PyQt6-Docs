.. sip:method-description::
    :status: todo
    :pysig: 72027f48b9d878c3a64e8f2588649c1d
    :realsig: (const QString&,QObject*)
    :digest: 1ca302e1fa627c5de36b45dd126dabe1

Registers a single object to the :sip:ref:`~PyQt6.QtWebChannel.QWebChannel`.

The properties, signals and public methods of the *object* are published to the remote clients. There, an object with the identifier *id* is then constructed.

**Note:** A property that is ``BINDABLE`` but does not have a ``NOTIFY`` signal will have working property updates on the client side, but no mechanism to register a callback for the change notifications.

**Note:** A current limitation is that objects must be registered before any client is initialized.

.. seealso:: :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.registerObjects`, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.deregisterObject`, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.registeredObjects`.
