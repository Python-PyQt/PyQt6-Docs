.. sip:method-description::
    :status: todo
    :pysig: f4696c2e3213eeb713abb7e8ec352d99
    :realsig: (QWidget*,const QStyleOptionViewItem&,const QModelIndex&) const
    :digest: ca10f41235a19c4bc0e06cdf1ad292ab

Updates the geometry of the *editor* for the item with the given *index*, according to the rectangle specified in the *option*. If the item has an internal layout, the editor will be laid out accordingly. Note that the index contains information about the model being used.

The base implementation does nothing. If you want custom editing you must reimplement this function.
