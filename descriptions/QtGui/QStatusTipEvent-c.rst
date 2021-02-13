.. sip:class-description::
    :status: todo
    :brief: Event that is used to show messages in a status bar
    :digest: 19592e30ef526fc378708082dd13c232

The :sip:ref:`~PyQt6.QtGui.QStatusTipEvent` class provides an event that is used to show messages in a status bar.

Status tips can be set on a widget using the QWidget::setStatusTip() function. They are shown in the status bar when the mouse cursor enters the widget. For example:

+-------------------------------------------------------------------------------------------+-------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qstatustipevent-main.py | .. image:: ../../../images/qstatustipevent-widget.png |
|     :lines: 64-71                                                                         |                                                       |
|                                                                                           |                                                       |
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qstatustipevent-main.py |                                                       |
|     :lines: 85-85                                                                         |                                                       |
+-------------------------------------------------------------------------------------------+-------------------------------------------------------+

Status tips can also be set on actions using the :sip:ref:`~PyQt6.QtGui.QAction.setStatusTip` function:

+-------------------------------------------------------------------------------------------+-------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qstatustipevent-main.py | .. image:: ../../../images/qstatustipevent-action.png |
|     :lines: 64-66                                                                         |                                                       |
|                                                                                           |                                                       |
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qstatustipevent-main.py |                                                       |
|     :lines: 75-79                                                                         |                                                       |
|                                                                                           |                                                       |
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qstatustipevent-main.py |                                                       |
|     :lines: 85-85                                                                         |                                                       |
+-------------------------------------------------------------------------------------------+-------------------------------------------------------+

Finally, status tips are supported for the item view classes through the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.StatusTipRole` enum value.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QHelpEvent`, :sip:ref:`~PyQt6.QtGui.QWhatsThisClickedEvent`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar`.
