.. sip:method-description::
    :status: todo
    :pysig: e0cf5d0d5a40b40e11200ce52b3b8bce
    :realsig: (QAbstractItemModel*,const QString&,const QString&,const QString&,const QString&,const QStringList&,const QStringList&,QObject*)
    :digest: 9596e0ded38df7a06c91a33fc7bc082f

Constructs :sip:ref:`~PyQt6.QtDataVisualization.QItemModelBarDataProxy` with *itemModel* and optional *parent*. Proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, *valueRole*, and *rotationRole*. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtDataVisualization.QItemModelBarDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtDataVisualization.QItemModelBarDataProxy.autoColumnCategories` to false.
