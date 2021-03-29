.. sip:method-description::
    :status: todo
    :pysig: d96ea631fbca390eace8bf562ba29c28
    :realsig: (QWidget*,int)
    :digest: 6bfbc4a97aae6470df70dbe178e59a7b

Adds the given *widget* permanently to this status bar, reparenting the widget if it isn't already a child of this :sip:ref:`~PyQt6.QtWidgets.QStatusBar` object. The *stretch* parameter is used to compute a suitable size for the given *widget* as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

Permanently means that the widget may not be obscured by temporary messages. It is is located at the far right of the status bar.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.insertPermanentWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.removeWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addWidget`.
