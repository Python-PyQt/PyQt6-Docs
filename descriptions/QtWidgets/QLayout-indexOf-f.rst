.. sip:method-description::
    :status: todo
    :pysig: 2a38832352a50ffc5e738fd2b818b613
    :realsig: (const QWidget*) const
    :digest: 1a4694a6630553ac530821e53fb2adb8

Searches for widget *widget* in this layout (not including child layouts).

Returns the index of *widget*, or -1 if *widget* is not found.

The default implementation iterates over all items using :sip:ref:`~PyQt6.QtWidgets.QLayout.itemAt`.
