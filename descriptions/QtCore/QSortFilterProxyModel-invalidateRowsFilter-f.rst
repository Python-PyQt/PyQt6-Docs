.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b5391962b5d2140d535e91f543646672

Invalidates the current filtering for the rows.

This function should be called if you are implementing custom filtering (by :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`), and your filter parameters have changed. This differs from :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` in that it will not invoke :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn`, but only :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow`. You can use this instead of :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` if you want to hide or show a row where the columns don't change.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidate`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter`.
