.. sip:method-description::
    :status: todo
    :pysig: a6acdc3199284514d754a013bd402898
    :realsig: (int,QLayoutItem*)
    :digest: 05666b149303412af199355de3a83ad5

Inserts *item* into this box layout at position *index*. Index must be either negative or within the range 0 to :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.count`, inclusive. If *index* is negative or :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.count`, the item is added at the end.

The ownership of *item* is passed to this layout.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addItem`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertLayout`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertStretch`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertSpacing`.
