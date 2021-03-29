.. sip:class-description::
    :status: todo
    :brief: Scrolling area with on-demand scroll bars
    :digest: af8ea670c8491ee8bbab7a3790252370

The :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` widget provides a scrolling area with on-demand scroll bars.

:sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` is a low-level abstraction of a scrolling area. The area provides a central widget called the viewport, in which the contents of the area is to be scrolled (i.e, the visible parts of the contents are rendered in the viewport).

Next to the viewport is a vertical scroll bar, and below is a horizontal scroll bar. When all of the area contents fits in the viewport, each scroll bar can be either visible or hidden depending on the scroll bar's :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy`. When a scroll bar is hidden, the viewport expands in order to cover all available space. When a scroll bar becomes visible again, the viewport shrinks in order to make room for the scroll bar.

It is possible to reserve a margin area around the viewport, see :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.setViewportMargins`. The feature is mostly used to place a :sip:ref:`~PyQt6.QtWidgets.QHeaderView` widget above or beside the scrolling area. Subclasses of :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` should implement margins.

When inheriting :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`, you need to do the following:

* Control the scroll bars by setting their range, value, page step, and tracking their movements.

* Draw the contents of the area in the viewport according to the values of the scroll bars.

* Handle events received by the viewport in :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewportEvent` - notably resize events.

* Use ``viewport->update()`` to update the contents of the viewport instead of :sip:ref:`~PyQt6.QtWidgets.QWidget.update` as all painting operations take place on the viewport.

With a scroll bar policy of :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded` (the default), :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` shows scroll bars when they provide a non-zero scrolling range, and hides them otherwise.

The scroll bars and viewport should be updated whenever the viewport receives a resize event or the size of the contents changes. The viewport also needs to be updated when the scroll bars values change. The initial values of the scroll bars are often set when the area receives new contents.

We give a simple example, in which we have implemented a scroll area that can scroll any `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_. We make the widget a child of the viewport; this way, we do not have to calculate which part of the widget to draw but can simply move the widget with :sip:ref:`~PyQt6.QtWidgets.QWidget.move`. When the area contents or the viewport size changes, we do the following:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-myscrollarea-myscrollarea.py
    :lines: 112-119

When the scroll bars change value, we need to update the widget position, i.e., find the part of the widget that is to be drawn in the viewport:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-myscrollarea-myscrollarea.py
    :lines: 94-98

In order to track scroll bar movements, reimplement the virtual function :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.scrollContentsBy`. In order to fine-tune scrolling behavior, connect to a scroll bar's :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.actionTriggered` signal and adjust the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderPosition` as you wish.

For convenience, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` makes all viewport events available in the virtual :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.viewportEvent` handler. `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_'s specialized handlers are remapped to viewport events in the cases where this makes sense. The remapped specialized handlers are: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.paintEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.wheelEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dragEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dragMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dragLeaveEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.dropEvent`, :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.contextMenuEvent`, and :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.resizeEvent`.

:sip:ref:`~PyQt6.QtWidgets.QScrollArea`, which inherits :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`, provides smooth scrolling for any `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ (i.e., the widget is scrolled pixel by pixel). You only need to subclass :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea` if you need more specialized behavior. This is, for instance, true if the entire contents of the area is not suitable for being drawn on a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or if you do not want smooth scrolling.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScrollArea`.
