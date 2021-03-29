.. sip:method-description::
    :status: todo
    :pysig: eae522d5e7dd956b3354af2f7f910875
    :realsig: (QEvent*,QAbstractItemModel*,const QStyleOptionViewItem&,const QModelIndex&)
    :digest: 6e942efd446f4ca5fbbeaafd9c05e9b0

When editing of an item starts, this function is called with the *event* that triggered the editing, the *model*, the *index* of the item, and the *option* used for rendering the item.

Mouse events are sent to  even if they don't start editing of the item. This can, for instance, be useful if you wish to open a context menu when the right mouse button is pressed on an item.

The base implementation returns ``false`` (indicating that it has not handled the event).
