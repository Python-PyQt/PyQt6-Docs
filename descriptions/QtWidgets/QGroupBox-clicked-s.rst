.. sip:signal-description::
    :status: todo
    :pysig: 172b3fa18e5b4fe980b90f7beb495fa0
    :realsig: (bool)
    :digest: eb5366b476a12b082a36cd07076c2436

This signal is emitted when the check box is activated (i.e., pressed down then released while the mouse cursor is inside the button), or when the shortcut key is typed. Notably, this signal is *not* emitted if you call :sip:ref:`~PyQt6.QtWidgets.QGroupBox.setChecked`.

If the check box is checked, *checked* is true; it is false if the check box is unchecked.

.. seealso:: checkable, :sip:ref:`~PyQt6.QtWidgets.QGroupBox.toggled`, checked.
