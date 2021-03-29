.. sip:method-description::
    :status: todo
    :pysig: cecc065eef5b5bf94de5ed2feb733240
    :realsig: (int,const QModelIndex&) const
    :digest: 5be21b73dad6310adb1c43605d84301e

Returns ``true`` if the item in the column indicated by the given *source_column* and *source_parent* should be included in the model; otherwise returns ``false``.

**Note:** The default implementation always returns ``true``. You must reimplement this method to get the described behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`.
