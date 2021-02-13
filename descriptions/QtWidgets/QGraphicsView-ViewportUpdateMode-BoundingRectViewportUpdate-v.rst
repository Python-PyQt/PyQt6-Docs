.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: 27cb0e8ed5d62973436e0f6f980e1d9d

The bounding rectangle of all changes in the viewport will be redrawn. This mode has the advantage that :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` searches only one region for changes, minimizing time spent determining what needs redrawing. The disadvantage is that areas that have not changed also need to be redrawn.
