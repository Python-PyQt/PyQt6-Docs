.. sip:method-description::
    :status: todo
    :pysig: 48dc874a86aa726d066a6e260bbe7124
    :realsig: () const
    :digest: 4c963739a0659c8b168022a6a8b7249d

Returns the item's window, or ``nullptr`` if this item does not have a window. If the item is a window, it will return itself. Otherwise it will return the closest ancestor that is a window.

.. seealso:: QGraphicsWidget::isWindow().
