.. sip:method-description::
    :status: todo
    :pysig: 2fbee137ce64f2d924d825da23b13c6c
    :realsig: (QLayoutItem*)
    :digest: cd068b9264bbbfa9cc8618c31eac9180

Removes the layout item *item* from the layout. It is the caller's responsibility to delete the item.

Notice that *item* can be a layout (since :sip:ref:`~PyQt6.QtWidgets.QLayout` inherits :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QLayout.removeWidget`, :sip:ref:`~PyQt6.QtWidgets.QLayout.addItem`.
