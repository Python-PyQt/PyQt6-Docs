.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: ()
    :digest: 90ad472c5cc5a4419ad01ab552fb1853

Attempts to load the platform-default backend.

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

This function is provided for convenience where the default for a given platform is good enough. If you are not using the default plugins you must use one of the other :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load` overloads.

Returns ``true`` if it managed to load the backend or if it was already loaded. Returns ``false`` otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.instance`, :sip:ref:`~PyQt6.QtNetwork.QNetworkInformation.load`.
