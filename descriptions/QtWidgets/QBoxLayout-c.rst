.. sip:class-description::
    :status: todo
    :brief: Lines up child widgets horizontally or vertically
    :digest: 30448a0175c4ecb1d9024b7d2a00bb3b

The :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` class lines up child widgets horizontally or vertically.

:sip:ref:`~PyQt6.QtWidgets.QBoxLayout` takes the space it gets (from its parent layout or from the parentWidget()), divides it up into a row of boxes, and makes each managed widget fill one box.

.. image:: ../../../images/qhboxlayout-with-5-children.png

If the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`'s orientation is :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Horizontal` the boxes are placed in a row, with suitable sizes. Each widget (or other box) will get at least its minimum size and at most its maximum size. Any excess space is shared according to the stretch factors (more about that below).

.. image:: ../../../images/qvboxlayout-with-5-children.png

If the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`'s orientation is :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Vertical`, the boxes are placed in a column, again with suitable sizes.

The easiest way to create a :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` is to use one of the convenience classes, e.g. :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout` (for :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Horizontal` boxes) or :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout` (for :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Vertical` boxes). You can also use the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` constructor directly, specifying its direction as :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction.LeftToRight`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction.RightToLeft`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction.TopToBottom`, or :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction.BottomToTop`.

If the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` is not the top-level layout (i.e. it is not managing all of the widget's area and children), you must add it to its parent layout before you can do anything with it. The normal way to add a layout is by calling parentLayout->\ :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addLayout`.

Once you have done this, you can add boxes to the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` using one of four functions:

* :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addWidget` to add a widget to the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` and set the widget's stretch factor. (The stretch factor is along the row of boxes.)

* :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addSpacing` to create an empty box; this is one of the functions you use to create nice and spacious dialogs. See below for ways to set margins.

* :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addStretch` to create an empty, stretchable box.

* :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addLayout` to add a box containing another :sip:ref:`~PyQt6.QtWidgets.QLayout` to the row and set that layout's stretch factor.

Use :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertSpacing`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertStretch` or :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertLayout` to insert a box at a specified position in the layout.

:sip:ref:`~PyQt6.QtWidgets.QBoxLayout` also includes two margin widths:

* setContentsMargins() sets the width of the outer border on each side of the widget. This is the width of the reserved space along each of the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`'s four sides.

* :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.setSpacing` sets the width between neighboring boxes. (You can use :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addSpacing` to get more space at a particular spot.)

The margin default is provided by the style. The default margin most Qt styles specify is 9 for child widgets and 11 for windows. The spacing defaults to the same as the margin width for a top-level layout, or to the same as the parent layout.

To remove a widget from a layout, call removeWidget(). Calling :sip:ref:`~PyQt6.QtWidgets.QWidget.hide` on a widget also effectively removes the widget from the layout until :sip:ref:`~PyQt6.QtWidgets.QWidget.show` is called.

You will almost always want to use :sip:ref:`~PyQt6.QtWidgets.QVBoxLayout` and :sip:ref:`~PyQt6.QtWidgets.QHBoxLayout` rather than :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` because of their convenient constructors.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGridLayout`, :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`, `Layout Management <https://doc.qt.io/qt-6/layout.html>`_.
