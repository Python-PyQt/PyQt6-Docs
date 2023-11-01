.. sip:method-description::
    :status: todo
    :pysig: a53f7396bebfe5931030f53fcdbc15a1
    :realsig: (QAbstractItemModel*, const QString&, QObject*)
    :digest: a3d609f066f0d24b8efc96865e86e638

Constructs :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy` with *itemModel* and optional *parent*. Proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.yPosRole` role is set to *yPosRole*. This constructor is meant to be used with models that have data properly sorted in rows and columns already, so it also sets :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.useModelCategories` property to ``true``.
