.. sip:method-description::
    :status: todo
    :pysig: 0dd2ad472f3d3a5c8f581d0b8cbf4e29
    :realsig: (const QHash<QString, QObject*>&)
    :digest: 7cab882630552490c7f18a0dc9e4cdec

Registers a group of objects to the :sip:ref:`~PyQt6.QtWebChannel.QWebChannel`.

The properties, signals and public invokable methods of the objects are published to the remote clients. There, an object with the identifier used as key in the *objects* map is then constructed.

**Note:** A current limitation is that objects must be registered before any client is initialized.

.. seealso:: :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.registerObject`, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.deregisterObject`, :sip:ref:`~PyQt6.QtWebChannel.QWebChannel.registeredObjects`.
