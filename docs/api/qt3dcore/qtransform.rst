:orphan:

.. sip:class:: PyQt6.Qt3DCore.QTransform
    :inherits: :sip:ref:`~PyQt6.Qt3DCore.QComponent`
    :description: Qt3DCore/QTransform-c.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DCore/QTransform-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromAxes
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromAxes-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromAxesAndAngles
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromAxesAndAngles-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromAxesAndAngles
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromAxesAndAngles-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromAxisAndAngle
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromAxisAndAngle-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromAxisAndAngle
        :args:
            float
            float
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromAxisAndAngle-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromEulerAngles
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromEulerAngles-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.fromEulerAngles
        :args:
            float
            float
            float
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :static:
        :description: Qt3DCore/QTransform-fromEulerAngles-f-1.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.matrix
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: Qt3DCore/QTransform-matrix-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.rotateAround
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :static:
        :description: Qt3DCore/QTransform-rotateAround-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.rotateFromAxes
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :static:
        :description: Qt3DCore/QTransform-rotateFromAxes-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.rotation
        :returns:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :description: Qt3DCore/QTransform-rotation-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.rotationX
        :returns:
            float
        :description: Qt3DCore/QTransform-rotationX-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.rotationY
        :returns:
            float
        :description: Qt3DCore/QTransform-rotationY-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.rotationZ
        :returns:
            float
        :description: Qt3DCore/QTransform-rotationZ-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.scale
        :returns:
            float
        :description: Qt3DCore/QTransform-scale-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.scale3D
        :returns:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DCore/QTransform-scale3D-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setMatrix
        :args:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: Qt3DCore/QTransform-setMatrix-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setRotation
        :args:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :description: Qt3DCore/QTransform-setRotation-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setRotationX
        :args:
            float
        :description: Qt3DCore/QTransform-setRotationX-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setRotationY
        :args:
            float
        :description: Qt3DCore/QTransform-setRotationY-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setRotationZ
        :args:
            float
        :description: Qt3DCore/QTransform-setRotationZ-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setScale
        :args:
            float
        :description: Qt3DCore/QTransform-setScale-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setScale3D
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DCore/QTransform-setScale3D-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.setTranslation
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DCore/QTransform-setTranslation-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.translation
        :returns:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DCore/QTransform-translation-f.rst

    .. sip:method:: PyQt6.Qt3DCore.QTransform.worldMatrix
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: Qt3DCore/QTransform-worldMatrix-f.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.matrixChanged
        :description: Qt3DCore/QTransform-matrixChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.rotationChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QQuaternion`
        :description: Qt3DCore/QTransform-rotationChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.rotationXChanged
        :args:
            float
        :description: Qt3DCore/QTransform-rotationXChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.rotationYChanged
        :args:
            float
        :description: Qt3DCore/QTransform-rotationYChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.rotationZChanged
        :args:
            float
        :description: Qt3DCore/QTransform-rotationZChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.scale3DChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DCore/QTransform-scale3DChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.scaleChanged
        :args:
            float
        :description: Qt3DCore/QTransform-scaleChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.translationChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DCore/QTransform-translationChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DCore.QTransform.worldMatrixChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: Qt3DCore/QTransform-worldMatrixChanged-s.rst
