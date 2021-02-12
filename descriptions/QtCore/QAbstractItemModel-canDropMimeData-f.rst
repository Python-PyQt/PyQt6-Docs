.. sip:method-description::
    :status: todo
    :pysig: 6e63cde85334e414daad28e429b56d42
    :realsig: (const QMimeData*,Qt::DropAction,int,int,const QModelIndex&) const
    :digest: 2a569afc6381f2c87562231baf7bf71c

Returns ``true`` if a model can accept a drop of the *data*. This default implementation only checks if *data* has at least one format in the list of :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.mimeTypes` and if *action* is among the model's :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.supportedDropActions`.

Reimplement this function in your custom model, if you want to test whether the *data* can be dropped at *row*, *column*, *parent* with *action*. If you don't need that test, it is not necessary to reimplement this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData`.
