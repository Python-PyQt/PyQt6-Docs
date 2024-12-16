.. sip:method-description::
    :status: todo
    :pysig: b6da2bfae229ab0448ace11dffdc01bb
    :realsig: (const QPointF&) const
    :digest: 322ce362838472eb90caa30db68c792c

Maps the given *point* in this item's coordinate system to the equivalent point within global screen coordinate system, and returns the mapped coordinate.

The following properties of the item are used in the mapping: :sip:ref:`~PyQt6.QtQuick.QQuickItem.x`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.y`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.scale`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.rotation`, :sip:ref:`~PyQt6.QtQuick.QQuickItem.transformOrigin`, and `transform <https://doc.qt.io/qt-6/qml-qtquick-item.html#transform-prop>`_.

If the items are part of different scenes, the mapping includes the relative position of the two scenes.

For example, this may be helpful to add a popup to a Qt Quick component.

**Note:** Window positioning is done by the window manager and this value is treated only as a hint. So, the resulting window position may differ from what is expected.

.. seealso:: `Concepts - Visual Coordinates in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-coordinates.html>`_.
