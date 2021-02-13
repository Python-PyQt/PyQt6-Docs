.. sip:class-description::
    :status: todo
    :brief: Layout where one can anchor widgets together in Graphics View
    :digest: a848bab3d8d8960ecee1b56c9890cd00

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout` class provides a layout where one can anchor widgets together in Graphics View.

The anchor layout allows developers to specify how widgets should be placed relative to each other, and to the layout itself. The specification is made by adding anchors to the layout by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchors` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addCornerAnchors`.

Existing anchors in the layout can be accessed with the :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.anchor` function. Items that are anchored are automatically added to the layout, and if items are removed, all their anchors will be automatically removed.

|image-simpleanchorlayout-example-png|

Anchors are always set up between edges of an item, where the "center" is also considered to be an edge. Consider the following example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-graphicsview-simpleanchorlayout-main.py
    :lines: 111-112

Here, the right edge of item ``a`` is anchored to the left edge of item ``b`` and the bottom edge of item ``a`` is anchored to the top edge of item ``b``, with the result that item ``b`` will be placed diagonally to the right and below item ``b``.

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addCornerAnchors` function provides a simpler way of anchoring the corners of two widgets than the two individual calls to :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchor` shown in the code above. Here, we see how a widget can be anchored to the top-left corner of the enclosing layout:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-graphicsview-simpleanchorlayout-main.py
    :lines: 107-107

In cases where anchors are used to match the widths or heights of widgets, it is convenient to use the :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout.addAnchors` function. As with the other functions for specifying anchors, it can also be used to anchor a widget to a layout.

.. _qgraphicsanchorlayout-size-hints-and-size-policies-in-an-anchor-layout:

Size Hints and Size Policies in an Anchor Layout
------------------------------------------------

:sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout` respects each item's size hints and size policies. Note that there are some properties of :sip:ref:`~PyQt6.QtWidgets.QSizePolicy` that are not respected.

.. _qgraphicsanchorlayout-spacing-within-an-anchor-layout:

Spacing within an Anchor Layout
-------------------------------

The layout may distribute some space between the items. If the spacing has not been explicitly specified, the actual amount of space will usually be 0.

However, if the first edge is the *opposite* of the second edge (e.g., the right edge of the first widget is anchored to the left edge of the second widget), the size of the anchor will be queried from the style through a pixel metric: :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutHorizontalSpacing` for horizontal anchors and :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutVerticalSpacing` for vertical anchors.

If the spacing is negative, the items will overlap to some extent.

.. _qgraphicsanchorlayout-known-issues:

Known Issues
------------

There are some features that :sip:ref:`~PyQt6.QtWidgets.QGraphicsAnchorLayout` currently does not support. This might change in the future, so avoid using these features if you want to avoid any future regressions in behaviour:

* Stretch factors are not respected.

* :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.PolicyFlag.ExpandFlag` is not respected.

* Height for width is not respected.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsGridLayout`, `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_.

.. |image-simpleanchorlayout-example-png| image:: ../../../images/simpleanchorlayout-example.png
