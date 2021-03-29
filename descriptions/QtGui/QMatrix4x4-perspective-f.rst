.. sip:method-description::
    :status: todo
    :pysig: 5fd70130e629f44666196fc320d4f2e1
    :realsig: (float,float,float,float)
    :digest: cecf615b1222c38d131ae7f32f4165a2

Multiplies this matrix by another that applies a perspective projection. The vertical field of view will be *verticalAngle* degrees within a window with a given *aspectRatio* that determines the horizontal field of view. The projection will have the specified *nearPlane* and *farPlane* clipping planes which are the distances from the viewer to the corresponding planes.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMatrix4x4.ortho`, :sip:ref:`~PyQt6.QtGui.QMatrix4x4.frustum`.
