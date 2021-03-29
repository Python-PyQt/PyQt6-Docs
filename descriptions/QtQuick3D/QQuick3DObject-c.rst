.. sip:class-description::
    :status: todo
    :brief: Base class of all 3D nodes and resources
    :digest: a15bb81eb828ac25a845dc0fc4ff6d26

Base class of all 3D nodes and resources.

`Object3D <https://doc.qt.io/qt-6/qml-qtquick3d-object3d.html>`_ is the base class for all Qt Quick 3D scene objects. Currently the types available in C++ are:

* :sip:ref:`~PyQt6.QtQuick3D.QQuick3DGeometry`

* :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData`

Both of these types are resource objects which directly inherit :sip:ref:`~PyQt6.QtQuick3D.QQuick3DObject`.

It should not be necessary to use :sip:ref:`~PyQt6.QtQuick3D.QQuick3DObject` directly anywhere currently because it is just an interface for supporting spatial items and resources in a 3D scene, as well as exposing similar functionality as :sip:ref:`~PyQt6.QtQuick.QQuickItem` for 3D scene content.
