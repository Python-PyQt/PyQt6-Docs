.. sip:class-description::
    :status: todo
    :brief: Convenient interface for working with URLs
    :digest: ca78e9fd8d9b0ba93f4964a38dee02a5

The :sip:ref:`~PyQt6.QtCore.QUrl` class provides a convenient interface for working with URLs.

It can parse and construct URLs in both encoded and unencoded form. :sip:ref:`~PyQt6.QtCore.QUrl` also has support for internationalized domain names (IDNs).

The most common way to use :sip:ref:`~PyQt6.QtCore.QUrl` is to initialize it via the constructor by passing a QString containing a full URL. :sip:ref:`~PyQt6.QtCore.QUrl` objects can also be created from a :sip:ref:`~PyQt6.QtCore.QByteArray` containing a full URL using :sip:ref:`~PyQt6.QtCore.QUrl.fromEncoded`, or heuristically from incomplete URLs using :sip:ref:`~PyQt6.QtCore.QUrl.fromUserInput`. The URL representation can be obtained from a :sip:ref:`~PyQt6.QtCore.QUrl` using either :sip:ref:`~PyQt6.QtCore.QUrl.toString` or :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`.

URLs can be represented in two forms: encoded or unencoded. The unencoded representation is suitable for showing to users, but the encoded representation is typically what you would send to a web server. For example, the unencoded URL "http://bühler.example.com/List of applicants.xml" would be sent to the server as "http://xn–bhler-kva.example.com/List%20of%20applicants.xml".

A URL can also be constructed piece by piece by calling :sip:ref:`~PyQt6.QtCore.QUrl.setScheme`, :sip:ref:`~PyQt6.QtCore.QUrl.setUserName`, :sip:ref:`~PyQt6.QtCore.QUrl.setPassword`, :sip:ref:`~PyQt6.QtCore.QUrl.setHost`, :sip:ref:`~PyQt6.QtCore.QUrl.setPort`, :sip:ref:`~PyQt6.QtCore.QUrl.setPath`, :sip:ref:`~PyQt6.QtCore.QUrl.setQuery` and :sip:ref:`~PyQt6.QtCore.QUrl.setFragment`. Some convenience functions are also available: :sip:ref:`~PyQt6.QtCore.QUrl.setAuthority` sets the user name, password, host and port. :sip:ref:`~PyQt6.QtCore.QUrl.setUserInfo` sets the user name and password at once.

Call :sip:ref:`~PyQt6.QtCore.QUrl.isValid` to check if the URL is valid. This can be done at any point during the constructing of a URL. If :sip:ref:`~PyQt6.QtCore.QUrl.isValid` returns ``false``, you should :sip:ref:`~PyQt6.QtCore.QUrl.clear` the URL before proceeding, or start over by parsing a new URL with :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`.

