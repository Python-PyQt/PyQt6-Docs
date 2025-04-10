.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e76ceeb493357c04db075a8e4bb034c6

Prepares a change of the filter.

This function should be called if you are implementing custom filtering (e.g. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameter is about to be changed.

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-itemviews-customsortfiltermodel-mysortfilterproxymodel.py
    :lines: 73-77

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateRowsFilter`.
