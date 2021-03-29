.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: () const
    :digest: 7cb45053157145a5d5835c03451851ad

Returns the bounding rectangle in item coordinates for the area :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` touches. The value is only in use when :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.flags` includes :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.RenderingFlags.BoundedRectRendering`, ignored otherwise.

Reporting the rectangle in combination with :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.RenderingFlags.BoundedRectRendering` is particularly important with the ``software`` backend because otherwise having a rendernode in the scene would trigger fullscreen updates, skipping all partial update optimizations.

For rendernodes covering the entire area of a corresponding :sip:ref:`~PyQt6.QtQuick.QQuickItem` the return value will be (0, 0, item->width(), item->height()).

**Note:** Nodes are also free to render outside the boundaries specified by the item's width and height, since the scenegraph nodes are not bounded by the :sip:ref:`~PyQt6.QtQuick.QQuickItem` geometry, as long as this is reported correctly from this function.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.flags`.
