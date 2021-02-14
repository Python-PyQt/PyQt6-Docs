.. sip:class-description::
    :status: todo
    :brief: A class implementing blend-shape morphing animation
    :realname: Qt3DAnimation::QMorphingAnimation
    :digest: d1c1ee3adb0ea85ac41ead30043036e9

A class implementing blend-shape morphing animation.

A :sip:ref:`~PyQt6.Qt3DAnimation.QMorphingAnimation` class implements blend-shape morphing animation to a target :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer`. The :sip:ref:`~PyQt6.Qt3DAnimation.QMorphingAnimation` sets the correct :sip:ref:`~PyQt6.Qt3DCore.QAttribute` from the :sip:ref:`~PyQt6.Qt3DAnimation.QMorphTarget` to the target :sip:ref:`~PyQt6.Qt3DRender.QGeometryRenderer.geometry` and calculates interpolator for the current position. The actual blending between the attributes must be implemented in the material. Qt3DAnimation::QMorphPhongMaterial implements material with morphing support for phong lighting model. The blending happens between 2 attributes - 'base' and 'target'. The names for the base and target attributes are taken from the morph target names, where the base attribute retains the name it already has and the target attribute name gets 'Target' appended to the name. The interpolator can be set as a :sip:ref:`~PyQt6.Qt3DRender.QParameter` to the used material. All morph targets in the animation should contain the attributes with same names as those in the base geometry.
