.. sip:method-description::
    :status: todo
    :pysig: 8358e6eb4698947d86dfde36a7725794
    :realsig: (const QQuickItem*,const QPointF&) const
    :digest: 8d6896e82e957ed4c3080682d3aea5c6

Maps the given *point* in *item*'s coordinate system to the equivalent point within this item's coordinate system, and returns the mapped coordinate.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

If *item* is ``nullptr``, this maps *point* from the coordinate system of the scene.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
