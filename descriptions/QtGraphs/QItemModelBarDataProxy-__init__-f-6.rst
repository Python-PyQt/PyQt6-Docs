.. sip:method-description::
    :status: todo
    :pysig: d91ddf5b30f7d62253bdfc91dcfb4f96
    :realsig: (QAbstractItemModel*, const QString&, const QString&, const QString&, const QString&, const QStringList&, const QStringList&, QObject*)
    :digest: 9596e0ded38df7a06c91a33fc7bc082f

Constructs :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy` with *itemModel* and an optional *parent*. The proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, *valueRole*, and *rotationRole*. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy.autoColumnCategories` to false.
