.. sip:method-description::
    :status: todo
    :pysig: 79102708bbd5744b924d11580c5a6768
    :realsig: (const QModelIndex&,int,int)
    :digest: 406ee16e895c178efbce3d17acf93397

This slot is called when sections are removed from the *parent*. *logicalFirst* and *logicalLast* signify where the sections were removed.

If only one section is removed, *logicalFirst* and *logicalLast* will be the same.
