.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6b950bf628c8bf2f02c1a1b802d6bde4

Updates the widget unless updates are disabled or the widget is hidden.

This function does not cause an immediate repaint; instead it schedules a paint event for processing when Qt returns to the main event loop. This permits Qt to optimize for more speed and less flicker than a call to :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` does.

Calling update() several times normally results in just one :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent` call.

Qt normally erases the widget's area before the :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent` call. If the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_OpaquePaintEvent` widget attribute is set, the widget is responsible for painting all its pixels with an opaque color.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint`, :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setUpdatesEnabled`, `Analog Clock <https://doc.qt.io/qt-6/qtwidgets-widgets-analogclock-example.html>`_.
