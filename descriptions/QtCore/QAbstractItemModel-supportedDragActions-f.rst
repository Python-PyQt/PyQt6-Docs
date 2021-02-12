.. sip:method-description::
    :status: todo
    :pysig: b730747ccdc682ff41f5a1b741c1a110
    :realsig: () const
    :digest: 5645af4c94825bf0ee5048de60929c22

Returns the actions supported by the data in this model.

The default implementation returns :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.supportedDropActions`. Reimplement this function if you wish to support additional actions.

is used by QAbstractItemView::startDrag() as the default values when a drag occurs.

.. seealso:: Qt::DropActions.
