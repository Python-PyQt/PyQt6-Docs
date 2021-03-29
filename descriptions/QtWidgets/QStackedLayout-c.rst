.. sip:class-description::
    :status: todo
    :brief: Stack of widgets where only one widget is visible at a time
    :digest: 0fe88b9b53f6a341907b2bcb710f4825

The :sip:ref:`~PyQt6.QtWidgets.QStackedLayout` class provides a stack of widgets where only one widget is visible at a time.

:sip:ref:`~PyQt6.QtWidgets.QStackedLayout` can be used to create a user interface similar to the one provided by :sip:ref:`~PyQt6.QtWidgets.QTabWidget`. There is also a convenience :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` class built on top of :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`.

A :sip:ref:`~PyQt6.QtWidgets.QStackedLayout` can be populated with a number of child widgets ("pages"). For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedlayout-main.py
    :lines: 65-73

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedlayout-main.py
    :lines: 84-84

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedlayout-main.py
    :lines: 88-89

:sip:ref:`~PyQt6.QtWidgets.QStackedLayout` provides no intrinsic means for the user to switch page. This is typically done through a `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_ or a :sip:ref:`~PyQt6.QtWidgets.QListWidget` that stores the titles of the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`'s pages. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qstackedlayout-main.py
    :lines: 75-80

When populating a layout, the widgets are added to an internal list. The indexOf() function returns the index of a widget in that list. The widgets can either be added to the end of the list using the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.addWidget` function, or inserted at a given index using the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.insertWidget` function. The removeWidget() function removes the widget at the given index from the layout. The number of widgets contained in the layout, can be obtained using the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.count` function.

The :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.widget` function returns the widget at a given index position. The index of the widget that is shown on screen is given by :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.currentIndex` and can be changed using :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.setCurrentIndex`. In a similar manner, the currently shown widget can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.currentWidget` function, and altered using the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.setCurrentWidget` function.

Whenever the current widget in the layout changes or a widget is removed from the layout, the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.currentChanged` and :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.widgetRemoved` signals are emitted respectively.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`, :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.
