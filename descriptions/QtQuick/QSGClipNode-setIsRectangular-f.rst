.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 551982e61f436360488dd96511a03abf

Sets whether this clip node has a rectangular clip to *rectHint*.

This is an optimization hint which means that the renderer can use scissoring instead of stencil, which is significantly faster.

When this hint is set and it is applicable, the clip region will be generated from :sip:ref:`~PyQt6.QtQuick.QSGClipNode.clipRect` rather than geometry().

By default this property is ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGClipNode.isRectangular`.
