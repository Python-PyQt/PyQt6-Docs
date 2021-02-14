.. sip:class-description::
    :status: todo
    :brief: The base class for types used to construct animation blend trees
    :realname: Qt3DAnimation::QAbstractClipBlendNode
    :digest: ffad559f59bdc96cfaf6d182e57b2771

:sip:ref:`~PyQt6.Qt3DAnimation.QAbstractClipBlendNode` is the base class for types used to construct animation blend trees.

Animation blend trees are used with a QBlendedClipAnimator to dynamically blend a set of animation clips together. The way in which the blending of animation clips is performed is controlled by the structure of the blend tree and the properties on the nodes it contains.

The leaf nodes in a blend tree are containers for the input animation clips. These clips can be baked clips read from file via QAnimationClipLoader, or they can be clips that you build within your application with QAnimatitonClip and QAnimationClipData. To include a clip in your blend tree, wrap it in a QClipBlendValue node.

The interior nodes of a blend tree represent blending operations that will be applied to their arguments which hold the input clips or even entire sub-trees of other blend tree nodes.

At present, the Qt 3D Animation module provides the following blend tree node types:

* :sip:ref:`~PyQt6.Qt3DAnimation.QClipBlendValue`

* :sip:ref:`~PyQt6.Qt3DAnimation.QLerpClipBlend`

* :sip:ref:`~PyQt6.Qt3DAnimation.QAdditiveClipBlend`

Additional node types representing other blending operations will be added in the future.

.. seealso:: QBlendedClipAnimator.
