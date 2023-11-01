.. sip:class-description::
    :status: todo
    :brief: Horizontal bar suitable for presenting status information
    :digest: b0581cab7f346c867764b51605001cb2

The :sip:ref:`~PyQt6.QtWidgets.QStatusBar` class provides a horizontal bar suitable for presenting status information.

Each status indicator falls into one of three categories:

* *Temporary* - briefly occupies most of the status bar. Used to explain tool tip texts or menu entries, for example.

* *Normal* - occupies part of the status bar and may be hidden by temporary messages. Used to display the page and line number in a word processor, for example.

* *Permanent* - is never hidden. Used for important mode indications, for example, some applications put a Caps Lock indicator in the status bar.

:sip:ref:`~PyQt6.QtWidgets.QStatusBar` lets you display all three types of indicators.

Typically, a request for the status bar functionality occurs in relation to a :sip:ref:`~PyQt6.QtWidgets.QMainWindow` object. :sip:ref:`~PyQt6.QtWidgets.QMainWindow` provides a main application window, with a menu bar, tool bars, dock widgets *and* a status bar around a large central widget. The status bar can be retrieved using the :sip:ref:`~PyQt6.QtWidgets.QMainWindow.statusBar` function, and replaced using the :sip:ref:`~PyQt6.QtWidgets.QMainWindow.setStatusBar` function.

Use the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.showMessage` slot to display a *temporary* message:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qstatusbar.py

To remove a temporary message, use the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.clearMessage` slot, or set a time limit when calling :sip:ref:`~PyQt6.QtWidgets.QStatusBar.showMessage`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qstatusbar.py

Use the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.currentMessage` function to retrieve the temporary message currently shown. The :sip:ref:`~PyQt6.QtWidgets.QStatusBar` class also provide the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.messageChanged` signal which is emitted whenever the temporary status message changes.

.. _qstatusbar-permanent-message:

*Normal* and *Permanent* messages are displayed by creating a small widget (\ :sip:ref:`~PyQt6.QtWidgets.QLabel`, :sip:ref:`~PyQt6.QtWidgets.QProgressBar` or even :sip:ref:`~PyQt6.QtWidgets.QToolButton`) and then adding it to the status bar using the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addWidget` or the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.addPermanentWidget` function. Use the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.removeWidget` function to remove such messages from the status bar.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qstatusbar.py
    :lines: 54-54

By default :sip:ref:`~PyQt6.QtWidgets.QStatusBar` provides a :sip:ref:`~PyQt6.QtWidgets.QSizeGrip` in the lower-right corner. You can disable it using the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.setSizeGripEnabled` function. Use the :sip:ref:`~PyQt6.QtWidgets.QStatusBar.isSizeGripEnabled` function to determine the current status of the size grip.

.. image:: ../../../images/fusion-statusbar-sizegrip.png

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow`, :sip:ref:`~PyQt6.QtGui.QStatusTipEvent`.
