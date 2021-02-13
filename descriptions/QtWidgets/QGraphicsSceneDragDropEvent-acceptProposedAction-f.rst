.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 71d72c217d2c116e3f895257feb25946

Sets the proposed action as accepted, i.e, the drop action is set to the proposed action. This is equal to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicssceneevent.py
    :lines: 54-56

When using this function, one should not call ``accept()``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.dropAction`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.setDropAction`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.proposedAction`.
