.. sip:method-description::
    :status: todo
    :pysig: e29038ad9f0ea4ee5e1065bf7926b1f2
    :realsig: (const QUrl&)
    :digest: 20d2e421358bf33fe01fc38f5aa4118d

Opens the given *url* in the appropriate Web browser for the user's desktop environment, and returns ``true`` if successful; otherwise returns ``false``.

If the URL is a reference to a local file (i.e., the URL scheme is "file") then it will be opened with a suitable application instead of a Web browser.

The following example opens a file on the Windows file system residing on a path that contains spaces:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 89-89

If a ``mailto`` URL is specified, the user's e-mail client will be used to open a composer window containing the options specified in the URL, similar to the way ``mailto`` links are handled by a Web browser.

For example, the following URL contains a recipient (``user@foo.com``), a subject (``Test``), and a message body (``Just a test``):

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 81-81

**Warning:** Although many e-mail clients can send attachments and are Unicode-aware, the user may have configured their client without these features. Also, certain e-mail clients (e.g., Lotus Notes) have problems with long URLs.

**Warning:** A return value of ``true`` indicates that the application has successfully requested the operating system to open the URL in an external application. The external application may still fail to launch or fail to open the requested URL. This result will not be reported back to the application.

**Warning:** URLs passed to this function on iOS will not load unless their schemes are listed in the ``LSApplicationQueriesSchemes`` key of the application's Info.plist file. For more information, see the Apple Developer Documentation for canOpenURL:. For example, the following lines enable URLs with the HTTPS scheme:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 97-100

**Note:** For Android Nougat (SDK 24) and above, URLs with a ``file`` scheme are opened using `FileProvider <https://doc.qt.io/qt-6/https://developer.android.com/reference/androidx/core/content/FileProvider>`_ which tries to obtain a shareable ``content`` scheme URI first. For that reason, Qt for Android defines a file provider with the authority ``${applicationId}.qtprovider``, with ``applicationId`` being the app's package name to avoid name conflicts. For more information, also see `Setting up file sharing <https://doc.qt.io/qt-6/https://developer.android.com/training/secure-file-sharing/setup-sharing.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDesktopServices.setUrlHandler`.
