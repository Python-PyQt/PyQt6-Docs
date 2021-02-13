.. sip:method-description::
    :status: todo
    :pysig: d155bbce5a0a067805adb2725d6083b7
    :realsig: (const QMap<QByteArray,QVariant>&)
    :digest: 746ef591dfae1f85544fccc8e2077a8d

Sets or clears the backend-specific configuration.

Without a *backendConfiguration* parameter this function will clear the backend-specific configuration. More information about the supported options is available in the documentation of :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setBackendConfigurationOption`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.backendConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setBackendConfigurationOption`.
