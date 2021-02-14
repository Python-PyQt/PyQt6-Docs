.. sip:class-description::
    :status: todo
    :brief: Used to perform transforms on meshes
    :realname: Qt3DCore::QTransform
    :digest: ee11787430d7b20ac361e4f8df844ae6

Used to perform transforms on meshes.

The :sip:ref:`~PyQt6.Qt3DCore.QTransform` component is not shareable between multiple QEntity's. The transformation is held as :sip:ref:`~PyQt6.QtGui.QVector3D` scale, :sip:ref:`~PyQt6.QtGui.QQuaternion` rotation and :sip:ref:`~PyQt6.QtGui.QVector3D` translation components. The transformations are applied to the mesh in that order. When QTransform::matrix property is set, it is decomposed to these transform components and corresponding signals are emitted.

Several helper functions are provided to set up the :sip:ref:`~PyQt6.Qt3DCore.QTransform`; :sip:ref:`~PyQt6.Qt3DCore.QTransform.fromAxisAndAngle` and :sip:ref:`~PyQt6.Qt3DCore.QTransform.fromAxesAndAngles` can be used to set the rotation around specific axes, :sip:ref:`~PyQt6.Qt3DCore.QTransform.fromEulerAngles` can be used to set the rotation based on euler angles and :sip:ref:`~PyQt6.Qt3DCore.QTransform.rotateAround` can be used to rotate the object around specific point relative to local origin.
