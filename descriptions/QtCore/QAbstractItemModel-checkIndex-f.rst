.. sip:method-description::
    :status: todo
    :pysig: 8937ee45c6dad9c63830562d69dcefb7
    :realsig: (const QModelIndex&,QAbstractItemModel::CheckIndexOptions) const
    :digest: 2d2fd4bb5d1ed4a05c01b96ec07cb8eb

This function checks whether *index* is a legal model index for this model. A legal model index is either an invalid model index, or a valid model index for which all the following holds:

* the index' model is ``this``;

* the index' row is greater or equal than zero;

* the index' row is less than the row count for the index' parent;

* the index' column is greater or equal than zero;

* the index' column is less than the column count for the index' parent.

The *options* argument may change some of these checks. If *options* contains ``IndexIsValid``, then *index* must be a valid index; this is useful when reimplementing functions such as :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` or :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.setData`, which expect valid indexes.

If *options* contains ``DoNotUseParent``, then the checks that would call :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.parent` are omitted; this allows calling this function from a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.parent` reimplementation (otherwise, this would result in endless recursion and a crash).

If *options* does not contain ``DoNotUseParent``, and it contains ``ParentIsInvalid``, then an additional check is performed: the parent index is checked for not being valid. This is useful when implementing flat models such as lists or tables, where no model index should have a valid parent index.

This function returns true if all the checks succeeded, and false otherwise. This allows to use the function in Q_ASSERT and similar other debugging mechanisms. If some check failed, a warning message will be printed in the ``qt.core.qabstractitemmodel.checkindex`` logging category, containing some information that may be useful for debugging the failure.

**Note:** This function is a debugging helper for implementing your own item models. When developing complex models, as well as when building complicated model hierarchies (e.g. using proxy models), it is useful to call this function in order to catch bugs relative to illegal model indices (as defined above) accidentally passed to some :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` API.

**Warning:** Note that it's undefined behavior to pass illegal indices to item models, so applications must refrain from doing so, and not rely on any "defensive" programming that item models could employ to handle illegal indexes gracefully.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QModelIndex`.
