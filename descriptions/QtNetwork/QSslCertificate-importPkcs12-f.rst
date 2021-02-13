.. sip:method-description::
    :status: todo
    :pysig: 24f5c46864a4b8276998ff5e882ab4fa
    :realsig: (QIODevice*,QSslKey*,QSslCertificate*,QList<QSslCertificate>*,const QByteArray&)
    :digest: 4fdf8dc5800fc877fa763b3cc7b8994e

Imports a PKCS#12 (pfx) file from the specified *device*. A PKCS#12 file is a bundle that can contain a number of certificates and keys. This method reads a single *key*, its *certificate* and any associated *caCertificates* from the bundle. If a *passPhrase* is specified then this will be used to decrypt the bundle. Returns ``true`` if the PKCS#12 file was successfully loaded.

**Note:** The *device* must be open and ready to be read from.
