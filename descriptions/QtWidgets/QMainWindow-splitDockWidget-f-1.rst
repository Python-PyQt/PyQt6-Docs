.. sip:method-description::
    :status: todo
    :pysig: bbc9b24d7bdf3fe5749e32ae3878be1e
    :realsig: (QDockWidget*,QDockWidget*,Qt::Orientation)
    :digest: 7a684377412f8addcffea93c03ab8704

Splits the space covered by the *first* dock widget into two parts, moves the *first* dock widget into the first part, and moves the *second* dock widget into the second part.

The *orientation* specifies how the space is divided: A :sip:ref:`~PyQt6.QtCore.Qt.Orientation.Horizontal` split places the second dock widget to the right of the first; a :sip:ref:`~PyQt6.QtCore.Qt.Orientation.Vertical` split places the second dock widget below the first.

*Note*: if *first* is currently in a tabbed docked area, *second* will be added as a new tab, not as a neighbor of *first*. This is because a single tab can contain only one dock widget.

*Note*: The :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection` influences the order of the dock widgets in the two parts of the divided area. When right-to-left layout direction is enabled, the placing of the dock widgets will be reversed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow.tabifyDockWidget`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.addDockWidget`, :sip:ref:`~PyQt6.QtWidgets.QMainWindow.removeDockWidget`.
