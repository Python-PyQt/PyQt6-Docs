.. sip:class-description::
    :status: todo
    :brief: Event that will be sent when there is a request to open a file or a URL
    :digest: 9a5c6715bd1e0a6d0e8c98d7d1cfbc27

The :sip:ref:`~PyQt6.QtGui.QFileOpenEvent` class provides an event that will be sent when there is a request to open a file or a URL.

File open events will be sent to the QApplication::instance() when the operating system requests that a file or URL should be opened. This is a high-level event that can be caused by different user actions depending on the user's desktop environment; for example, double clicking on an file icon in the Finder on macOS.

This event is only used to notify the application of a request. It may be safely ignored.

**Note:** This class is currently supported for macOS only.

.. _qfileopenevent-macos-example:

macOS Example
-------------

In order to trigger the event on macOS, the application must be configured to let the OS know what kind of file(s) it should react on.

For example, the following ``Info.plist`` file declares that the application can act as a viewer for files with a PNG extension:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qfileopenevent-Info.plist
    :lines: 54-70

The following implementation of a :sip:ref:`~PyQt6.QtWidgets.QApplication` subclass shows how to handle :sip:ref:`~PyQt6.QtGui.QFileOpenEvent` to open the file that was, for example, dropped on the Dock icon of the application.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qfileopenevent-main.py
    :lines: 54-76

Note how ``QFileOpenEvent::file()`` is not guaranteed to be the name of a local file that can be opened using :sip:ref:`~PyQt6.QtCore.QFile`. The contents of the string depend on the source application.
