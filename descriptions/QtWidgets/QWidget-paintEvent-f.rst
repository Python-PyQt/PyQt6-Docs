.. sip:method-description::
    :status: todo
    :pysig: f2ec3c5d78a75ad8f7dac6730db95648
    :realsig: (QPaintEvent*)
    :digest: 7961fd39a03aa86c69d4fc8626eb41f3

This event handler can be reimplemented in a subclass to receive paint events passed in *event*.

A paint event is a request to repaint all or part of a widget. It can happen for one of the following reasons:

* :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` or :sip:ref:`~PyQt6.QtWidgets.QWidget.update` was invoked,

* the widget was obscured and has now been uncovered, or

* many other reasons.

Many widgets can simply repaint their entire surface when asked to, but some slow widgets need to optimize by painting only the requested region: :sip:ref:`~PyQt6.QtGui.QPaintEvent.region`. This speed optimization does not change the result, as painting is clipped to that region during event processing. :sip:ref:`~PyQt6.QtWidgets.QListView` and :sip:ref:`~PyQt6.QtWidgets.QTableView` do this, for example.

Qt also tries to speed up painting by merging multiple paint events into one. When :sip:ref:`~PyQt6.QtWidgets.QWidget.update` is called several times or the window system sends several paint events, Qt merges these events into one event with a larger region (see :sip:ref:`~PyQt6.QtGui.QRegion.united`). The :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` function does not permit this optimization, so we suggest using :sip:ref:`~PyQt6.QtWidgets.QWidget.update` whenever possible.

When the paint event occurs, the update region has normally been erased, so you are painting on the widget's background.

The background can be set using :sip:ref:`~PyQt6.QtWidgets.QWidget.setBackgroundRole` and :sip:ref:`~PyQt6.QtWidgets.QWidget.setPalette`.

Since Qt 4.0, `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ automatically double-buffers its painting, so there is no need to write double-buffering code in  to avoid flicker.

**Note:** Generally, you should refrain from calling :sip:ref:`~PyQt6.QtWidgets.QWidget.update` or :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` **inside** a . For example, calling :sip:ref:`~PyQt6.QtWidgets.QWidget.update` or :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint` on children inside a  results in undefined behavior; the child may or may not get a paint event.

**Warning:** If you are using a custom paint engine without Qt's backingstore, :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_PaintOnScreen` must be set. Otherwise, :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEngine` will never be called; the backingstore will be used instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QWidget.repaint`, :sip:ref:`~PyQt6.QtWidgets.QWidget.update`, :sip:ref:`~PyQt6.QtGui.QPainter`, :sip:ref:`~PyQt6.QtGui.QPixmap`, :sip:ref:`~PyQt6.QtGui.QPaintEvent`, `Analog Clock Example <https://doc.qt.io/qt-6/qtwidgets-widgets-analogclock-example.html>`_.
