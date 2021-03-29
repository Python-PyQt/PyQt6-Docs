.. sip:class-description::
    :status: todo
    :brief: Component providing animation playback capabilities of a tree of blend nodes
    :realname: Qt3DAnimation::QBlendedClipAnimator
    :digest: d5e79bf9e211addb562dab78cbe1c8db

:sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator` is a component providing animation playback capabilities of a tree of blend nodes.

An instance of :sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator` can be aggregated by a QEntity to add the ability to play back animation clips and to apply the calculated animation values to properties of QObjects.

Whereas a QClipAnimator gets its animation data from a single animation clip, :sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator` can blend together multiple clips. The animation data is obtained by evaluating a so called *blend tree*. A blend tree is a hierarchical tree structure where the leaf nodes are value nodes that encapsulate an animation clip (QAbstractAnimationClip); and the internal nodes represent blending operations that operate on the nodes pointed to by their operand properties.

To associate a blend tree with a :sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator`, set the animator's :sip:ref:`~PyQt6.Qt3DAnimation.QBlendedClipAnimator.blendTree` property to point at the root node of your blend tree:

::

    auto blendTreeRoot = new QAdditiveClipBlend();
    ...
    auto animator = new QBlendedClipAnimator();
    animator->setBlendTree(blendTreeRoot);

A blend tree can be constructed from the following node types:

**Note:** The blend node tree should only be edited when the animator is not running.

* :sip:ref:`~PyQt6.Qt3DAnimation.QClipBlendValue`

* :sip:ref:`~PyQt6.Qt3DAnimation.QLerpClipBlend`

* :sip:ref:`~PyQt6.Qt3DAnimation.QAdditiveClipBlend`

Additional node types will be added over time.

As an example consider the following blend tree:

::

    Clip0----
            |
            Lerp Node----
            |           |
    Clip1----           Additive Node
                        |
                Clip2----

This can be created and used as follows:

::

    // Create leaf nodes of blend tree
    auto clip0 = new QClipBlendValue(
        new QAnimationClipLoader(QUrl::fromLocalFile("walk.json")));
    auto clip1 = new QClipBlendValue(
        new QAnimationClipLoader(QUrl::fromLocalFile("run.json")));
    auto clip2 = new QClipBlendValue(
        new QAnimationClipLoader(QUrl::fromLocalFile("wave-arm.json")));

    // Create blend tree inner nodes
    auto lerpNode = new QLerpClipBlend();
    lerpNode->setStartClip(clip0);
    lerpNode->setEndClip(clip1);
    lerpNode->setBlendFactor(0.5f); // Half-walk, half-run

    auto additiveNode = new QAdditiveClipBlend();
    additiveNode->setBaseClip(lerpNode); // Comes from lerp sub-tree
    additiveNode->setAdditiveClip(clip2);
    additiveNode->setAdditiveFactor(1.0f); // Wave arm fully

    // Run the animator
    auto animator = new QBlendedClipAnimator();
    animator->setBlendTree(additiveNode);
    animator->setChannelMapper(...);
    animator->setRunning(true);

By authoring a set of animation clips and blending between them dynamically at runtime with a blend tree, we open up a huge set of possible resulting animations. As some simple examples of the above blend tree, where alpha is the additive factor and beta is the lerp blend factor we can get a 2D continuum of possible animations:

::

    (alpha = 0, beta = 1) Running, No arm waving --- (alpha = 1, beta = 1) Running, Arm waving
            |                                               |
            |                                               |
            |                                               |
    (alpha = 0, beta = 0) Walking, No arm waving --- (alpha = 0, beta = 1) Running, No arm waving

More complex blend trees offer even more flexibility for combining your animation clips. Note that the values used to control the blend tree (alpha and beta above) are simple properties on the blend nodes. This means, that these properties themselves can also be controlled by the animation framework.
