.. sip:method-description::
    :status: todo
    :pysig: d30d6fd77773397ac43f04a90cda2075
    :realsig: (QAbstractItemModel*, const QString&, const QString&, const QString&, const QStringList&, const QStringList&, QObject*)
    :digest: 5f2db8dd8791bb0f84d3bf45d340ff66

Constructs :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy` with *itemModel* and an optional *parent*. The proxy doesn't take ownership of the *itemModel*, as typically item models are owned by other controls. The role mappings are set with *rowRole*, *columnRole*, and *valueRole*. Row and column categories are set with *rowCategories* and *columnCategories*. This constructor also sets :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy.autoRowCategories` and :sip:ref:`~PyQt6.QtGraphs.QItemModelBarDataProxy.autoColumnCategories` to false.
