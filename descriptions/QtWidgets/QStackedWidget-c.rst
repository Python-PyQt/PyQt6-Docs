.. sip:class-description::
    :status: todo
    :brief: Stack of widgets where only one widget is visible at a time
    :digest: c9613faf8869176d1a3fece871ce334a

The :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` class provides a stack of widgets where only one widget is visible at a time.

:sip:ref:`~PyQt6.QtWidgets.QStackedWidget` can be used to create a user interface similar to the one provided by :sip:ref:`~PyQt6.QtWidgets.QTabWidget`. It is a convenience layout widget built on top of the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout` class.

Like :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` can be constructed and populated with a number of child widgets ("pages"):

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedwidget-main.py
    :lines: 65-73

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedwidget-main.py
    :lines: 83-83

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedwidget-main.py
    :lines: 87-88

:sip:ref:`~PyQt6.QtWidgets.QStackedWidget` provides no intrinsic means for the user to switch page. This is typically done through a `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_ or a :sip:ref:`~PyQt6.QtWidgets.QListWidget` that stores the titles of the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`'s pages. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedwidget-main.py
    :lines: 75-81

When populating a stacked widget, the widgets are added to an internal list. The :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.indexOf` function returns the index of a widget in that list. The widgets can either be added to the end of the list using the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.addWidget` function, or inserted at a given index using the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.insertWidget` function. The :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.removeWidget` function removes a widget from the stacked widget. The number of widgets contained in the stacked widget can be obtained using the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.count` function.

The :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.widget` function returns the widget at a given index position. The index of the widget that is shown on screen is given by :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.currentIndex` and can be changed using :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.setCurrentIndex`. In a similar manner, the currently shown widget can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.currentWidget` function, and altered using the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.setCurrentWidget` function.

Whenever the current widget in the stacked widget changes or a widget is removed from the stacked widget, the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.currentChanged` and :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.widgetRemoved` signals are emitted respectively.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`, :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.
