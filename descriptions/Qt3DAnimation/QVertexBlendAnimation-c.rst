.. sip:class-description::
    :status: todo
    :brief: A class implementing vertex-blend morphing animation
    :realname: Qt3DAnimation::QVertexBlendAnimation
    :digest: 6d109a18510ff02ec007d7f149232d81

A class implementing vertex-blend morphing animation.

A :sip:ref:`~PyQt6.Qt3DAnimation.QVertexBlendAnimation` class implements vertex-blend morphing animation to a target :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer`. The :sip:ref:`~PyQt6.Qt3DAnimation.QVertexBlendAnimation` sets the correct :sip:ref:`~PyQt6.Qt3DCore.QAttribute` from the :sip:ref:`~PyQt6.Qt3DAnimation.QMorphTarget` to the target :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer.geometry` and calculates interpolator for the current position. Unlike with QMorphingAnimation, where the blending is controller with blend weights, the blending occurs between sequential morph targets. The actual blending between the attributes must be implemented in the material. Qt3DAnimation::QMorphPhongMaterial implements material with morphing support for phong lighting model. The blending happens between 2 attributes - 'base' and 'target'. The names for the base and target attributes are taken from the morph target names, where the base attribute retains the name it already has and the target attribute name gets 'Target' appended to the name. The interpolator can be set as a :sip:ref:`~PyQt6.Qt3DRender.QParameter` to the used material. All morph targets in the animation should contain the attributes with same names as those in the base geometry.
