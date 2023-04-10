.. sip:class-description::
    :status: todo
    :brief: Widget that presents buttons in a layout that is appropriate to the current widget style
    :digest: 23a500b0c1051a23f645d1b5496a4a67

The :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox` class is a widget that presents buttons in a layout that is appropriate to the current widget style.

Dialogs and message boxes typically present buttons in a layout that conforms to the interface guidelines for that platform. Invariably, different platforms have different layouts for their dialogs. :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox` allows a developer to add buttons to it and will automatically use the appropriate layout for the user's desktop environment.

Most buttons for a dialog follow certain roles. Such roles include:

* Accepting or rejecting the dialog.

* Asking for help.

* Performing actions on the dialog itself (such as resetting fields or applying changes).

There can also be alternate ways of dismissing the dialog which may cause destructive results.

Most dialogs have buttons that can almost be considered standard (e.g. OK and Cancel buttons). It is sometimes convenient to create these buttons in a standard way.

There are a couple ways of using :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox`. One ways is to create the buttons (or button texts) yourself and add them to the button box, specifying their role.

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-extension-finddialog.py
    :lines: 70-77

Alternatively, :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox` provides several standard buttons (e.g. OK, Cancel, Save) that you can use. They exist as flags so you can OR them together in the constructor.

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-tabdialog-tabdialog.py
    :lines: 70-75

You can mix and match normal buttons and standard buttons.

Currently the buttons are laid out in the following way if the button box is horizontal:

+-------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-buttonbox-gnomelayout-horizontal-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.GnomeLayout` Horizontal | Button box laid out in horizontal :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.GnomeLayout` |
+-------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-buttonbox-kdelayout-horizontal-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.KdeLayout` Horizontal     | Button box laid out in horizontal :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.KdeLayout`   |
+-------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-buttonbox-maclayout-horizontal-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout` Horizontal     | Button box laid out in horizontal :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout`   |
+-------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| |image-buttonbox-winlayout-horizontal-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.WinLayout` Horizontal     | Button box laid out in horizontal :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.WinLayout`   |
+-------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

The buttons are laid out the following way if the button box is vertical:

+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.GnomeLayout`                                                     | :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.KdeLayout`                                                   | :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout`                                                   | :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.WinLayout`                                                   |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| |image-buttonbox-gnomelayout-vertical-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.GnomeLayout` Vertical | |image-buttonbox-kdelayout-vertical-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.KdeLayout` Vertical | |image-buttonbox-maclayout-vertical-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout` Vertical | |image-buttonbox-winlayout-vertical-png| :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.WinLayout` Vertical |
+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

Additionally, button boxes that contain only buttons with :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonRole.ActionRole` or :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonRole.HelpRole` can be considered modeless and have an alternate look on macOS:

+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| modeless horizontal :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout` | |image-buttonbox-mac-modeless-horizontal-png| Screenshot of modeless horizontal :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout` |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| modeless vertical :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout`   | |image-buttonbox-mac-modeless-vertical-png| Screenshot of modeless vertical :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonLayout.MacLayout`     |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

When a button is clicked in the button box, the :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.clicked` signal is emitted for the actual button is that is pressed. For convenience, if the button has an :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonRole.AcceptRole`, :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonRole.RejectRole`, or :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.ButtonRole.HelpRole`, the :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.accepted`, :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.rejected`, or :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.helpRequested` signals are emitted respectively.

If you want a specific button to be default you need to call :sip:ref:`~PyQt6.QtWidgets.QPushButton.setDefault` on it yourself. However, if there is no default button set and to preserve which button is the default button across platforms when using the :sip:ref:`~PyQt6.QtWidgets.QPushButton.autoDefault` property, the first push button with the accept role is made the default button when the :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox` is shown,

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMessageBox`, :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QDialog`.

.. |image-buttonbox-gnomelayout-horizontal-png| image:: ../../../images/buttonbox-gnomelayout-horizontal.png
.. |image-buttonbox-kdelayout-horizontal-png| image:: ../../../images/buttonbox-kdelayout-horizontal.png
.. |image-buttonbox-maclayout-horizontal-png| image:: ../../../images/buttonbox-maclayout-horizontal.png
.. |image-buttonbox-winlayout-horizontal-png| image:: ../../../images/buttonbox-winlayout-horizontal.png
.. |image-buttonbox-gnomelayout-vertical-png| image:: ../../../images/buttonbox-gnomelayout-vertical.png
.. |image-buttonbox-kdelayout-vertical-png| image:: ../../../images/buttonbox-kdelayout-vertical.png
.. |image-buttonbox-maclayout-vertical-png| image:: ../../../images/buttonbox-maclayout-vertical.png
.. |image-buttonbox-winlayout-vertical-png| image:: ../../../images/buttonbox-winlayout-vertical.png
.. |image-buttonbox-mac-modeless-horizontal-png| image:: ../../../images/buttonbox-mac-modeless-horizontal.png
.. |image-buttonbox-mac-modeless-vertical-png| image:: ../../../images/buttonbox-mac-modeless-vertical.png
