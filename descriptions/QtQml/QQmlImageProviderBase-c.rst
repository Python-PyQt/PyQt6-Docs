.. sip:class-description::
    :status: todo
    :brief: Used to register image providers in the QML engine
    :digest: afba729603514fccd6073ff386392ae4

The :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase` class is used to register image providers in the QML engine.

Image providers must be registered with the QML engine. The only information the QML engine knows about image providers is the type of image data they provide. To use an image provider to acquire image data, you must cast the :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase` pointer to a :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider` pointer.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider`, :sip:ref:`~PyQt6.QtQuick.QQuickTextureFactory`.
