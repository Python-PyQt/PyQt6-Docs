.. sip:method-description::
    :status: todo
    :pysig: 7c0574595c80995729d7956d73f9fa01
    :realsig: (const QTransform&,bool)
    :digest: 40dd7b70f6cd401a66a4e19d02f64a4e

Sets the view's current transformation matrix to *matrix*.

If *combine* is true, then *matrix* is combined with the current matrix; otherwise, *matrix* *replaces* the current matrix. *combine* is false by default.

The transformation matrix tranforms the scene into view coordinates. Using the default transformation, provided by the identity matrix, one pixel in the view represents one unit in the scene (e.g., a 10x10 rectangular item is drawn using 10x10 pixels in the view). If a 2x2 scaling matrix is applied, the scene will be drawn in 1:2 (e.g., a 10x10 rectangular item is then drawn using 20x20 pixels in the view).

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsview.py
    :lines: 138-143

To simplify interation with items using a transformed view, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` provides mapTo... and mapFrom... functions that can translate between scene and view coordinates. For example, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene` to map a view coordiate to a floating point scene coordinate, or :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapFromScene` to map from floating point scene coordinates to view coordinates.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.rotate`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.shear`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.translate`.
