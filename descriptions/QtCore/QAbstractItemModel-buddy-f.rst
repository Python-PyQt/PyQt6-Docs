.. sip:method-description::
    :status: todo
    :pysig: c2435248c7dc5a666882a323b22b1429
    :realsig: (const QModelIndex&) const
    :digest: 85865ecf22d6b26a5d9e3070ab27e45a

Returns a model index for the buddy of the item represented by *index*. When the user wants to edit an item, the view will call this function to check whether another item in the model should be edited instead. Then, the view will construct a delegate using the model index returned by the buddy item.

The default implementation of this function has each item as its own buddy.
