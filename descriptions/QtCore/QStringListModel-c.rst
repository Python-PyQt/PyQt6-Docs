.. sip:class-description::
    :status: todo
    :brief: Model that supplies strings to views
    :digest: 7deeb4f7642a34cb7c64ac6e231c7780

The :sip:ref:`~PyQt6.QtCore.QStringListModel` class provides a model that supplies strings to views.

:sip:ref:`~PyQt6.QtCore.QStringListModel` is an editable model that can be used for simple cases where you need to display a number of strings in a view widget, such as a :sip:ref:`~PyQt6.QtWidgets.QListView` or a `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_.

The model provides all the standard functions of an editable model, representing the data in the string list as a model with one column and a number of rows equal to the number of items in the list.

Model indexes corresponding to items are obtained with the :sip:ref:`~PyQt6.QtCore.QAbstractListModel.index` function, and item flags are obtained with :sip:ref:`~PyQt6.QtCore.QStringListModel.flags`. Item data is read with the :sip:ref:`~PyQt6.QtCore.QStringListModel.data` function and written with :sip:ref:`~PyQt6.QtCore.QStringListModel.setData`. The number of rows (and number of items in the string list) can be found with the :sip:ref:`~PyQt6.QtCore.QStringListModel.rowCount` function.

The model can be constructed with an existing string list, or strings can be set later with the :sip:ref:`~PyQt6.QtCore.QStringListModel.setStringList` convenience function. Strings can also be inserted in the usual way with the :sip:ref:`~PyQt6.QtCore.QStringListModel.insertRows` function, and removed with :sip:ref:`~PyQt6.QtCore.QStringListModel.removeRows`. The contents of the string list can be retrieved with the :sip:ref:`~PyQt6.QtCore.QStringListModel.stringList` convenience function.

An example usage of :sip:ref:`~PyQt6.QtCore.QStringListModel`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qstringlistmodel-main.py
    :lines: 65-68

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractListModel`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, `Model Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-classes>`_.
