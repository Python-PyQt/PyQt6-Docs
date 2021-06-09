.. sip:method-description::
    :status: todo
    :pysig: b6da2bfae229ab0448ace11dffdc01bb
    :realsig: (const QPointF&) const
    :digest: f8c556bf499cc6cd8a2872a34004ac45

Maps the given *point* in the global screen coordinate system to the equivalent point within this item's coordinate system, and returns the mapped coordinate.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

For example, this may be helpful to add a popup to a Qt Quick component.

**Note:** Window positioning is done by the window manager and this value is treated only as a hint. So, the resulting window position may differ from what is expected.

**Note:** If this item is in a subscene, e.g. mapped onto a 3D `Model <https://doc.qt.io/qt-6/qml-qtquick3d-model.html>`_ object, the UV mapping is incorporated into this transformation, so that it really goes from screen coordinates to this item's coordinates, as long as *point* is actually within this item's bounds. The other mapping functions do not yet work that way.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
