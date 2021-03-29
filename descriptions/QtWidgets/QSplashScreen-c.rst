.. sip:class-description::
    :status: todo
    :brief: Splash screen that can be shown during application startup
    :digest: 9616ac1893bc327ebf8d8097cccbc576

The :sip:ref:`~PyQt6.QtWidgets.QSplashScreen` widget provides a splash screen that can be shown during application startup.

A splash screen is a widget that is usually displayed when an application is being started. Splash screens are often used for applications that have long start up times (e.g. database or networking applications that take time to establish connections) to provide the user with feedback that the application is loading.

The splash screen appears in the center of the screen. It may be useful to add the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.WindowStaysOnTopHint` to the splash widget's window flags if you want to keep it above all the other windows on the desktop.

Some X11 window managers do not support the "stays on top" flag. A solution is to set up a timer that periodically calls raise() on the splash screen to simulate the "stays on top" effect.

The most common usage is to show a splash screen before the main widget is displayed on the screen. This is illustrated in the following code snippet in which a splash screen is displayed and some initialization tasks are performed before the application's main window is shown:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qsplashscreen-main.py
    :lines: 59-65

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qsplashscreen-main.py
    :lines: 70-74

The user can hide the splash screen by clicking on it with the mouse. Since the splash screen is typically displayed before the event loop has started running, it is necessary to periodically call :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents` to receive the mouse clicks.

It is sometimes useful to update the splash screen with messages, for example, announcing connections established or modules loaded as the application starts up:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qsplashscreen.py
    :lines: 54-66

:sip:ref:`~PyQt6.QtWidgets.QSplashScreen` supports this with the :sip:ref:`~PyQt6.QtWidgets.QSplashScreen.showMessage` function. If you wish to do your own drawing you can get a pointer to the pixmap used in the splash screen with :sip:ref:`~PyQt6.QtWidgets.QSplashScreen.pixmap`. Alternatively, you can subclass :sip:ref:`~PyQt6.QtWidgets.QSplashScreen` and reimplement :sip:ref:`~PyQt6.QtWidgets.QSplashScreen.drawContents`.

In case of having multiple screens, it is also possible to show the splash screen on a different screen than the primary one. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qsplashscreen-main.py
    :lines: 78-81
