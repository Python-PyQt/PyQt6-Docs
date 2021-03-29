.. sip:method-description::
    :status: todo
    :pysig: abd865647d9b87b38bc934925ca4940a
    :realsig: (QQmlContext*)
    :digest: 1a71365c11f8ce603ceacb6206a8aefb

Create an object instance from this component. Returns ``nullptr`` if creation failed. *context* specifies the context within which to create the object instance.

If *context* is ``nullptr`` (the default), it will create the instance in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext` of the engine.

The ownership of the returned object instance is transferred to the caller.

If the object being created from this component is a visual item, it must have a visual parent, which can be set by calling :sip:ref:`~PyQt6.QtQuick.QQuickItem.setParentItem`. See `Concepts - Visual Parent in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-visualparent.html>`_ for more details.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership.ObjectOwnership`.
