.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 5fd495f309f1c2b01e79b43cbb5ad05d

Prepares a change of the filter.

This function should be called if you are implementing custom filtering (e.g. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameter is about to be changed.

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-itemviews-customsortfiltermodel-mysortfilterproxymodel.py
    :lines: 73-77

Once the filter has been changed, call :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.endFilterChange` with :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Rows` for row-filters, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Columns` for column-filters, or :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Columns`|\ :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Rows` if both rows and columns are filtered.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.endFilterChange`.
