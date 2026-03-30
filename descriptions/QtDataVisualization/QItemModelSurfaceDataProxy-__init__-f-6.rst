.. sip:method-description::
    :status: todo
    :pysig: cb22d112d95a1170ac0d7a14c1976e78
    :realsig: (QAbstractItemModel*, const QString&, const QString&, const QString&, const QString&, const QString&, const QStringList&, const QStringList&, QObject*)
    :digest: 2359f67662bc15fd5997ca4473507ea4

Constructs :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy` with *itemModel* and optional *parent*. Proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, *xPosRole*, *yPosRole*, and *zPosRole*. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.autoColumnCategories` to false.
