.. sip:method-description::
    :status: todo
    :pysig: 866cf4df96ec50c87e799ba998a2116b
    :realsig: (QSortFilterProxyModel::Directions)
    :digest: 3fef92081936e4fa9a9979f5bf1af0f1

Invalidates the current filtering after the filter parameter has changed.

This function should be called if you implement custom filtering (e.g. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameters have changed. The *directions* parameter specifies whether the custom filter impacts rows, columns, or both.

Call :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange` when the filter parameter is about to change, and follow with a call to this function once the filter parameters have been changed. Call with *directions* set to :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Rows` for row-filters (i.e. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow` is implemented), :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Columns` for column-filters (i.e. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn` is implemented), or ``Direction::Both`` if both filter functions are implemented.
