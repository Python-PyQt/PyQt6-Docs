.. sip:class-description::
    :status: todo
    :brief: Enables or disables entire subtrees of framegraph nodes
    :realname: Qt3DRender::QSubtreeEnabler
    :digest: 03f2e497e38c8eeddd59508b8bb4a1ae

Enables or disables entire subtrees of framegraph nodes.

While QFrameGraphNodes can be individually enabled and disabled via the ``enabled`` property, this can become tedious when an entire path needs to be turned on or off. :sip:ref:`~PyQt6.Qt3DRender.QSubtreeEnabler` is a convenience node that makes this use case trivial, allowing all of its children to be controlled by a single switch.

:sip:ref:`~PyQt6.Qt3DRender.QSubtreeEnabler` is enabled by default.
