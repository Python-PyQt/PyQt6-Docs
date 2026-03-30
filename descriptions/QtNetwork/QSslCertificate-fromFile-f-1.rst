.. sip:method-description::
    :status: todo
    :pysig: 265217c73b0e2e179a827ec35a717653
    :realsig: (const QString&, QSsl::EncodingFormat)
    :digest: 0c4b1422d318a601fd8f985b94521679

Reads the data from the file *filePath* and parses all certificates that are encoded in the specified *format* and returns a list of :sip:ref:`~PyQt6.QtNetwork.QSslCertificate` objects.

If *filePath* isn't a regular file, this method will return an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.fromData`, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.fromPath`.
