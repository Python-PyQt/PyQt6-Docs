.. sip:method-description::
    :status: todo
    :pysig: 3d68fd44a7f90d7ff616d010e35ec2e3
    :realsig: (const QUrl&, const QMultiMap<QString, QVariant>&)
    :digest: e74d158126d70fca06e8d298a5a56a33

Builds the resource owner authorization URL to be used in the web browser: *url* is used as the base URL and the query is created using *parameters*. When the URL is ready, the :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.authorizeWithBrowser` signal will be emitted with the generated URL.

.. seealso:: :sip:ref:`~PyQt6.QtNetworkAuth.QAbstractOAuth.authorizeWithBrowser`.
