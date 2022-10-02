.. sip:class-description::
    :status: todo
    :brief: Used to display and edit data items from a model
    :digest: 225180ba04c5dd943fae69fee683ae4b

The :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate` class is used to display and edit data items from a model.

A :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate` provides the interface and common functionality for delegates in the model/view architecture. Delegates display individual items in views, and handle the editing of model data.

The :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

To render an item in a custom way, you must implement :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.paint` and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.sizeHint`. The :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate` class provides default implementations for these functions; if you do not need custom rendering, subclass that class instead.

We give an example of drawing a progress bar in items; in our case for a package management program.

.. image:: ../../../images/widgetdelegate.png

We create the ``WidgetDelegate`` class, which inherits from :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`. We do the drawing in the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.paint` function:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-widgetdelegate.py

Notice that we use a :sip:ref:`~PyQt6.QtWidgets.QStyleOptionProgressBar` and initialize its members. We can then use the current :sip:ref:`~PyQt6.QtWidgets.QStyle` to draw it.

To provide custom editing, there are two approaches that can be used. The first approach is to create an editor widget and display it directly on top of the item. To do this you must reimplement :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.createEditor` to provide an editor widget, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setEditorData` to populate the editor with the data from the model, and :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.setModelData` so that the delegate can update the model with data from the editor.

The second approach is to handle user events directly by reimplementing :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.editorEvent`.

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, `Pixelator Example <https://doc.qt.io/qt-6/qtwidgets-itemviews-pixelator-example.html>`_, :sip:ref:`~PyQt6.QtWidgets.QStyledItemDelegate`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
