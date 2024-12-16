.. sip:method-description::
    :status: todo
    :pysig: 4bbbb3d8c3cbc8be55d1e5947ef9a3dc
    :realsig: (const QQuickItem*,const QRectF&) const
    :digest: 7ab5878a2080a96f3454dba5cccc63db

Maps the given *rect* in *item*'s coordinate system to the equivalent rectangular area within this item's coordinate system, and returns the mapped rectangle value.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

If the items are part of different scenes, the mapping includes the relative position of the two scenes.

If *item* is ``nullptr``, this maps *rect* from the coordinate system of the scene.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
