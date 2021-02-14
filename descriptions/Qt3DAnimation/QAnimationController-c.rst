.. sip:class-description::
    :status: todo
    :brief: A controller class for animations
    :realname: Qt3DAnimation::QAnimationController
    :digest: dca087542292c11b4eadf66f840355a9

A controller class for animations.

:sip:ref:`~PyQt6.Qt3DAnimation.QAnimationController` class controls the selection and playback of animations. The class can be used to find all animations from :sip:ref:`~PyQt6.Qt3DCore.QEntity` tree and create :sip:ref:`~PyQt6.Qt3DAnimation.QAnimationGroup` from the animations with the same name. The user can select which animation group is currently controlled with the animation controller by setting the active animation. The animation position is then propagated to that group after scaling and offsetting the provided position value with the :sip:ref:`~PyQt6.Qt3DAnimation.QAnimationController.positionScale` and :sip:ref:`~PyQt6.Qt3DAnimation.QAnimationController.positionOffset` values.

**Note:** that the animation controller doesn't have internal timer, but instead the user is responsible for updating the position property in timely manner.
