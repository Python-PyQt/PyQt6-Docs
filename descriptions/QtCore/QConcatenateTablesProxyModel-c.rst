.. sip:class-description::
    :status: todo
    :brief: Proxies multiple source models, concatenating their rows
    :digest: 97a32cb4288138399471a99f86ba4507

The :sip:ref:`~PyQt6.QtCore.QConcatenateTablesProxyModel` class proxies multiple source models, concatenating their rows.

:sip:ref:`~PyQt6.QtCore.QConcatenateTablesProxyModel` takes multiple source models and concatenates their rows.

In other words, the proxy will have all rows of the first source model, followed by all rows of the second source model, and so on.

If the source models don't have the same number of columns, the proxy will only have as many columns as the source model with the smallest number of columns. Additional columns in other source models will simply be ignored.

Source models can be added and removed at runtime, and the column count is adjusted accordingly.

This proxy does not inherit from :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel` because it uses multiple source models, rather than a single one.

Only flat models (lists and tables) are supported, tree models are not.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.
