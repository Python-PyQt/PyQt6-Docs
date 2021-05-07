.. sip:method-description::
    :status: todo
    :pysig: f96f3c238b7a27038ccd0c6e71900feb
    :realsig: (Qt::DropAction)
    :digest: 5dae0363dbf8db618db26d027d9047e4

This function lets the receiver of the drop set the drop action that was performed to *action*, which should be one of the :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.possibleActions`. Call ``accept()`` in stead of ``acceptProposedAction()`` if you use this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.dropAction`, accept(), :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent.possibleActions`.