Constructing a query is particularly convenient through the use of the :sip:ref:`~PyQt6.QtCore.QUrlQuery` class and its methods :sip:ref:`~PyQt6.QtCore.QUrlQuery.setQueryItems`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem` and :sip:ref:`~PyQt6.QtCore.QUrlQuery.removeQueryItem`. Use :sip:ref:`~PyQt6.QtCore.QUrlQuery.setQueryDelimiters` to customize the delimiters used for generating the query string.

For the convenience of generating encoded URL strings or query strings, there are two static functions called :sip:ref:`~PyQt6.QtCore.QUrl.fromPercentEncoding` and :sip:ref:`~PyQt6.QtCore.QUrl.toPercentEncoding` which deal with percent encoding and decoding of QString objects.

:sip:ref:`~PyQt6.QtCore.QUrl.fromLocalFile` constructs a :sip:ref:`~PyQt6.QtCore.QUrl` by parsing a local file path. :sip:ref:`~PyQt6.QtCore.QUrl.toLocalFile` converts a URL to a local file path.

The human readable representation of the URL is fetched with :sip:ref:`~PyQt6.QtCore.QUrl.toString`. This representation is appropriate for displaying a URL to a user in unencoded form. The encoded form however, as returned by :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, is for internal use, passing to web servers, mail clients and so on. Both forms are technically correct and represent the same URL unambiguously – in fact, passing either form to :sip:ref:`~PyQt6.QtCore.QUrl`'s constructor or to :sip:ref:`~PyQt6.QtCore.QUrl.setUrl` will yield the same :sip:ref:`~PyQt6.QtCore.QUrl` object.

:sip:ref:`~PyQt6.QtCore.QUrl` conforms to the URI specification from RFC 3986 (Uniform Resource Identifier: Generic Syntax), and includes scheme extensions from RFC 1738 (Uniform Resource Locators). Case folding rules in :sip:ref:`~PyQt6.QtCore.QUrl` conform to RFC 3491 (Nameprep: A Stringprep Profile for Internationalized Domain Names (IDN)). It is also compatible with the `file URI specification <http://freedesktop.org/wiki/Specifications/file-uri-spec/>`_ from freedesktop.org, provided that the locale encodes file names using UTF-8 (required by IDN).

.. _qurl-relative-urls-vs-relative-paths:

Relative URLs vs Relative Paths
...............................

Calling :sip:ref:`~PyQt6.QtCore.QUrl.isRelative` will return whether or not the URL is relative. A relative URL has no :sip:ref:`~PyQt6.QtCore.QUrl.scheme`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 108-111

Notice that a URL can be absolute while containing a relative path, and vice versa:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 115-123

A relative URL can be resolved by passing it as an argument to :sip:ref:`~PyQt6.QtCore.QUrl.resolved`, which returns an absolute URL. :sip:ref:`~PyQt6.QtCore.QUrl.isParentOf` is used for determining whether one URL is a parent of another.

.. _qurl-error-checking:

Error checking
..............

:sip:ref:`~PyQt6.QtCore.QUrl` is capable of detecting many errors in URLs while parsing it or when components of the URL are set with individual setter methods (like :sip:ref:`~PyQt6.QtCore.QUrl.setScheme`, :sip:ref:`~PyQt6.QtCore.QUrl.setHost` or :sip:ref:`~PyQt6.QtCore.QUrl.setPath`). If the parsing or setter function is successful, any previously recorded error conditions will be discarded.

By default, :sip:ref:`~PyQt6.QtCore.QUrl` setter methods operate in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`, which means they accept some common mistakes and mis-representation of data. An alternate method of parsing is :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, which applies further checks. See :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode` for a description of the difference of the parsing modes.

:sip:ref:`~PyQt6.QtCore.QUrl` only checks for conformance with the URL specification. It does not try to verify that high-level protocol URLs are in the format they are expected to be by handlers elsewhere. For example, the following URIs are all considered valid by :sip:ref:`~PyQt6.QtCore.QUrl`, even if they do not make sense when used:

* "http:/filename.html"

* "mailto://example.com"

When the parser encounters an error, it signals the event by making :sip:ref:`~PyQt6.QtCore.QUrl.isValid` return false and :sip:ref:`~PyQt6.QtCore.QUrl.toString` / :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded` return an empty string. If it is necessary to show the user the reason why the URL failed to parse, the error condition can be obtained from :sip:ref:`~PyQt6.QtCore.QUrl` by calling :sip:ref:`~PyQt6.QtCore.QUrl.errorString`. Note that this message is highly technical and may not make sense to end-users.

:sip:ref:`~PyQt6.QtCore.QUrl` is capable of recording only one error condition. If more than one error is found, it is undefined which error is reported.

.. _qurl-character-conversions:

Character Conversions
.....................

Follow these rules to avoid erroneous character conversion when dealing with URLs and strings:

* When creating a QString to contain a URL from a :sip:ref:`~PyQt6.QtCore.QByteArray` or a char\*, always use QString::fromUtf8().
