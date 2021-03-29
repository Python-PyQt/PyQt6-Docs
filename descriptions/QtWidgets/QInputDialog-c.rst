.. sip:class-description::
    :status: todo
    :brief: Simple convenience dialog to get a single value from the user
    :digest: bd05861527429701e678a3d926e1efda

The :sip:ref:`~PyQt6.QtWidgets.QInputDialog` class provides a simple convenience dialog to get a single value from the user.

The input value can be a string, a number or an item from a list. A label must be set to tell the user what they should enter.

Five static convenience functions are provided: :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getText`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getMultiLineText`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getInt`, :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getDouble`, and :sip:ref:`~PyQt6.QtWidgets.QInputDialog.getItem`. All the functions can be used in a similar way, for example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-standarddialogs-dialog.py
    :lines: 358-363

The ``ok`` variable is set to true if the user clicks OK; otherwise, it is set to false.

.. image:: ../../../images/inputdialogs.png

The `Standard Dialogs <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtWidgets.QInputDialog` as well as other built-in Qt dialogs.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox`, `Standard Dialogs Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-standarddialogs-example.html>`_.
