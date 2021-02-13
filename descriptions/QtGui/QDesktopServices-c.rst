.. sip:class-description::
    :status: todo
    :brief: Methods for accessing common desktop services
    :digest: b03f39bbc66be9fddc1383f478513760

The :sip:ref:`~PyQt6.QtGui.QDesktopServices` class provides methods for accessing common desktop services.

Many desktop environments provide services that can be used by applications to perform common tasks, such as opening a web page, in a way that is both consistent and takes into account the user's application preferences.

This class contains functions that provide simple interfaces to these services that indicate whether they succeeded or failed.

The :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` function is used to open files located at arbitrary URLs in external applications. For URLs that correspond to resources on the local filing system (where the URL scheme is "file"), a suitable application will be used to open the file; otherwise, a web browser will be used to fetch and display the file.

The user's desktop settings control whether certain executable file types are opened for browsing, or if they are executed instead. Some desktop environments are configured to prevent users from executing files obtained from non-local URLs, or to ask the user's permission before doing so.

.. _qdesktopservices-url-handlers:

URL Handlers
------------

The behavior of the :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` function can be customized for individual URL schemes to allow applications to override the default handling behavior for certain types of URLs.

The dispatch mechanism allows only one custom handler to be used for each URL scheme; this is set using the :sip:ref:`~PyQt6.QtGui.QDesktopServices.setUrlHandler` function. Each handler is implemented as a slot which accepts only a single :sip:ref:`~PyQt6.QtCore.QUrl` argument.

The existing handlers for each scheme can be removed with the :sip:ref:`~PyQt6.QtGui.QDesktopServices.unsetUrlHandler` function. This returns the handling behavior for the given scheme to the default behavior.

This system makes it easy to implement a help system, for example. Help could be provided in labels and text browsers using help://myapplication/mytopic URLs, and by registering a handler it becomes possible to display the help text inside the application:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 60-67

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 73-73

If inside the handler you decide that you can't open the requested URL, you can just call :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` again with the same argument, and it will try to open the URL using the appropriate mechanism for the user's desktop environment.

Combined with platform specific settings, the schemes registered by the :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` function can also be exposed to other applications, opening up for application deep linking or a very basic URL-based IPC mechanism.

.. seealso:: `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_, :sip:ref:`~PyQt6.QtCore.QStandardPaths`, :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon`.
