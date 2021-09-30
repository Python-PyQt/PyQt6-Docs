.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 7ed11b70a7882827670accec435f8041

Sets the wildcard expression used to filter the contents of the source model to the given *pattern*.

This method will reset the regular expression options but respect case sensitivity.

**Note:** Calling this method updates the regular expression, thereby breaking the binding for :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`. However it has no effect on the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterCaseSensitivity` bindings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`.
