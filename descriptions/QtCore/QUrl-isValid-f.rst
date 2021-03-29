.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 114c6357ff3b4002f085dc8a11c99c13

Returns ``true`` if the URL is non-empty and valid; otherwise returns ``false``.

The URL is run through a conformance test. Every part of the URL must conform to the standard encoding rules of the URI standard for the URL to be reported as valid.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 65-72
