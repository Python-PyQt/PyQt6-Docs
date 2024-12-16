.. sip:class-description::
    :status: todo
    :brief: Display and editing facilities for data items from a model
    :digest: 256ca61d320e1bbf356ebf2cf23efc5e

The :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` class provides display and editing facilities for data items from a model.

When displaying data from models in Qt item views, e.g., a :sip:ref:`~PyQt6.QtWidgets.QTableView`, the individual items are drawn by a delegate. Also, when an item is edited, it provides an editor widget, which is placed on top of the item view while editing takes place. :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` is the default delegate for all Qt item views, and is installed upon them when they are created.

The :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#the-model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_. The delegate allows the display and editing of items to be developed independently from the model and view.

The data of items in models are assigned an :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole`; each item can store a :sip:ref:`~PyQt6.QtCore.QVariant` for each role. :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` implements display and editing for the most common datatypes expected by users, including booleans, integers, and strings.

The data will be drawn differently depending on which role they have in the model. The following table describes the roles and the data types the delegate can handle for each of them. It is often sufficient to ensure that the model returns appropriate data for each of the roles to determine the appearance of items in views.

+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Role                                                       | Accepted Types                                                                                                                    |
+============================================================+===================================================================================================================================+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.BackgroundRole`    | :sip:ref:`~PyQt6.QtGui.QBrush`                                                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.CheckStateRole`    | :sip:ref:`~PyQt6.QtCore.Qt.CheckState`                                                                                            |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DecorationRole`    | :sip:ref:`~PyQt6.QtGui.QIcon`, :sip:ref:`~PyQt6.QtGui.QPixmap`, :sip:ref:`~PyQt6.QtGui.QImage` and :sip:ref:`~PyQt6.QtGui.QColor` |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`       | QString and types with a string representation                                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`          | See :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` for details                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.FontRole`          | :sip:ref:`~PyQt6.QtGui.QFont`                                                                                                     |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.SizeHintRole`      | :sip:ref:`~PyQt6.QtCore.QSize`                                                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.TextAlignmentRole` | Qt::Alignment                                                                                                                     |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.ForegroundRole`    | :sip:ref:`~PyQt6.QtGui.QBrush`                                                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

Editors are created with a :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory`; a default static instance provided by :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` is installed on all item delegates. You can set a custom factory using :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.setItemEditorFactory` or set a new default factory with :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory.setDefaultFactory`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qitemeditorfactory.py

After the new factory has been set, all standard item delegates will use it (i.e, also delegates that were created before the new default factory was set).

It is the data stored in the item model with the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole` that is edited. See the :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory` class for a more high-level introduction to item editor factories.

.. _qstyleditemdelegate-subclassing-qstyleditemdelegate:

Subclassing QStyledItemDelegate
-------------------------------

If the delegate does not support painting of the data types you need or you want to customize the drawing of items, you need to subclass :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`, and reimplement :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.paint` and possibly :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.sizeHint`. The :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.paint` function is called individually for each item, and with :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.sizeHint`, you can specify the hint for each of them.

When reimplementing :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.paint`, one would typically handle the datatypes one would like to draw and use the superclass implementation for other types.

The painting of check box indicators are performed by the current style. The style also specifies the size and the bounding rectangles in which to draw the data for the different data roles. The bounding rectangle of the item itself is also calculated by the style. When drawing already supported datatypes, it is therefore a good idea to ask the style for these bounding rectangles. The :sip:ref:`~PyQt6.QtWidgets.QStyle` class description describes this in more detail.

If you wish to change any of the bounding rectangles calculated by the style or the painting of check box indicators, you can subclass :sip:ref:`~PyQt6.QtWidgets.QStyle`. Note, however, that the size of the items can also be affected by reimplementing :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.sizeHint`.

It is possible for a custom delegate to provide editors without the use of an editor item factory. In this case, the following virtual functions must be reimplemented:

* :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.createEditor` returns the widget used to change data from the model and can be reimplemented to customize editing behavior.

* :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.setEditorData` provides the widget with data to manipulate.

* :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.updateEditorGeometry` ensures that the editor is displayed correctly with respect to the item view.

* :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate.setModelData` returns updated data to the model.

The `Star Delegate <https://doc.qt.io/qt-6/qtwidgets-itemviews-stardelegate-example.html>`_ example creates editors by reimplementing these methods.

.. _qstyleditemdelegate-qstyleditemdelegate-vs-qitemdelegate:

QStyledItemDelegate vs. QItemDelegate
-------------------------------------

Since Qt 4.4, there are two delegate classes: :sip:ref:`~PyQt6.QtWidgets.QItemDelegate` and :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`. However, the default delegate is :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`. These two classes are independent alternatives to painting and providing editors for items in views. The difference between them is that :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` uses the current style to paint its items. We therefore recommend using :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` as the base class when implementing custom delegates or when working with Qt style sheets. The code required for either class should be equal unless the custom delegate needs to use the style for drawing.

If you wish to customize the painting of item views, you should implement a custom style. Please see the :sip:ref:`~PyQt6.QtWidgets.QStyle` class documentation for details.

.. seealso:: `Delegate Classes <https://doc.qt.io/qt-6/model-view-programming.html#delegate-classes>`_, :sip:ref:`~PyQt6.QtWidgets.QItemDelegate`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`, :sip:ref:`~PyQt6.QtWidgets.QStyle`, `Star Delegate Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-stardelegate-example.html>`_.
