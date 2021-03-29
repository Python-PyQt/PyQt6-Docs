.. sip:class-description::
    :status: todo
    :brief: Tool tips (balloon help) for any widget
    :digest: e0bb76a197f181e2701c61d7b78456b4

The :sip:ref:`~PyQt6.QtWidgets.QToolTip` class provides tool tips (balloon help) for any widget.

The tip is a short piece of text reminding the user of the widget's function. It is drawn immediately below the given position in a distinctive black-on-yellow color combination. The tip can be any :sip:ref:`~PyQt6.QtWidgets.QTextEdit` formatted string.

Rich text displayed in a tool tip is implicitly word-wrapped unless specified differently with ``<p style='white-space:pre'>``.

The simplest and most common way to set a widget's tool tip is by calling its :sip:ref:`~PyQt6.QtWidgets.QWidget.setToolTip` function.

It is also possible to show different tool tips for different regions of a widget, by using a :sip:ref:`~PyQt6.QtGui.QHelpEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolTip`. Intercept the help event in your widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.event` function and call :sip:ref:`~PyQt6.QtWidgets.QToolTip.showText` with the text you want to display. The `Tooltips <https://doc.qt.io/qt-6/qtwidgets-widgets-tooltips-example.html>`_ example illustrates this technique.

If you are calling :sip:ref:`~PyQt6.QtWidgets.QToolTip.hideText`, or :sip:ref:`~PyQt6.QtWidgets.QToolTip.showText` with an empty string, as a result of a :sip:ref:`~PyQt6.QtCore.QEvent.Type.ToolTip`-event you should also call :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on the event, to signal that you don't want to start any tooltip specific modes.

Note that, if you want to show tooltips in an item view, the model/view architecture provides functionality to set an item's tool tip; e.g., the :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem.setToolTip` function. However, if you want to provide custom tool tips in an item view, you must intercept the help event in the :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.viewportEvent` function and handle it yourself.

The default tool tip color and font can be customized with :sip:ref:`~PyQt6.QtWidgets.QToolTip.setPalette` and :sip:ref:`~PyQt6.QtWidgets.QToolTip.setFont`. When a tooltip is currently on display, :sip:ref:`~PyQt6.QtWidgets.QToolTip.isVisible` returns ``true`` and :sip:ref:`~PyQt6.QtWidgets.QToolTip.text` the currently visible text.

**Note:** Tool tips use the inactive color group of :sip:ref:`~PyQt6.QtGui.QPalette`, because tool tips are not active windows.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.toolTip`, :sip:ref:`~PyQt6.QtGui.QAction.toolTip`, `Tool Tips Example <https://doc.qt.io/qt-6/qtwidgets-widgets-tooltips-example.html>`_.
