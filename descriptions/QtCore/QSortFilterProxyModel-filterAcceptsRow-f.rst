.. sip:method-description::
    :status: todo
    :pysig: cecc065eef5b5bf94de5ed2feb733240
    :realsig: (int,const QModelIndex&) const
    :digest: 2d32c98168b2752b14b87f2f9a84fbf8

Returns ``true`` if the item in the row indicated by the given *source_row* and *source_parent* should be included in the model; otherwise returns false.

The default implementation returns ``true`` if the value held by the relevant item matches the filter string, wildcard string or regular expression.

**Note:** By default, the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` is used to determine if the row should be accepted or not. This can be changed by setting the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRole` property.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`.
