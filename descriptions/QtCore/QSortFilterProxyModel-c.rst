.. sip:class-description::
    :status: todo
    :brief: Support for sorting and filtering data passed between another model and a view
    :digest: 8fa1f8e54857782cec483797323b2b74

The :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` class provides support for sorting and filtering data passed between another model and a view.

:sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` can be used for sorting items, filtering out items, or both. The model transforms the structure of a source model by mapping the model indexes it supplies to new indexes, corresponding to different locations, for views to use. This approach allows a given source model to be restructured as far as views are concerned without requiring any transformations on the underlying data, and without duplicating the data in memory.

Let's assume that we want to sort and filter the items provided by a custom model. The code to set up the model and the view, *without* sorting and filtering, would look like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsortfilterproxymodel-details-main.py
    :lines: 77-81

To add sorting and filtering support to ``MyItemModel``, we need to create a :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel`, call :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setSourceModel` with the ``MyItemModel`` as argument, and install the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` on the view:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsortfilterproxymodel-details-main.py
    :lines: 77-77

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsortfilterproxymodel-details-main.py
    :lines: 85-89

At this point, neither sorting nor filtering is enabled; the original data is displayed in the view. Any changes made through the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` are applied to the original model.

The :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` acts as a wrapper for the original model. If you need to convert source :sip:ref:`~PyQt6.QtCore.QModelIndex`\ es to sorted/filtered model indexes or vice versa, use :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.mapToSource`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.mapFromSource`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.mapSelectionToSource`, and :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.mapSelectionFromSource`.

**Note:** By default, the model dynamically re-sorts and re-filters data whenever the original model changes. This behavior can be changed by setting the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.dynamicSortFilter` property.

The `Basic Sort/Filter Model <https://doc.qt.io/qt-6/qtwidgets-itemviews-basicsortfiltermodel-example.html>`_ and `Custom Sort/Filter Model <https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html>`_ examples illustrate how to use :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` to perform basic sorting and filtering and how to subclass it to implement custom behavior.

.. _qsortfilterproxymodel-sorting:

Sorting
-------

:sip:ref:`~PyQt6.QtWidgets.QTableView` and :sip:ref:`~PyQt6.QtWidgets.QTreeView` have a sortingEnabled property that controls whether the user can sort the view by clicking the view's horizontal header. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsortfilterproxymodel-details-main.py
    :lines: 93-93

When this feature is on (the default is off), clicking on a header section sorts the items according to that column. By clicking repeatedly, the user can alternate between ascending and descending order.

.. image:: ../../../images/qsortfilterproxymodel-sorting.png

Behind the scene, the view calls the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sort` virtual function on the model to reorder the data in the model. To make your data sortable, you can either implement :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sort` in your model, or use a :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` to wrap your model -- :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` provides a generic :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sort` reimplementation that operates on the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sortRole` (\ :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` by default) of the items and that understands several data types, including ``int``, QString, and :sip:ref:`~PyQt6.QtCore.QDateTime`. For hierarchical models, sorting is applied recursively to all child items. String comparisons are case sensitive by default; this can be changed by setting the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sortCaseSensitivity` property.

Custom sorting behavior is achieved by subclassing :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` and reimplementing :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.lessThan`, which is used to compare items. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-itemviews-customsortfiltermodel-mysortfilterproxymodel.py
    :lines: 95-123

(This code snippet comes from the `Custom Sort/Filter Model <https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html>`_ example.)

An alternative approach to sorting is to disable sorting on the view and to impose a certain order to the user. This is done by explicitly calling :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sort` with the desired column and order as arguments on the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` (or on the original model if it implements :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.sort`). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsortfilterproxymodel-details-main.py
    :lines: 97-97

:sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` can be sorted by column -1, in which case it returns to the sort order of the underlying source model.

.. _qsortfilterproxymodel-filtering:

Filtering
---------

In addition to sorting, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` can be used to hide items that do not match a certain filter. The filter is specified using a `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object and is applied to the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterRole` (\ :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` by default) of each item, for a given column. The `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object can be used to match a regular expression, a wildcard pattern, or a fixed string. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qsortfilterproxymodel-details-main.py
    :lines: 99-100

For hierarchical models, the filter is applied recursively to all children. If a parent item doesn't match the filter, none of its children will be shown.

A common use case is to let the user specify the filter regular expression, wildcard pattern, or fixed string in a :sip:ref:`~PyQt6.QtWidgets.QLineEdit` and to connect the :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textChanged` signal to :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression`, :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard`, or :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString` to reapply the filter.

Custom filtering behavior can be achieved by reimplementing the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow` and :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn` functions. For example (from the `Custom Sort/Filter Model <https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html>`_ example), the following implementation ignores the :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.filterKeyColumn` property and performs filtering on columns 0, 1, and 2:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-itemviews-customsortfiltermodel-mysortfilterproxymodel.py
    :lines: 81-91

(This code snippet comes from the `Custom Sort/Filter Model <https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html>`_ example.)

If you are working with large amounts of filtering and have to invoke :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter` repeatedly, using beginResetModel() / endResetModel() may be more efficient, depending on the implementation of your model. However, beginResetModel() / endResetModel() returns the proxy model to its original state, losing selection information, and will cause the proxy model to be repopulated.

.. _qsortfilterproxymodel-subclassing:

Subclassing
-----------

Since :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel` and its subclasses are derived from :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, much of the same advice about subclassing normal models also applies to proxy models. In addition, it is worth noting that many of the default implementations of functions in this class are written so that they call the equivalent functions in the relevant source model. This simple proxying mechanism may need to be overridden for source models with more complex behavior; for example, if the source model provides a custom :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel.hasChildren` implementation, you should also provide one in the proxy model.

**Note:** Some general guidelines for subclassing models are available in the `Model Subclassing Reference <https://doc.qt.io/qt-6/model-view-programming.html#model-subclassing-reference>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, `Basic Sort/Filter Model Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-basicsortfiltermodel-example.html>`_, `Custom Sort/Filter Model Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-customsortfiltermodel-example.html>`_, :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel`.
