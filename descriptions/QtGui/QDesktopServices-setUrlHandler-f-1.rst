.. sip:method-description::
    :status: todo
    :pysig: 1eef66a026ef49fb16c6bad28df55d16
    :realsig: (const QString&,QObject*,const char*)
    :digest: 074f7ab1735501c34920837d1e6e3a43

Sets the handler for the given *scheme* to be the handler *method* provided by the *receiver* object.

This function provides a way to customize the behavior of :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl`. If :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` is called with a URL with the specified *scheme* then the given *method* on the *receiver* object is called instead of :sip:ref:`~PyQt6.QtGui.QDesktopServices` launching an external application.

The provided method must be implemented as a slot that only accepts a single :sip:ref:`~PyQt6.QtCore.QUrl` argument.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 60-67

If  is used to set a new handler for a scheme which already has a handler, the existing handler is simply replaced with the new one. Since :sip:ref:`~PyQt6.QtGui.QDesktopServices` does not take ownership of handlers, no objects are deleted when a handler is replaced.

Note that the handler will always be called from within the same thread that calls :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl`.

iOS
---

To use this function for receiving data from other apps on iOS you also need to add the custom scheme to the ``CFBundleURLSchemes`` list in your Info.plist file:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 104-112

For more information, see the Apple Developer Documentation for Defining a Custom URL Scheme for Your App.

**Warning:** It is not possible to claim support for some well known URL schemes, including http and https. This is only allowed for Universal Links.

To claim support for http and https the above entry in the Info.plist file is not allowed. This is only possible when you add your domain to the Entitlements file:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 128-131

iOS will search for /.well-known/apple-app-site-association on your domain, when the application is installed. If you want to listen to ``https://your.domain.com/help?topic=ABCDEF`` you need to provide the following content there:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 135-146

For more information, see the Apple Developer Documentation for Supporting Associated Domains.

Android
-------

To use this function for receiving data from other apps on Android, you need to add one or more intent filter to the ``activity`` in your app manifest:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py

For more information, see the Android Developer Documentation for Create Deep Links to App Content.

To immediately open the corresponding content in your Android app, without requiring the user to select the app, you need to verify your link. To enable the verification, add an additional parameter to your intent filter:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py

Android will look for ``https://your.domain.com/.well-known/assetlinks.json``, when the application is installed. If you want to listen to ``https://your.domain.com:1337/help``, you need to provide the following content there:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py

For more information, see the Android Developer Documentation for Verify Android App Links.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl`, :sip:ref:`~PyQt6.QtGui.QDesktopServices.unsetUrlHandler`.
