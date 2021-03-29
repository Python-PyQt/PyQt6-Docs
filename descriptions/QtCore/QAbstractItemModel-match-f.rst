.. sip:method-description::
    :status: todo
    :pysig: 67ed920694bb7faedb6a7b17f20b8b1e
    :realsig: (const QModelIndex&,int,const QVariant&,int,Qt::MatchFlags) const
    :digest: 7b67c54287f930b4765bb602b19c163d

Returns a list of indexes for the items in the column of the *start* index where data stored under the given *role* matches the specified *value*. The way the search is performed is defined by the *flags* given. The list that is returned may be empty. Note also that the order of results in the list may not correspond to the order in the model, if for example a proxy model is used. The order of the results cannot be relied upon.

The search begins from the *start* index, and continues until the number of matching data items equals *hits*, the search reaches the last row, or the search reaches *start* again - depending on whether ``MatchWrap`` is specified in *flags*. If you want to search for all matching items, use *hits* = -1.

By default, this function will perform a wrapping, string-based comparison on all items, searching for items that begin with the search term specified by *value*.

**Note:** The default implementation of this function only searches columns. Reimplement this function to include a different search behavior.
