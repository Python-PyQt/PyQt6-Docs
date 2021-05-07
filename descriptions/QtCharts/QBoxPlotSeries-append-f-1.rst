.. sip:method-description::
    :status: todo
    :pysig: 10a2aa55367c19cbeacd581f4d52c0f4
    :realsig: (const QList<QBoxSet*>&)
    :digest: e6269b20d2253948457fb0a830410093

Adds a list of box-and-whiskers items specified by *sets* to the series and takes ownership of them. If the list is null or the items already belong to the series, it will not be appended. Returns ``true`` if appending succeeded.
