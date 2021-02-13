.. sip:method-description::
    :status: todo
    :pysig: 50cad8623622f8634e05e32fc5f89c03
    :realsig: (const QPointF&)
    :digest: c77819ad8b8a87b33087df95620390c0

Scrolls the contents of the viewport to ensure that the scene coordinate *pos*, is centered in the view.

Because *pos* is a floating point coordinate, and the scroll bars operate on integer coordinates, the centering is only an approximation.

**Note:** If the item is close to or outside the border, it will be visible in the view, but not centered.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.ensureVisible`.
