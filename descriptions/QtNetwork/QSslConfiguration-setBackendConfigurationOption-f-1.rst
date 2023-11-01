.. sip:method-description::
    :status: todo
    :pysig: e1722fde2b9fc7a7fe536b5edc796108
    :realsig: (const QByteArray&, const QVariant&)
    :digest: 477a5eb72c79d26ef2e0c3d1044e0df7

Sets the option *name* in the backend-specific configuration to *value*.

Options supported by the OpenSSL (>= 1.0.2) backend are available in the `supported configuration file commands <https://www.openssl.org/docs/manmaster/man3/SSL_CONF_cmd.html#SUPPORTED-CONFIGURATION-FILE-COMMANDS>`_ documentation. The expected type for the *value* parameter is a :sip:ref:`~PyQt6.QtCore.QByteArray` for all options. The `examples <https://www.openssl.org/docs/manmaster/man3/SSL_CONF_cmd.html#EXAMPLES>`_ show how to use some of the options.

**Note:** The backend-specific configuration will be applied after the general configuration. Using the backend-specific configuration to set a general configuration option again will overwrite the general configuration option.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.backendConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setBackendConfiguration`.
