.. sip:method-description::
    :status: todo
    :pysig: de7db18542fd73eeb5a53a26f5ff2640
    :realsig: (QWidget*,Qt::Corner)
    :digest: 9ac0aaab88f84c168891c38e17d90178

This sets the given *widget* to be shown directly on the left of the first menu item, or on the right of the last menu item, depending on *corner*.

The menu bar takes ownership of *widget*, reparenting it into the menu bar. However, if the *corner* already contains a widget, this previous widget will no longer be managed and will still be a visible child of the menu bar.

**Note:** Using a corner other than :sip:ref:`~PyQt6.QtCore.Qt.Corner.TopRightCorner` or :sip:ref:`~PyQt6.QtCore.Qt.Corner.TopLeftCorner` will result in a warning.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenuBar.cornerWidget`.
