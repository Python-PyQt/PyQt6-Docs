.. sip:class-description::
    :status: todo
    :brief: Proxies multiple source models, concatenating their rows
    :digest: 6bfe2a82d001687ff58d43301a665f83

The :sip:ref:`~PyQt6.QtCore.QConcatenateTablesProxyModel` class proxies multiple source models, concatenating their rows.

:sip:ref:`~PyQt6.QtCore.QConcatenateTablesProxyModel` takes multiple source models and concatenates their rows.

In other words, the proxy will have all rows of the first source model, followed by all rows of the second source model, and so on.

If the source models don't have the same number of columns, the proxy will only have as many columns as the source model with the smallest number of columns. Additional columns in other source models will simply be ignored.

Source models can be added and removed at runtime, and the column count is adjusted accordingly.

This proxy does not inherit from :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel` because it uses multiple source models, rather than a single one.

Only flat models (lists and tables) are supported, tree models are not.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`, :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.
