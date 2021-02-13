.. sip:class-description::
    :status: todo
    :brief: Movable panel that contains a set of controls
    :digest: f008dfd91393b58874ef19c88d8200d5

The :sip:ref:`~PyQt6.QtWidgets.QToolBar` class provides a movable panel that contains a set of controls.

Toolbar buttons are added by adding *actions*, using :sip:ref:`~PyQt6.QtWidgets.QToolBar.addAction` or insertAction(). Groups of buttons can be separated using :sip:ref:`~PyQt6.QtWidgets.QToolBar.addSeparator` or :sip:ref:`~PyQt6.QtWidgets.QToolBar.insertSeparator`. If a toolbar button is not appropriate, a widget can be inserted instead using :sip:ref:`~PyQt6.QtWidgets.QToolBar.addWidget` or :sip:ref:`~PyQt6.QtWidgets.QToolBar.insertWidget`. Examples of suitable widgets are :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDoubleSpinBox`, and `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_. When a toolbar button is pressed, it emits the :sip:ref:`~PyQt6.QtWidgets.QToolBar.actionTriggered` signal.

A toolbar can be fixed in place in a particular area (e.g., at the top of the window), or it can be movable between toolbar areas; see :sip:ref:`~PyQt6.QtWidgets.QToolBar.setMovable`, :sip:ref:`~PyQt6.QtWidgets.QToolBar.isMovable`, :sip:ref:`~PyQt6.QtWidgets.QToolBar.allowedAreas` and :sip:ref:`~PyQt6.QtWidgets.QToolBar.isAreaAllowed`.

When a toolbar is resized in such a way that it is too small to show all the items it contains, an extension button will appear as the last item in the toolbar. Pressing the extension button will pop up a menu containing the items that do not currently fit in the toolbar.

When a :sip:ref:`~PyQt6.QtWidgets.QToolBar` is not a child of a :sip:ref:`~PyQt6.QtWidgets.QMainWindow`, it loses the ability to populate the extension pop up with widgets added to the toolbar using :sip:ref:`~PyQt6.QtWidgets.QToolBar.addWidget`. Please use widget actions created by inheriting :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` and implementing :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.createWidget` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QToolButton`, :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtGui.QAction`, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_.
