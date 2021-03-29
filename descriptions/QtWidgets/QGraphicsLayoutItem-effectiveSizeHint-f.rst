.. sip:method-description::
    :status: todo
    :pysig: 87350351ac7539b57ac9074a1a8bc6f9
    :realsig: (Qt::SizeHint,const QSizeF&) const
    :digest: a1b80ad5c1b69831ea17728e3cc8d5f4

Returns the effective size hint for this :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem`.

*which* is the size hint in question. *constraint* is an optional argument that defines a special constrain when calculating the effective size hint. By default, *constraint* is :sip:ref:`~PyQt6.QtCore.QSizeF`\ (-1, -1), which means there is no constraint to the size hint.

If you want to specify the widget's size hint for a given width or height, you can provide the fixed dimension in *constraint*. This is useful for widgets that can grow only either vertically or horizontally, and need to set either their width or their height to a special value.

For example, a text paragraph item fit into a column width of 200 may grow vertically. You can pass :sip:ref:`~PyQt6.QtCore.QSizeF`\ (200, -1) as a constraint to get a suitable minimum, preferred and maximum height).

You can adjust the effective size hint by reimplementing :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` in a :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` subclass, or by calling one of the following functions: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMinimumSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setPreferredSize`, or :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.setMaximumSize` (or a combination of both).

This function caches each of the size hints and guarantees that :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` will be called only once for each value of *which* - unless *constraint* is not specified and :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.updateGeometry` has been called.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint`.
