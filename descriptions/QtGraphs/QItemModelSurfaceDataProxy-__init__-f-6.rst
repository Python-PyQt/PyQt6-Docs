.. sip:method-description::
    :status: todo
    :pysig: 30b89e9a6635d24d5ba231a7360d5612
    :realsig: (QAbstractItemModel*, const QString&, const QString&, const QString&, const QString&, const QString&, const QStringList&, const QStringList&, QObject*)
    :digest: 2359f67662bc15fd5997ca4473507ea4

Constructs :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy` with *itemModel* and an optional *parent*. The proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, *xPosRole*, *yPosRole*, and *zPosRole*. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.autoColumnCategories` to false.
