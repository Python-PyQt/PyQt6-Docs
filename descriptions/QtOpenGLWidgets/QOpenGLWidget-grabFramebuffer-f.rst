.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: ()
    :digest: b7a6db8b77a90cb3754ae4c042d024e7

Renders and returns a 32-bit RGB image of the framebuffer.

**Note:** This is a potentially expensive operation because it relies on glReadPixels() to read back the pixels. This may be slow and can stall the GPU pipeline.
