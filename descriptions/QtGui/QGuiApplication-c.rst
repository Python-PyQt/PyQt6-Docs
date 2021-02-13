.. sip:class-description::
    :status: todo
    :brief: Manages the GUI application's control flow and main settings
    :digest: 52235c4d6efb1a3c9c5aaa97b4c74844

The :sip:ref:`~PyQt6.QtGui.QGuiApplication` class manages the GUI application's control flow and main settings.

:sip:ref:`~PyQt6.QtGui.QGuiApplication` contains the main event loop, where all events from the window system and other sources are processed and dispatched. It also handles the application's initialization and finalization, and provides session management. In addition, :sip:ref:`~PyQt6.QtGui.QGuiApplication` handles most of the system-wide and application-wide settings.

For any GUI application using Qt, there is precisely **one** :sip:ref:`~PyQt6.QtGui.QGuiApplication` object no matter whether the application has 0, 1, 2 or more windows at any given time. For non-GUI Qt applications, use :sip:ref:`~PyQt6.QtCore.QCoreApplication` instead, as it does not depend on the Qt GUI module. For QWidget based Qt applications, use QApplication instead, as it provides some functionality needed for creating QWidget instances.

The :sip:ref:`~PyQt6.QtGui.QGuiApplication` object is accessible through the instance() function, which returns a pointer equivalent to the global qApp pointer.

:sip:ref:`~PyQt6.QtGui.QGuiApplication`'s main areas of responsibility are:

* It initializes the application with the user's desktop settings, such as :sip:ref:`~PyQt6.QtGui.QGuiApplication.palette`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.font` and :sip:ref:`~PyQt6.QtGui.QGuiApplication.styleHints`. It keeps track of these properties in case the user changes the desktop globally, for example, through some kind of control panel.

* It performs event handling, meaning that it receives events from the underlying window system and dispatches them to the relevant widgets. You can send your own events to windows by using sendEvent() and postEvent().

* It parses common command line arguments and sets its internal state accordingly. See the :sip:ref:`~PyQt6.QtGui.QGuiApplication.__init__` below for more details.

* It provides localization of strings that are visible to the user via translate().

* It provides some magical objects like the :sip:ref:`~PyQt6.QtGui.QGuiApplication.clipboard`.

* It knows about the application's windows. You can ask which window is at a certain position using :sip:ref:`~PyQt6.QtGui.QGuiApplication.topLevelAt`, get a list of :sip:ref:`~PyQt6.QtGui.QGuiApplication.topLevelWindows`, etc.

* It manages the application's mouse cursor handling, see :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor`

* It provides support for sophisticated session management. This makes it possible for applications to terminate gracefully when the user logs out, to cancel a shutdown process if termination isn't possible and even to preserve the entire application's state for a future session. See :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId` and :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest` and :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest` for details.

Since the :sip:ref:`~PyQt6.QtGui.QGuiApplication` object does so much initialization, it *must* be created before any other objects related to the user interface are created. :sip:ref:`~PyQt6.QtGui.QGuiApplication` also deals with common command line arguments. Hence, it is usually a good idea to create it *before* any interpretation or modification of ``argv`` is done in the application itself.

+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Groups of functions      |                                                                                                                                                                                                                                                                                                                                                                                        |
+==========================+========================================================================================================================================================================================================================================================================================================================================================================================+
| System settings          | :sip:ref:`~PyQt6.QtGui.QGuiApplication.desktopSettingsAware`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.setDesktopSettingsAware`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.styleHints`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.palette`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.setPalette`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.font`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.setFont`. |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event handling           | :sip:ref:`~PyQt6.QtGui.QGuiApplication.exec`, processEvents(), exit(), quit(). sendEvent(), postEvent(), sendPostedEvents(), removePostedEvents(), :sip:ref:`~PyQt6.QtGui.QGuiApplication.notify`.                                                                                                                                                                                     |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows                  | :sip:ref:`~PyQt6.QtGui.QGuiApplication.allWindows`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.topLevelWindows`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.focusWindow`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.clipboard`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.topLevelAt`.                                                                                                               |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Advanced cursor handling | :sip:ref:`~PyQt6.QtGui.QGuiApplication.overrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor`.                                                                                                                                                                                                      |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Session management       | :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest`.                                                                                                                                                     |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Miscellaneous            | startingUp(), closingDown().                                                                                                                                                                                                                                                                                                                                                           |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication`, :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`, :sip:ref:`~PyQt6.QtCore.QEventLoop`.
