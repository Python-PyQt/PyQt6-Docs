.. sip:class-description::
    :status: todo
    :brief: Interface for loading custom textures from QML
    :digest: 8674d297f5df55e56c6d4afb8da872b2

The :sip:ref:`~PyQt6.QtQuick.QQuickTextureFactory` class provides an interface for loading custom textures from QML.

The purpose of the texture factory is to provide a placeholder for a image data that can be converted into an OpenGL texture.

Creating a texture directly is not possible as there is rarely an OpenGL context available in the thread that is responsible for loading the image data.
