.. sip:method-description::
    :status: todo
    :pysig: a53f7396bebfe5931030f53fcdbc15a1
    :realsig: (QAbstractItemModel*, const QString&, QObject*)
    :digest: 006a2385bf27d76da9ff4d7c9d1f6177

Constructs :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy` with *itemModel* and an optional *parent*. The proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The value role is set to *valueRole*. This constructor is meant to be used with models that have data properly sorted in rows and columns already, so it also sets :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy.useModelCategories` property to true.
