.. sip:method-description::
    :status: todo
    :pysig: f036f485eb055d6ec1bb498745801d23
    :realsig: (const QRect&)
    :digest: 49c580e7e6eda738c241e90b76f68cb4

Marks the *rect* of the window as dirty and schedules a repaint.

**Note:** Subsequent calls to this function before the next paint event will get ignored, but *rect* is added to the region to update.

**Note:** For non-exposed windows the update is deferred until the window becomes exposed again.
