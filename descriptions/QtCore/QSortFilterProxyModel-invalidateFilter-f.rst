.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2febd84682e4c31e6a33362f844e89c3

Invalidates the current filtering.

This function should be called if you are implementing custom filtering (e.g. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameters have changed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidate`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateRowsFilter`.
