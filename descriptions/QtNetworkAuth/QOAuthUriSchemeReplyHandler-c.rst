.. sip:class-description::
    :status: todo
    :brief: Handles private/custom and https URI scheme redirects
    :digest: 98407b1bc3e54eca668a27fc2e329bc2

Handles private/custom and https URI scheme redirects.

This class serves as a reply handler for `OAuth 2.0 <https://datatracker.ietf.org/doc/html/rfc6749>`_ authorization processes that use private/custom or HTTPS URI schemes for redirection. It manages the reception of the authorization redirection (also known as the callback) and the subsequent acquisition of access tokens.

The `redirection URI <https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2>`_ is where the authorization server redirects the user-agent (typically, and preferably, the system browser) once the authorization part of the flow is complete.

The use of specific URI schemes requires configuration at the operating system level to associate the URI with the correct application. The way to set up this association varies between operating systems. See :ref:`qoauthurischemereplyhandler-platform-support-and-dependencies`.

This class complements :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthHttpServerReplyHandler`, which handles ``http`` schemes by setting up a localhost server.

The following code illustrates the usage. First, the needed variables:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers_p.py
    :lines: 101-102

Followed up by the OAuth setup (error handling omitted for brevity):

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py
    :lines: 69-79

Finally, we then set up the URI scheme reply-handler:

.. literalinclude:: ../../../snippets/qtnetworkauth-src-oauth-doc-snippets-src_oauth_replyhandlers.py
    :lines: 83-89

.. _qoauthurischemereplyhandler-private-custom-uri-schemes:

Private/Custom URI Schemes
--------------------------

Custom URI schemes typically use reverse-domain notation followed by a path, or occasionally a host/host+path:

::

    // Example with path:
    com.example.myapp:/oauth2/callback
    // Example with host:
    com.example.myapp://oauth2.callback

.. _qoauthurischemereplyhandler-https-uri-scheme:

HTTPS URI Scheme
----------------

With HTTPS URI schemes, the redirect URLs are regular https links:

::

    https://myapp.example.com/oauth2/callback

These links are called `Universal Links <https://developer.apple.com/ios/universal-links/>`_ on iOS and `App Links on Android <https://developer.android.com/training/app-links>`_.

The use of https schemes is recommended as it provides additional security by forcing application developers to prove ownership of the URLs used. This proving is done by hosting an association file, which the operating system will consult as part of its internal URL dispatching.

The content of this file associates the application and the used URLs. The association files must be publicly accessible without any HTTP redirects. In addition, the hosting site must have valid certificates and, at least with Android, the file must be served as ``application/json`` content-type (refer to your server's configuration guide).

In addition, https links can provide some usability benefits:

* The https URL doubles as a regular https link. If the user hasn't installed the application (since the URL wasn't handled by any application), the https link may for example serve instructions to do so.

* The application selection dialogue to open the URL may be avoided, and instead your application may be opened automatically

The tradeoff is that this requires extra setup as you need to set up this publicly-hosted association file.

.. _qoauthurischemereplyhandler-platform-support-and-dependencies:

Platform Support and Dependencies
---------------------------------

Currently supported platforms are Android, iOS, and macOS.

URI scheme listening is based on :sip:ref:`~PyQt6.QtGui.QDesktopServices.setUrlHandler` and :sip:ref:`~PyQt6.QtGui.QDesktopServices.unsetUrlHandler`. These are currently provided by Qt::Gui module and therefore :sip:ref:`~PyQt6.QtNetworkAuth` module depends on Qt::Gui. If :sip:ref:`~PyQt6.QtNetworkAuth` is built without Qt::Gui, :sip:ref:`~PyQt6.QtNetworkAuth.QOAuthUriSchemeReplyHandler` will not be included.

.. _qoauthurischemereplyhandler-android:

Android
.......

On Android the URI schemes require:

* Setting up intent-filters in the application manifest

* Optionally, for automatic verification with https schemes, hosting a site association file assetlinks.json

See also the `Qt Android Manifest File Configuration <https://doc.qt.io/qt-6/android-manifest-file-configuration.html>`_.

.. _qoauthurischemereplyhandler-ios-and-macos:

iOS and macOS
.............

On iOS and macOS the URI schemes require:

* Setting up site association entitlement

* With https schemes, hosting a site association file (``apple-app-site-association``)

.. _qoauthurischemereplyhandler-windows-linux:

Windows, Linux
..............

Currently not supported. However platforms and use cases supporting Qt WebEngine can still use this reply handler - see `Qt OAuth2 Browser Support <https://doc.qt.io/qt-6/qt-oauth2-browsersupport.html>`_ for details.
