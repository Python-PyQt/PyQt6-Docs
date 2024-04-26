.. sip:class-description::
    :status: todo
    :brief: Display and editing facilities for data items from a model
    :digest: 910f75883bd7a6847223c5b1189b5c7b

The :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` class provides display and editing facilities for data items from a model.

:sip:ref:`~PyQt6.QtWidgets.QItemDelegate` can be used to provide custom display features and editor widgets for item views based on :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` subclasses. Using a delegate for this purpose allows the display and editing mechanisms to be customized and developed independently from the model and view.

The :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_. Note that :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` has taken over the job of drawing Qt's item views. We recommend the use of :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` when creating new delegates.

When displaying items from a custom model in a standard view, it is often sufficient to simply ensure that the model returns appropriate data for each of the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole` that determine the appearance of items in views. The default delegate used by Qt's standard views uses this role information to display items in most of the common forms expected by users. However, it is sometimes necessary to have even more control over the appearance of items than the default delegate can provide.

This class provides default implementations of the functions for painting item data in a view and editing data from item models. Default implementations of the :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.paint` and :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.sizeHint` virtual functions, defined in :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`, are provided to ensure that the delegate implements the correct basic behavior expected by views. You can reimplement these functions in subclasses to customize the appearance of items.

When editing data in an item view, :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` provides an editor widget, which is a widget that is placed on top of the view while editing takes place. Editors are created with a :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory`; a default static instance provided by :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` is installed on all item delegates. You can set a custom factory using :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.setItemEditorFactory` or set a new default factory with :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory.setDefaultFactory`. It is the data stored in the item model with the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` that is edited.

Only the standard editing functions for widget-based delegates are reimplemented here:

* :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.createEditor` returns the widget used to change data from the model and can be reimplemented to customize editing behavior.

* :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.setEditorData` provides the widget with data to manipulate.

* :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.updateEditorGeometry` ensures that the editor is displayed correctly with respect to the item view.

* :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.setModelData` returns updated data to the model.

The closeEditor() signal indicates that the user has completed editing the data, and that the editor widget can be destroyed.

.. _qitemdelegate-standard-roles-and-data-types:

Standard Roles and Data Types
-----------------------------

The default delegate used by the standard views supplied with Qt associates each standard role (defined by :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`) with certain data types. Models that return data in these types can influence the appearance of the delegate as described in the following table.

+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Role                                                       | Accepted Types                                                                                    |
+============================================================+===================================================================================================+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.BackgroundRole`    | :sip:ref:`~PyQt6.QtGui.QBrush` (                                                                  |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.CheckStateRole`    | :sip:ref:`~PyQt6.QtCore.Qt.CheckState`                                                            |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DecorationRole`    | :sip:ref:`~PyQt6.QtGui.QIcon`, :sip:ref:`~PyQt6.QtGui.QPixmap` and :sip:ref:`~PyQt6.QtGui.QColor` |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`       | QString and types with a string representation                                                    |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`          | See :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` for details                                    |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.FontRole`          | :sip:ref:`~PyQt6.QtGui.QFont`                                                                     |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.SizeHintRole`      | :sip:ref:`~PyQt6.QtCore.QSize`                                                                    |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.TextAlignmentRole` | Qt::Alignment                                                                                     |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.ForegroundRole`    | :sip:ref:`~PyQt6.QtGui.QBrush` (                                                                  |
+------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

If the default delegate does not allow the level of customization that you need, either for display purposes or for editing data, it is possible to subclass :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` to implement the desired behavior.

.. _qitemdelegate-subclassing:

Subclassing
-----------

When subclassing :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` to create a delegate that displays items using a custom renderer, it is important to ensure that the delegate can render items suitably for all the required states; e.g. selected, disabled, checked. The documentation for the :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.paint` function contains some hints to show how this can be achieved.

You can provide custom editors by using a :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory`. The `Color Editor Factory Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-coloreditorfactory-example.html>`_ shows how a custom editor can be made available to delegates with the default item editor factory. This way, there is no need to subclass :sip:ref:`~PyQt6.QtWidgets.QItemDelegate`. An alternative is to reimplement :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.createEditor`, :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.setEditorData`, :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.setModelData`, and :sip:ref:`~PyQt6.QtWidgets.QItemDelegate.updateEditorGeometry`. This process is described in the `Model/View Programming overview documentation <https://doc.qt.io/qt-6/model-view-programming.html#a-simple-delegate>`_.

.. _qitemdelegate-qstyleditemdelegate-vs-qitemdelegate:

QStyledItemDelegate vs. QItemDelegate
-------------------------------------

Since Qt 4.4, there are two delegate classes: :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` and :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`. However, the default delegate is :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`. These two classes are independent alternatives to painting and providing editors for items in views. The difference between them is that :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` uses the current style to paint its items. We therefore recommend using :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` as the base class when implementing custom delegates or when working with Qt style sheets. The code required for either class should be equal unless the custom delegate needs to use the style for drawing.

.. seealso:: `Delegate Classes <https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes>`_, :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`.
