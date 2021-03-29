.. sip:method-description::
    :status: todo
    :pysig: 226b5e1510ad722b6ec2ef3fd3f3750d
    :realsig: (const QString&,const QByteArray&,const QByteArray&)
    :digest: 6f708cdf7f3c134d039ce825ca2e96fb

Returns an encoded copy of *input*. *input* is first converted to UTF-8, and all ASCII-characters that are not in the unreserved group are percent encoded. To prevent characters from being percent encoded pass them to *exclude*. To force characters to be percent encoded pass them to *include*.

Unreserved is defined as: ``ALPHA / DIGIT / "-" / "." / "_" / "~"``

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 96-98
