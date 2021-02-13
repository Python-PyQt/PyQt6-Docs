.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 196419225e981d1596a83f5ff630fdfc

Marks the entire window as dirty and schedules a repaint.

**Note:** Subsequent calls to this function before the next paint event will get ignored.

**Note:** For non-exposed windows the update is deferred until the window becomes exposed again.
