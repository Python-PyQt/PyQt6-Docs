.. sip:method-description::
    :status: todo
    :pysig: a0867d3002630bbad6e7e3985f19f7f9
    :realsig: (const QQuickItem*)
    :digest: f1062b6111fff5ad3396a450c3769e07

Moves the specified *sibling* item to the index after this item within the list of children. The order of children affects both the visual stacking order and tab focus navigation order.

Assuming the z values of both items are the same, this will cause *sibling* to be rendered below this item.

If both items have :sip:ref:`~PyQt6.QtQuick.QQuickItem.activeFocusOnTab` set to ``true``, this will also cause the tab focus order to change, with *sibling* receiving focus before this item.

The given *sibling* must be a sibling of this item; that is, they must have the same immediate parent.

.. seealso:: `Concepts - Visual Parent in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-visualparent.html>`_.
