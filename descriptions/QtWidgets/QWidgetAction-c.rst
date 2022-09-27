.. sip:class-description::
    :status: todo
    :brief: Extends QAction by an interface for inserting custom widgets into action based containers, such as toolbars
    :digest: 4f7d25922f46d917ee8412d8cd373420

The :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` class extends :sip:ref:`~PyQt6.QtGui.QAction` by an interface for inserting custom widgets into action based containers, such as toolbars.

Most actions in an application are represented as items in menus or buttons in toolbars. However sometimes more complex widgets are necessary. For example a zoom action in a word processor may be realized using a :sip:ref:`~PyQt6.QtWidgets.QComboBox` in a :sip:ref:`~PyQt6.QtWidgets.QToolBar`, presenting a range of different zoom levels. :sip:ref:`~PyQt6.QtWidgets.QToolBar` provides :sip:ref:`~PyQt6.QtWidgets.QToolBar.insertWidget` as convenience function for inserting a single widget. However if you want to implement an action that uses custom widgets for visualization in multiple containers then you have to subclass :sip:ref:`~PyQt6.QtWidgets.QWidgetAction`.

If a :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` is added for example to a :sip:ref:`~PyQt6.QtWidgets.QToolBar` then :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.createWidget` is called. Reimplementations of that function should create a new custom widget with the specified parent.

If the action is removed from a container widget then :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.deleteWidget` is called with the previously created custom widget as argument. The default implementation hides the widget and deletes it using :sip:ref:`~PyQt6.QtCore.QObject.deleteLater`.

If you have only one single custom widget then you can set it as default widget using :sip:ref:`~PyQt6.QtWidgets.QWidgetAction.setDefaultWidget`. That widget will then be used if the action is added to a :sip:ref:`~PyQt6.QtWidgets.QToolBar`, or in general to an action container that supports :sip:ref:`~PyQt6.QtWidgets.QWidgetAction`. If a :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` with only a default widget is added to two toolbars at the same time then the default widget is shown only in the first toolbar the action was added to. :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` takes over ownership of the default widget.

Note that it is up to the widget to activate the action, for example by reimplementing mouse event handlers and calling :sip:ref:`~PyQt6.QtGui.QAction.trigger`.

**macOS**: If you add a widget to a menu in the application's menu bar on macOS, the widget will be added and it will function but with some limitations:

#. The widget is reparented away from the :sip:ref:`~PyQt6.QtWidgets.QMenu` to the native menu view. If you show the menu in some other place (e.g. as a popup menu), the widget will not be there.

#. Focus/Keyboard handling of the widget is not possible.

#. Due to Apple's design, mouse tracking on the widget currently does not work.

#. Connecting the triggered() signal to a slot that opens a modal dialog will cause a crash in macOS 10.4 (known bug acknowledged by Apple), a workaround is to use a QueuedConnection instead of a DirectConnection.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction`, :sip:ref:`~PyQt6.QtGui.QActionGroup`, :sip:ref:`~PyQt6.QtWidgets.QWidget`.
