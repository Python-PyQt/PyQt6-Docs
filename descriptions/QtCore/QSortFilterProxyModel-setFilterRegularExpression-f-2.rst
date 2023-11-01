.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 94f85984a247d77bfd09ed35466ad0ac

Sets the regular expression used to filter the contents of the source model to *pattern*.

This method should be preferred for new code as it will use :sip:ref:`~PyQt6.QtCore.QRegularExpression` internally.

This method will reset the regular expression options but respect case sensitivity.

**Note:** Calling this method updates the regular expression, thereby breaking the binding for :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`. However it has no effect on the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterCaseSensitivity` bindings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression`.
