.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e54e128172fbf16549944e0fa5aca0bc

Begins a model reset operation.

A reset operation resets the model to its current state in any attached views.

**Note:** Any views attached to this model will be reset as well.

When a model is reset it means that any previous data reported from the model is now invalid and has to be queried for again. This also means that the current item and any selected items will become invalid.

When a model radically changes its data it can sometimes be easier to just call this function rather than emit :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged` to inform other components when the underlying data source, or its structure, has changed.

You must call this function before resetting any internal data structures in your model or proxy model.

This function emits the signal :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelAboutToBeReset`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelAboutToBeReset`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelReset`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endResetModel`.
