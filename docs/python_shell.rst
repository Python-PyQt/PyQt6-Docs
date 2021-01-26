Using PyQt6 from the Python Shell
=================================

PyQt6 installs an input hook (using :c:func:`PyOS_InputHook`) that processes
events when an interactive interpreter is waiting for user input.  This means
that you can, for example, create widgets from the Python shell prompt,
interact with them, and still being able to enter other Python commands.

For example, if you enter the following in the Python shell::

    >>> from PyQt6.QtWidgets import QApplication, QWidget
    >>> a = QApplication([])
    >>> w = QWidget()
    >>> w.show()
    >>> w.hide()
    >>>

The widget would be displayed when ``w.show()`` was entered and hidden as soon
as ``w.hide()`` was entered.

The installation of an input hook can cause problems for certain applications
(particularly those that implement a similar feature using different means).
The :sip:ref:`~PyQt6.QtCore` module contains the
:sip:ref:`~PyQt6.QtCore.pyqtRemoveInputHook` and
:sip:ref:`~PyQt6.QtCore.pyqtRestoreInputHook` functions that remove and restore
the input hook respectively.
