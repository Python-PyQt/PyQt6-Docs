.. sip:method-description::
    :status: todo
    :pysig: b6da2bfae229ab0448ace11dffdc01bb
    :realsig: (const QPointF&) const
    :digest: ddb0e460cb6508add77b75919c715918

Maps the given *point* in the scene's coordinate system to the equivalent point within this item's coordinate system, and returns the mapped coordinate.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
