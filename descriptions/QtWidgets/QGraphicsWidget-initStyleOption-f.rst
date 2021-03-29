.. sip:method-description::
    :status: todo
    :pysig: 207044357f3c256a510bb81ee7f16bce
    :realsig: (QStyleOption*) const
    :digest: d540a7a98f7b7cefaaa45ff2195c21ca

Populates a style option object for this widget based on its current state, and stores the output in *option*. The default implementation populates *option* with the following properties.

+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Style Option Property                                            | Value                                                                                                      |
+==================================================================+============================================================================================================+
| state & :sip:ref:`~PyQt6.QtWidgets.QStyle.State.State_Enabled`   | Corresponds to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isEnabled`.                                        |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| state & :sip:ref:`~PyQt6.QtWidgets.QStyle.State.State_HasFocus`  | Corresponds to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasFocus`.                                         |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| state & :sip:ref:`~PyQt6.QtWidgets.QStyle.State.State_MouseOver` | Corresponds to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.isUnderMouse`.                                     |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| direction                                                        | Corresponds to :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.layoutDirection`.                                |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| rect                                                             | Corresponds to :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.rect`.toRect().                                  |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| palette                                                          | Corresponds to :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.palette`.                                        |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| fontMetrics                                                      | Corresponds to :sip:ref:`~PyQt6.QtGui.QFontMetrics`\ (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.font`). |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Subclasses of `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ should call the base implementation, and then test the type of *option* using qstyleoption_cast<>() or test :sip:ref:`~PyQt6.QtWidgets.QStyleOption.StyleOptionType.Type` before storing widget-specific options.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicswidget.py
    :lines: 54-62

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption.initFrom`.
