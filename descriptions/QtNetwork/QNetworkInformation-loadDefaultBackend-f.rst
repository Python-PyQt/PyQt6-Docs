.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: ()
    :digest: d861bef6abd5f50234a0e024c65e6e4b

Attempts to load the platform-default backend.

**Note:** Starting with 6.7 this tries to load any backend that supports :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.Feature.Reachability` if the platform-default backend is not available or fails to load. If this also fails it will fall back to a backend that only returns the default values for all properties.

This platform-to-plugin mapping is as follows:

+-------------------+-----------------------+
| Platform          | Plugin-name           |
+===================+=======================+
| Windows           | networklistmanager    |
+-------------------+-----------------------+
| Apple (macOS/iOS) | scnetworkreachability |
+-------------------+-----------------------+
| Android           | android               |
+-------------------+-----------------------+
| Linux             | networkmanager        |
+-------------------+-----------------------+

This function is provided for convenience where the logic earlier is good enough. If you require a specific plugin then you should call :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.loadBackendByName` or :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.loadBackendByFeatures` directly instead.

Determines a suitable backend to load and returns ``true`` if this backend is already loaded or on successful loading of it. Returns ``false`` if any other backend has already been loaded, or if loading of the selected backend fails.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.instance`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load`.
