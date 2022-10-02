.. sip:method-description::
    :status: todo
    :pysig: 2de4a9b36e90e283f219da86d9f7de66
    :realsig: (QSGNode*,QQuickItem::UpdatePaintNodeData*)
    :digest: 4a00439ab817cb5e5741708d279271bb

Called on the render thread when it is time to sync the state of the item with the scene graph.

The function is called as a result of :sip:ref:`~PyQt6.QtQuick.QQuickItem.update`, if the user has set the :sip:ref:`~PyQt6.QtQuick.QQuickItem.Flag.ItemHasContents` flag on the item.

The function should return the root of the scene graph subtree for this item. Most implementations will return a single :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode` containing the visual representation of this item. *oldNode* is the node that was returned the last time the function was called. *updatePaintNodeData* provides a pointer to the :sip:ref:`~PyQt6.QtQuick.QSGTransformNode` associated with this :sip:ref:`~PyQt6.QtQuick.QQuickItem`.

::

    QSGNode *MyItem::updatePaintNode(QSGNode *node, UpdatePaintNodeData *)
    {
        QSGSimpleRectNode *n = static_cast<QSGSimpleRectNode *>(node);
        if (!n) {
            n = new QSGSimpleRectNode();
            n->setColor(Qt::red);
        }
        n->setRect(boundingRect());
        return n;
    }

The main thread is blocked while this function is executed so it is safe to read values from the :sip:ref:`~PyQt6.QtQuick.QQuickItem` instance and other objects in the main thread.

If no call to QQuickItem::updatePaintNode() result in actual scene graph changes, like :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty` or adding and removing nodes, then the underlying implementation may decide to not render the scene again as the visual outcome is identical.

**Warning:** It is crucial that graphics operations and interaction with the scene graph happens exclusively on the render thread, primarily during the QQuickItem::updatePaintNode() call. The best rule of thumb is to only use classes with the "QSG" prefix inside the QQuickItem::updatePaintNode() function.

**Warning:** This function is called on the render thread. This means any QObjects or thread local storage that is created will have affinity to the render thread, so apply caution when doing anything other than rendering in this function. Similarly for signals, these will be emitted on the render thread and will thus often be delivered via queued connections.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGMaterial`, :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode`, :sip:ref:`~PyQt6.QtQuick.QSGGeometry`, :sip:ref:`~PyQt6.QtQuick.QSGFlatColorMaterial`, :sip:ref:`~PyQt6.QtQuick.QSGTextureMaterial`, :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty`, :ref:`qquickitem-graphics-resource-handling`.
