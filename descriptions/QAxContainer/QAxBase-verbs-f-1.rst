.. sip:method-description::
    :status: todo
    :pysig: 3c9a938a1e983dbe538fd869f2db5e67
    :realsig: () const
    :digest: cfe9bb019404f0c409a9fea4cb21e98f

Returns the list of verbs that the COM object can execute. If the object does not implement IOleObject, or does not support any verbs, then this function returns an empty stringlist.

Note that the OLE default verbs (OLEIVERB_SHOW etc) are not included in the list.
