.. sip:class-description::
    :status: todo
    :brief: Rectangle or line that can indicate a selection or a boundary
    :digest: 7cc78ad1b828b4bef78afc5baa807082

The :sip:ref:`~PyQt6.QtWidgets.QRubberBand` class provides a rectangle or line that can indicate a selection or a boundary.

A rubber band is often used to show a new bounding area (as in a :sip:ref:`~PyQt6.QtWidgets.QSplitter` or a :sip:ref:`~PyQt6.QtWidgets.QDockWidget` that is undocking). Historically this has been implemented using a :sip:ref:`~PyQt6.QtGui.QPainter` and XOR, but this approach doesn't always work properly since rendering can happen in the window below the rubber band, but before the rubber band has been "erased".

You can create a :sip:ref:`~PyQt6.QtWidgets.QRubberBand` whenever you need to render a rubber band around a given area (or to represent a single line), then call :sip:ref:`~PyQt6.QtWidgets.QRubberBand.setGeometry`, :sip:ref:`~PyQt6.QtWidgets.QRubberBand.move` or :sip:ref:`~PyQt6.QtWidgets.QRubberBand.resize` to position and size it. A common pattern is to do this in conjunction with mouse events. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qrubberband.py
    :lines: 54-73

If you pass a parent to :sip:ref:`~PyQt6.QtWidgets.QRubberBand`'s constructor, the rubber band will display only inside its parent, but stays on top of other child widgets. If no parent is passed, :sip:ref:`~PyQt6.QtWidgets.QRubberBand` will act as a top-level widget.

Call show() to make the rubber band visible; also when the rubber band is not a top-level. Hiding or destroying the widget will make the rubber band disappear. The rubber band can be a :sip:ref:`~PyQt6.QtWidgets.QRubberBand.Shape.Rectangle` or a :sip:ref:`~PyQt6.QtWidgets.QRubberBand.Shape.Line` (vertical or horizontal), depending on the :sip:ref:`~PyQt6.QtWidgets.QRubberBand.shape` it was given when constructed.
