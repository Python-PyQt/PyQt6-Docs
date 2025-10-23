.. sip:method-description::
    :status: todo
    :pysig: 5e73ce7c084a5367655f59f19c482cd7
    :realsig: (const QString&, QSsl::EncodingFormat)
    :digest: 0c4b1422d318a601fd8f985b94521679

Reads the data from the file *filePath* and parses all certificates that are encoded in the specified *format* and returns a list of :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` objects.

If *filePath* isn't a regular file, this method will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.fromData`, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.fromPath`.
