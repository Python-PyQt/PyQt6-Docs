.. sip:class-description::
    :status: todo
    :brief: The basic functionality for item view classes
    :digest: 17f485ffb8800208ee0f4313d941c15a

The :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` class provides the basic functionality for item view classes.

:sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` class is the base class for every standard view that uses a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`. :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` is an abstract class and cannot itself be instantiated. It provides a standard interface for interoperating with models through the signals and slots mechanism, enabling subclasses to be kept up-to-date with changes to their models. This class provides standard support for keyboard and mouse navigation, viewport scrolling, item editing, and selections. The keyboard navigation implements this functionality:

+-------------------+---------------------------------------------------------------------------------------------+
| Keys              | Functionality                                                                               |
+===================+=============================================================================================+
| Arrow keys        | Changes the current item and selects it.                                                    |
+-------------------+---------------------------------------------------------------------------------------------+
| Ctrl+Arrow keys   | Changes the current item but does not select it.                                            |
+-------------------+---------------------------------------------------------------------------------------------+
| Shift+Arrow keys  | Changes the current item and selects it. The previously selected item(s) is not deselected. |
+-------------------+---------------------------------------------------------------------------------------------+
| Ctr+Space         | Toggles selection of the current item.                                                      |
+-------------------+---------------------------------------------------------------------------------------------+
| Tab/Backtab       | Changes the current item to the next/previous item.                                         |
+-------------------+---------------------------------------------------------------------------------------------+
| Home/End          | Selects the first/last item in the model.                                                   |
+-------------------+---------------------------------------------------------------------------------------------+
| Page up/Page down | Scrolls the rows shown up/down by the number of visible rows in the view.                   |
+-------------------+---------------------------------------------------------------------------------------------+
| Ctrl+A            | Selects all items in the model.                                                             |
+-------------------+---------------------------------------------------------------------------------------------+

Note that the above table assumes that the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionMode` allows the operations. For instance, you cannot select items if the selection mode is :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.SelectionMode.NoSelection`.

The :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

The view classes that inherit :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` only need to implement their own view-specific functionality, such as drawing items, returning the geometry of items, finding items, etc.

:sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` provides common slots such as :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.edit` and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setCurrentIndex`. Many protected slots are also provided, including :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.dataChanged`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.rowsInserted`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.rowsAboutToBeRemoved`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionChanged`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.currentChanged`.

The root item is returned by :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.rootIndex`, and the current item by :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.currentIndex`. To make sure that an item is visible use :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.scrollTo`.

Some of :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`'s functions are concerned with scrolling, for example :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setHorizontalScrollMode` and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setVerticalScrollMode`. To set the range of the scroll bars, you can, for example, reimplement the view's :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.resizeEvent` function:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_itemviews_qabstractitemview.py
    :lines: 54-57

Note that the range is not updated until the widget is shown.

Several other functions are concerned with selection control; for example :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelectionMode`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelectionBehavior`. This class provides a default selection model to work with (\ :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.selectionModel`), but this can be replaced by using :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelectionModel` with an instance of :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`.

For complete control over the display and editing of items you can specify a delegate with :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setItemDelegate`.

:sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` provides a lot of protected functions. Some are concerned with editing, for example, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.edit`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.commitData`, whilst others are keyboard and mouse event handlers.

**Note:** If you inherit :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView` and intend to update the contents of the viewport, you should use viewport->\ :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.update` instead of :sip:ref:`~PyQt6.QtWidgets.QWidget.update` as all painting operations take place on the viewport.

.. seealso:: `View Classes <https://doc.qt.io/qt-6/model-view-programming.html#view-classes>`_, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, `Chart Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-chart-example.html>`_.
