.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: () const
    :digest: ceca3ba2bb8012df624757dce1df1e14

Dumps some details about the `visual tree of Items <https://doc.qt.io/qt-6/qtquick-visualcanvas-visualparent.html>`_ starting with this item, recursively.

**Note:** :sip:ref:`~PyQt6.QtCore.QObject.dumpObjectTree` dumps a similar tree; but, as explained in `Concepts - Visual Parent in Qt Quick <https://doc.qt.io/qt-6/qtquick-visualcanvas-visualparent.html>`_, an item's :sip:ref:`~PyQt6.QtCore.QObject.parent` sometimes differs from its :sip:ref:`~PyQt6.QtQuick.QQuickItem.parentItem`. You can dump both trees to see the difference.

**Note:** The exact output format may change in future versions of Qt.

.. seealso:: `GammaRay's Qt Quick Inspector <https://doc.qt.io/GammaRay/gammaray-qtquick2-inspector.html>`_, Debugging Techniques.
