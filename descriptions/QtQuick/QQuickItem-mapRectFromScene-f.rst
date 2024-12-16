.. sip:method-description::
    :status: todo
    :pysig: 10b73e32ef579338968290bf7f39b35c
    :realsig: (const QRectF&) const
    :digest: bc948c3e54ccab2529521af1b8f12e20

Maps the given *rect* in the scene's coordinate system to the equivalent rectangular area within this item's coordinate system, and returns the mapped rectangle value.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

If the items are part of different scenes, the mapping includes the relative position of the two scenes.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
