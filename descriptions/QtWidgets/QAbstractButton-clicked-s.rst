.. sip:signal-description::
    :status: todo
    :pysig: 172b3fa18e5b4fe980b90f7beb495fa0
    :realsig: (bool)
    :digest: b554e92c77b645f86d1df2740e328c60

This signal is emitted when the button is activated (i.e., pressed down then released while the mouse cursor is inside the button), when the shortcut key is typed, or when :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.click` or :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.animateClick` is called. Notably, this signal is *not* emitted if you call :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setDown`, :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.setChecked` or :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.toggle`.

If the button is checkable, *checked* is true if the button is checked, or false if the button is unchecked.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.pressed`, :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.released`, :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.toggled`.
