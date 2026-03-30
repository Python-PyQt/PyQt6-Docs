.. sip:method-description::
    :status: todo
    :pysig: 45d78fb07717c3e50e5678f81f3a922b
    :realsig: (QAbstractItemModel*, const QString&, QObject*)
    :digest: a3d609f066f0d24b8efc96865e86e638

Constructs :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy` with *itemModel* and an optional *parent*. The proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.yPosRole` role is set to *yPosRole*. This constructor is meant to be used with models that have data properly sorted in rows and columns already, so it also sets :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.useModelCategories` property to ``true``.
