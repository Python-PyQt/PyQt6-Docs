.. sip:method-description::
    :status: todo
    :pysig: 1eef66a026ef49fb16c6bad28df55d16
    :realsig: (const QString&,QObject*,const char*)
    :digest: 7ffaadeae4c464b92168c082f9151214

Sets the handler for the given *scheme* to be the handler *method* provided by the *receiver* object.

This function provides a way to customize the behavior of :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl`. If :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` is called with a URL with the specified *scheme* then the given *method* on the *receiver* object is called instead of :sip:ref:`~PyQt6.QtGui.QDesktopServices` launching an external application.

The provided method must be implemented as a slot that only accepts a single :sip:ref:`~PyQt6.QtCore.QUrl` argument.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 60-67

To use this function for receiving data from other apps on iOS you also need to add the custom scheme to the ``CFBundleURLSchemes`` list in your Info.plist file:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 104-112

For more information, see the Apple Developer Documentation for `Communicating with Other Apps Using Custom URLs <https://developer.apple.com/documentation/uikit/core_app/allowing_apps_and_websites_to_link_to_your_content/communicating_with_other_apps_using_custom_urls?language=objc>`_.

**Warning:** It is not possible to claim support for some well known URL schemes, including http and https. This is only allowed for Universal Links.

To claim support for http and https the above entry in the Info.plist file is not allowed. This is only possible when you add your domain to the Entitlements file:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 128-131

iOS will search for /.well-known/apple-app-site-association on your domain, when the application is installed. If you want to listen to https://your.domain.com/help?topic=ABCDEF you need to provide the following content there:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qdesktopservices.py
    :lines: 135-146

For more information, see the Apple Developer Documentation for `https://developer.apple.com/documentation/safariservices/supporting_associated_domains_in_your_app <https://developer.apple.com/documentation/safariservices/supporting_associated_domains_in_your_app>`_[Supporting Associated Domains}.

If  is used to set a new handler for a scheme which already has a handler, the existing handler is simply replaced with the new one. Since :sip:ref:`~PyQt6.QtGui.QDesktopServices` does not take ownership of handlers, no objects are deleted when a handler is replaced.

Note that the handler will always be called from within the same thread that calls :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl`, :sip:ref:`~PyQt6.QtGui.QDesktopServices.unsetUrlHandler`.
