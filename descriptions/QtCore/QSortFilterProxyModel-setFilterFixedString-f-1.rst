.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 884a9a444c00222e992280390824371a

Sets the fixed string used to filter the contents of the source model to the given *pattern*.

This method will reset the regular expression options but respect case sensitivity.

**Note:** Calling this method updates the regular expression, thereby breaking the binding for :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`. However it has no effect on the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterCaseSensitivity` bindings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`.
