.. sip:method-description::
    :status: todo
    :pysig: c073b02b82df741ccd08995eb1e8a77a
    :realsig: (QAbstractProxyModel*)
    :digest: 266acdb995c882bcf5aa74d69df62126

Sets the model for the views to the given *proxyModel*. This is useful if you want to modify the underlying model; for example, to add columns, filter data or add drives.

Any existing proxy model is removed, but not deleted. The file dialog takes ownership of the *proxyModel*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.proxyModel`.
