.. sip:method-description::
    :status: todo
    :pysig: 5e1bc25ca7b8fb138a4dd73c6add6af8
    :realsig: (QAbstractItemModel*,const QString&,const QString&,const QString&,const QStringList&,const QStringList&,QObject*)
    :digest: a47767f4e56a6f25f4c0cafb765893f4

Constructs :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy` with *itemModel* and optional *parent*. Proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, and *yPosRole*. The :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.zPosRole` and the :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.xPosRole` are set to *rowRole* and *columnRole*, respectively. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.autoColumnCategories` to false.
