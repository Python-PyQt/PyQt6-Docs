.. sip:method-description::
    :status: todo
    :pysig: d1b2d1e73b838b74c32f54d9656c2196
    :realsig: (const QString&,QQmlImageProviderBase*)
    :digest: 34cf4f7b32a17f0a0cae25ae9c262301

Sets the *provider* to use for images requested via the *image*: url scheme, with host *providerId*. The :sip:ref:`~PyQt6.QtQml.QQmlEngine` takes ownership of *provider*.

Image providers enable support for pixmap and threaded image requests. See the :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider` documentation for details on implementing and using image providers.

All required image providers should be added to the engine before any QML sources files are loaded.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.removeImageProvider`, :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider`, :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase`.
