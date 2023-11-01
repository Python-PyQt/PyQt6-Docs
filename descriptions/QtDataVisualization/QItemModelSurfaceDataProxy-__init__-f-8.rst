.. sip:method-description::
    :status: todo
    :pysig: 87b0d0d4b0fc54a905de354806dbfdc1
    :realsig: (QAbstractItemModel*, const QString&, const QString&, const QString&, QObject*)
    :digest: 611a4b43ab3d103651084a9cbdbfaea6

Constructs :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy` with *itemModel* and optional *parent*. Proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, and *yPosRole*. The :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.zPosRole` and the :sip:ref:`~PyQt6.QtDataVisualization.QItemModelSurfaceDataProxy.xPosRole` are set to *rowRole* and *columnRole*, respectively.
