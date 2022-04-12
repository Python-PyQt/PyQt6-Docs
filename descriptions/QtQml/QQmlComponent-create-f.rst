.. sip:method-description::
    :status: todo
    :pysig: abd865647d9b87b38bc934925ca4940a
    :realsig: (QQmlContext*)
    :digest: af14ecd3ce230f33d4d8ce3374f8a30c

Create an object instance from this component, within the specified *context*. Returns ``nullptr`` if creation failed.

If *context* is ``nullptr`` (the default), it will create the instance in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext` of the engine.

The ownership of the returned object instance is transferred to the caller.

If the object being created from this component is a visual item, it must have a visual parent, which can be set by calling :sip:ref:`~PyQt6.QtQuick.QQuickItem.setParentItem`. See `Concepts - Visual Parent in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-visualparent.html>`_ for more details.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership.ObjectOwnership`.
