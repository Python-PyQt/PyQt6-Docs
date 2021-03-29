.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 6fc9bba737a9ff8f86be0876b5c8acee

Requests a Qt Quick scenegraph *backend*. Backends can either be built-in or be installed in form of dynamically loaded plugins.

This is an overloaded function.

**Note:** The call to the function must happen before constructing the first :sip:ref:`~PyQt6.QtQuick.QQuickWindow` in the application. It cannot be changed afterwards.

If *backend* is invalid or an error occurs, the request is ignored.

**Note:** Calling this function is equivalent to setting the ``QT_QUICK_BACKEND`` or ``QMLSCENE_DEVICE`` environment variables. However, this API is safer to use in applications that spawn other processes as there is no need to worry about environment inheritance.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphBackend`.
