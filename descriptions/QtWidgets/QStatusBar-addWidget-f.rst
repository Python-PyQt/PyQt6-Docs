.. sip:method-description::
    :status: todo
    :pysig: d96ea631fbca390eace8bf562ba29c28
    :realsig: (QWidget*,int)
    :digest: 6ff38244de2323ec89407d150481c917

Adds the given *widget* to this status bar, reparenting the widget if it isn't already a child of this :sip:ref:`~PyQt6.QtWidgets.QStatusBar` object. The *stretch* parameter is used to compute a suitable size for the given *widget* as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

The widget is located to the far left of the first permanent widget (see :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addPermanentWidget`) and may be obscured by temporary messages.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.removeWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addPermanentWidget`.
