.. sip:method-description::
    :status: todo
    :pysig: 28019a57f7648f93372af030e53c2c9e
    :realsig: (const QModelIndex&,const QModelIndex&,const QList<int>&)
    :digest: 00caf9e3e9dee15d09e3bcafd6b8eeac

This slot is called when items with the given *roles* are changed in the model. The changed items are those from *topLeft* to *bottomRight* inclusive. If just one item is changed *topLeft* == *bottomRight*.

The *roles* which have been changed can either be an empty container (meaning everything has changed), or a non-empty container with the subset of roles which have changed.

**Note:** : :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.ToolTipRole` is not honored by  in the views provided by Qt.
