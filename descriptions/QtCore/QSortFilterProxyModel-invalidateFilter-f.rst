.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7f5655f20cc2389b5f20dad217f1386a

use :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange` and :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.endFilterChange` instead.

Invalidates the current filtering.

This function should be called if you are implementing custom filtering (e.g. :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameters have changed.

Before your filter parameters change, call :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange`.

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-itemviews-customsortfiltermodel-mysortfilterproxymodel.py
    :lines: 73-77

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidate`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateRowsFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange`.
