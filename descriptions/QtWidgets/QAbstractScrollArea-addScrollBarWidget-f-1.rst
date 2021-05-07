.. sip:method-description::
    :status: todo
    :pysig: be29f3a4b42a5849eeae0ee5f244a656
    :realsig: (QWidget*,Qt::Alignment)
    :digest: 765ee8d6e5ce028ddcc5329341455af6

Adds *widget* as a scroll bar widget in the location specified by *alignment*.

Scroll bar widgets are shown next to the horizontal or vertical scroll bar, and can be placed on either side of it. If you want the scroll bar widgets to be always visible, set the scrollBarPolicy for the corresponding scroll bar to ``AlwaysOn``.

*alignment* must be one of Qt::Alignleft and :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignRight`, which maps to the horizontal scroll bar, or :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignTop` and :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignBottom`, which maps to the vertical scroll bar.

A scroll bar widget can be removed by either re-parenting the widget or deleting it. It's also possible to hide a widget with :sip:ref:`~PyQt6.QtWidgets.QWidget.hide`

The scroll bar widget will be resized to fit the scroll bar geometry for the current style. The following describes the case for scroll bar widgets on the horizontal scroll bar:

The height of the widget will be set to match the height of the scroll bar. To control the width of the widget, use :sip:ref:`~PyQt6.QtWidgets.QWidget.setMinimumWidth` and :sip:ref:`~PyQt6.QtWidgets.QWidget.setMaximumWidth`, or implement :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` and set a horizontal size policy. If you want a square widget, call :sip:ref:`~PyQt6.QtWidgets.QStyle.pixelMetric`\ (\ :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_ScrollBarExtent`) and set the width to this value.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.scrollBarWidgets`.
