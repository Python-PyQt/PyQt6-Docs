.. sip:class-description::
    :status: todo
    :brief: Performs a linear interpolation of two animation clips based on a normalized factor
    :realname: Qt3DAnimation::QLerpClipBlend
    :digest: aab8fbf4a7f508602858c7adfff53b11

Performs a linear interpolation of two animation clips based on a normalized factor.

:sip:ref:`~PyQt6.Qt3DAnimation.QLerpClipBlend` can be useful to create advanced animation effects based on individual animation clips. For instance, given a player character, lerp blending could be used to combine a walking animation clip with an injured animation clip based on a blend factor that increases the more the player gets injured. This would then allow with blend factor == 0 to have a non injured walking player, with blend factor == 1 a fully injured player, with blend factor == 0.5 a partially walking and injured player.

.. seealso:: QBlendedClipAnimator.
