.. sip:method-description::
    :status: todo
    :pysig: 54a5e8e51a9370586327f84486918a43
    :realsig: (const QModelIndex&,int,int,const QModelIndex&,int)
    :digest: 85adf659e0ba405dc1e816c05a5a47e4

Begins a column move operation.

When reimplementing a subclass, this method simplifies moving entities in your model. This method is responsible for moving persistent indexes in the model, which you would otherwise be required to do yourself. Using beginMoveColumns and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endMoveColumns` is an alternative to emitting :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutAboutToBeChanged` and :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.layoutChanged` directly along with :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.changePersistentIndex`.

The *sourceParent* index corresponds to the parent from which the columns are moved; *sourceFirst* and *sourceLast* are the first and last column numbers of the columns to be moved. The *destinationParent* index corresponds to the parent into which those columns are moved. The *destinationChild* is the column to which the columns will be moved. That is, the index at column *sourceFirst* in *sourceParent* will become column *destinationChild* in *destinationParent*, followed by all other columns up to *sourceLast*.

However, when moving columns down in the same parent (\ *sourceParent* and *destinationParent* are equal), the columns will be placed before the *destinationChild* index. That is, if you wish to move columns 0 and 1 so they will become columns 1 and 2, *destinationChild* should be 3. In this case, the new index for the source column ``i`` (which is between *sourceFirst* and *sourceLast*) is equal to ``(destinationChild-sourceLast-1+i)``.

Note that if *sourceParent* and *destinationParent* are the same, you must ensure that the *destinationChild* is not within the range of *sourceFirst* and *sourceLast* + 1. You must also ensure that you do not attempt to move a column to one of its own children or ancestors. This method returns ``false`` if either condition is true, in which case you should abort your move operation.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.endMoveColumns`.
