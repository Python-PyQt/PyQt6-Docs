.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 41f4baad2d7787d5932c8a6646981739

use :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange` and :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.endFilterChange`\ (\ :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.Direction.Columns`) instead.

Invalidates the current filtering for the rows.

This function should be called if you are implementing custom filtering (by :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameters have changed. This differs from :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` in that it will not invoke :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn`, but only :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`. You can use this instead of :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` if you want to hide or show a row where the columns don't change.

Before your filter parameters change, call :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.beginFilterChange`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidate`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter`.
