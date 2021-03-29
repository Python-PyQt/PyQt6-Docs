.. sip:method-description::
    :status: todo
    :pysig: 4fcdfd9e643a4a7ca50a7e50ace31b1b
    :realsig: (int,QWidget*,int)
    :digest: 0cb801f718257aaa21312a8d97574bbc

Inserts the given *widget* at the given *index* permanently to this status bar, reparenting the widget if it isn't already a child of this :sip:ref:`~PyQt6.QtWidgets.QStatusBar` object. If *index* is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).

The *stretch* parameter is used to compute a suitable size for the given *widget* as the status bar grows and shrinks. The default stretch factor is 0, i.e giving the widget a minimum of space.

Permanently means that the widget may not be obscured by temporary messages. It is is located at the far right of the status bar.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addPermanentWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.removeWidget`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addWidget`.
