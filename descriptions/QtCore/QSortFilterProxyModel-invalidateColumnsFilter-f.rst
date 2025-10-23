.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: dc19fbe73eb69834579c824796687ae6

use :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange` and :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.endFilterChange`\ (\ :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Rows`) instead.

Invalidates the current filtering for the columns.

This function should be called if you are implementing custom filtering (by :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn`), and your filter parameters have changed. This differs from :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` in that it will not invoke :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`, but only :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn`. You can use this instead of :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` if you want to hide or show a column where the rows don't change.

Before your filter parameters change, call :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidate`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateRowsFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange`.
