.. sip:method-description::
    :status: todo
    :pysig: a34fd3e57af0cc79ef189995220041c2
    :realsig: () const
    :digest: cfe9bb019404f0c409a9fea4cb21e98f

Returns the list of verbs that the COM object can execute. If the object does not implement IOleObject, or does not support any verbs, then this function returns an empty stringlist.

Note that the OLE default verbs (OLEIVERB_SHOW etc) are not included in the list.
