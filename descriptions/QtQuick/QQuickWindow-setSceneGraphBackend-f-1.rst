.. sip:method-description::
    :status: todo
    :pysig: c5283bf81cad04335531dd6931c2734d
    :realsig: (const QString&)
    :digest: 581c6d6ace112d5ba528e4dcab68f6c6

Requests a Qt Quick scenegraph *backend*. Backends can either be built-in or be installed in form of dynamically loaded plugins.

This is an overloaded function.

**Note:** The call to the function must happen before constructing the first :sip:ref:`~PyQt6.QtQuick.QQuickWindow` in the application. It cannot be changed afterwards.

See `Switch Between Adaptations in Your Application <https://doc.qt.io/qt-6/qtquick-visualcanvas-adaptations.html#switch-between-adaptations-in-your-application>`_ for more information about the list of backends. If *backend* is invalid or an error occurs, the request is ignored.

**Note:** Calling this function is equivalent to setting the ``QT_QUICK_BACKEND`` or ``QMLSCENE_DEVICE`` environment variables. However, this API is safer to use in applications that spawn other processes as there is no need to worry about environment inheritance.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphBackend`.
