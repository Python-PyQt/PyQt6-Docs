.. sip:method-description::
    :status: todo
    :pysig: d4492a13818022be6671f3a7fc12bcaa
    :realsig: (QWidget*,const QModelIndex&) const
    :digest: 82469755f02979c782eb913cdde03dc6

Called when the *editor* is no longer needed for editing the data item with the given *index* and should be destroyed. The default behavior is a call to deleteLater on the editor. It is possible e.g. to avoid this delete by reimplementing this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.createEditor`.
