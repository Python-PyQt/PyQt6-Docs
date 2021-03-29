.. sip:method-description::
    :status: todo
    :pysig: 10b73e32ef579338968290bf7f39b35c
    :realsig: (const QRectF&) const
    :digest: 7d1c45d2022d497f95fe7a5aeb684d9a

Maps the given *rect* in this item's coordinate system to the equivalent rectangular area within the scene's coordinate system, and returns the mapped rectangle value.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
