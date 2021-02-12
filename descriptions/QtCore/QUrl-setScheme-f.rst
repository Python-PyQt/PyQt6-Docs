.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: a82f33887fb153f7c878a026b33c131a

Sets the scheme of the URL to *scheme*. As a scheme can only contain ASCII characters, no conversion or decoding is done on the input. It must also start with an ASCII letter.

The scheme describes the type (or protocol) of the URL. It's represented by one or more ASCII characters at the start the URL.

A scheme is strictly `RFC 3986 <http://www.ietf.org/rfc/rfc3986.txt>`_-compliant: ``scheme = ALPHA \*( ALPHA / DIGIT / "+" / "-" / "." )``

The following example shows a URL where the scheme is "ftp":

.. image:: ../../../images/qurl-authority2.png

To set the scheme, the following call is used:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 136-137

The scheme can also be empty, in which case the URL is interpreted as relative.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.scheme`, :sip:ref:`~PyQt6.QtCore.QUrl.isRelative`.
