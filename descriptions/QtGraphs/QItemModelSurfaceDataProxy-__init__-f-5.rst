.. sip:method-description::
    :status: todo
    :pysig: d30d6fd77773397ac43f04a90cda2075
    :realsig: (QAbstractItemModel*, const QString&, const QString&, const QString&, const QStringList&, const QStringList&, QObject*)
    :digest: a47767f4e56a6f25f4c0cafb765893f4

Constructs :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy` with *itemModel* and an optional *parent*. The proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, and *yPosRole*. The :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.zPosRole` and the :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.xPosRole` are set to *rowRole* and *columnRole*, respectively. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtGraphs.QItemModelSurfaceDataProxy.autoColumnCategories` to false.
