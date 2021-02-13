.. sip:method-description::
    :status: todo
    :pysig: 48dc874a86aa726d066a6e260bbe7124
    :realsig: () const
    :digest: f5c58723446be22ba4089aa10af9ba4c

Returns a pointer to the item's top level widget (i.e., the item's ancestor whose parent is ``nullptr``, or whose parent is not a widget), or ``nullptr`` if this item does not have a top level widget. If the item is its own top level widget, this function returns a pointer to the item itself.
