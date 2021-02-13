.. sip:method-description::
    :status: todo
    :pysig: b50101d8bfae203ac36738ea6bf758e3
    :realsig: (const QString&,QSsl::EncodingFormat,QSslCertificate::PatternSyntax)
    :digest: ce0f3668d8120d51a1bfbd15428b4c1a

Searches all files in the *path* for certificates encoded in the specified *format* and returns them in a list. *path* must be a file or a pattern matching one or more files, as specified by *syntax*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslcertificate.py
    :lines: 54-58

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.fromData`.
