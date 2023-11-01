.. sip:class-description::
    :status: todo
    :brief: API for accessing the extensions of an X509 certificate
    :digest: f7699439af1657f24001adef0842682e

The :sip:ref:`~PyQt6.QtNetwork.QSslCertificateExtension` class provides an API for accessing the extensions of an X509 certificate.

:sip:ref:`~PyQt6.QtNetwork.QSslCertificateExtension` provides access to an extension stored in an X509 certificate. The information available depends on the type of extension being accessed.

All X509 certificate extensions have the following properties:

+-------------+------------------------------------------------------------------------------------------------------------+
| Property    | Description                                                                                                |
+=============+============================================================================================================+
| name        | The human readable name of the extension, eg. 'basicConstraints'.                                          |
+-------------+------------------------------------------------------------------------------------------------------------+
| criticality | This is a boolean value indicating if the extension is critical to correctly interpreting the certificate. |
+-------------+------------------------------------------------------------------------------------------------------------+
| oid         | The ASN.1 object identifier that specifies which extension this is.                                        |
+-------------+------------------------------------------------------------------------------------------------------------+
| supported   | If this is true the structure of the extension's value will not change between Qt versions.                |
+-------------+------------------------------------------------------------------------------------------------------------+
| value       | A :sip:ref:`~PyQt6.QtCore.QVariant` with a structure dependent on the type of extension.                   |
+-------------+------------------------------------------------------------------------------------------------------------+

Whilst this class provides access to any type of extension, only some are guaranteed to be returned in a format that will remain unchanged between releases. The :sip:ref:`~PyQt6.QtNetwork.QSslCertificateExtension.isSupported` method returns ``true`` for extensions where this is the case.

The extensions currently supported, and the structure of the value returned are as follows:

+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                   | OID               | Details                                                                                                                                                                                                                                                                                                          |
+========================+===================+==================================================================================================================================================================================================================================================================================================================+
| basicConstraints       | 2.5.29.19         | Returned as a QVariantMap. The key 'ca' contains a boolean value, the optional key 'pathLenConstraint' contains an integer.                                                                                                                                                                                      |
+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| authorityInfoAccess    | 1.3.6.1.5.5.7.1.1 | Returned as a QVariantMap. There is a key for each access method, with the value being a URI.                                                                                                                                                                                                                    |
+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| subjectKeyIdentifier   | 2.5.29.14         | Returned as a :sip:ref:`~PyQt6.QtCore.QVariant` containing a QString. The string is the key identifier.                                                                                                                                                                                                          |
+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| authorityKeyIdentifier | 2.5.29.35         | Returned as a QVariantMap. The optional key 'keyid' contains the key identifier as a hex string stored in a :sip:ref:`~PyQt6.QtCore.QByteArray`. The optional key 'serial' contains the authority key serial number as a qlonglong. Currently there is no support for the general names field of this extension. |
+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In addition to the supported extensions above, many other common extensions will be returned in a reasonably structured way. Extensions that the SSL backend has no support for at all will be returned as a :sip:ref:`~PyQt6.QtCore.QByteArray`.

Further information about the types of extensions certificates can contain can be found in RFC 5280.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate.extensions`.
