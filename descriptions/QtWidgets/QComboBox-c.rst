.. sip:class-description::
    :status: todo
    :brief: Combined button and popup list
    :digest: d3d157d38f8d577366eccfa27188633d

The :sip:ref:`~PyQt6.QtWidgets.QComboBox` widget is a combined button and popup list.

.. image:: ../../../images/windows-combobox.png

A :sip:ref:`~PyQt6.QtWidgets.QComboBox` provides a means of presenting a list of options to the user in a way that takes up the minimum amount of screen space.

A combobox is a selection widget that displays the current item, and can pop up a list of selectable items. A combobox may be editable, allowing the user to modify each item in the list.

Comboboxes can contain pixmaps as well as strings; the :sip:ref:`~PyQt6.QtWidgets.QComboBox.insertItem` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.setItemText` functions are suitably overloaded. For editable comboboxes, the function :sip:ref:`~PyQt6.QtWidgets.QComboBox.clearEditText` is provided, to clear the displayed string without changing the combobox's contents.

There are three signals emitted if the current item of a combobox changes, :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentIndexChanged`, :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentTextChanged` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.activated`. :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentIndexChanged` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentTextChanged` are always emitted regardless if the change was done programmatically or by user interaction, while :sip:ref:`~PyQt6.QtWidgets.QComboBox.activated` is only emitted when the change is caused by user interaction. The :sip:ref:`~PyQt6.QtWidgets.QComboBox.highlighted` signal is emitted when the user highlights an item in the combobox popup list. All three signals exist in two versions, one with a QString argument and one with an ``int`` argument. If the user selects or highlights a pixmap, only the ``int`` signals are emitted. Whenever the text of an editable combobox is changed the :sip:ref:`~PyQt6.QtWidgets.QComboBox.editTextChanged` signal is emitted.

When the user enters a new string in an editable combobox, the widget may or may not insert it, and it can insert it in several locations. The default policy is :sip:ref:`~PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertAtBottom` but you can change this using :sip:ref:`~PyQt6.QtWidgets.QComboBox.setInsertPolicy`.

It is possible to constrain the input to an editable combobox using :sip:ref:`~PyQt6.QtGui.QValidator`; see :sip:ref:`~PyQt6.QtWidgets.QComboBox.setValidator`. By default, any input is accepted.

A combobox can be populated using the insert functions, :sip:ref:`~PyQt6.QtWidgets.QComboBox.insertItem` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.insertItems` for example. Items can be changed with :sip:ref:`~PyQt6.QtWidgets.QComboBox.setItemText`. An item can be removed with :sip:ref:`~PyQt6.QtWidgets.QComboBox.removeItem` and all items can be removed with :sip:ref:`~PyQt6.QtWidgets.QComboBox.clear`. The text of the current item is returned by :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentText`, and the text of a numbered item is returned with text(). The current item can be set with :sip:ref:`~PyQt6.QtWidgets.QComboBox.setCurrentIndex`. The number of items in the combobox is returned by :sip:ref:`~PyQt6.QtWidgets.QComboBox.count`; the maximum number of items can be set with :sip:ref:`~PyQt6.QtWidgets.QComboBox.setMaxCount`. You can allow editing using . For editable comboboxes you can set auto-completion using :sip:ref:`~PyQt6.QtWidgets.QComboBox.setCompleter` and whether or not the user can add duplicates is set with :sip:ref:`~PyQt6.QtWidgets.QComboBox.setDuplicatesEnabled`.

:sip:ref:`~PyQt6.QtWidgets.QComboBox` uses the `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_ for its popup list and to store its items. By default a :sip:ref:`~PyQt6.QtGui.QStandardItemModel` stores the items and a :sip:ref:`~PyQt6.QtWidgets.QListView` subclass displays the popuplist. You can access the model and view directly (with :sip:ref:`~PyQt6.QtWidgets.QComboBox.model` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.view`), but :sip:ref:`~PyQt6.QtWidgets.QComboBox` also provides functions to set and get item data (e.g., :sip:ref:`~PyQt6.QtWidgets.QComboBox.setItemData` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.itemText`). You can also set a new model and view (with :sip:ref:`~PyQt6.QtWidgets.QComboBox.setModel` and :sip:ref:`~PyQt6.QtWidgets.QComboBox.setView`). For the text and icon in the combobox label, the data in the model that has the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole` and :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DecorationRole` is used. Note that you cannot alter the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.SelectionMode` of the :sip:ref:`~PyQt6.QtWidgets.QComboBox.view`, e.g., by using :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setSelectionMode`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QRadioButton`, :sip:ref:`~PyQt6.QtWidgets.QButtonGroup`.
