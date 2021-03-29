.. sip:method-description::
    :status: todo
    :pysig: 7b302619a1f8d21d9efa913403e8d56b
    :realsig: (const QRegion&)
    :digest: 021e1baf62f4b10cf2bbd533611fad1c

Marks the *region* of the window as dirty and schedules a repaint.

**Note:** Subsequent calls to this function before the next paint event will get ignored, but *region* is added to the region to update.

**Note:** For non-exposed windows the update is deferred until the window becomes exposed again.
