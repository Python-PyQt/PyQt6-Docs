.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: cd31139f154fea5f4769eec79e34ecae

This slot is called when sections are inserted into the *parent*. *logicalFirst* and *logicalLast* indices signify where the new sections were inserted.

If only one section is inserted, *logicalFirst* and *logicalLast* will be the same.
