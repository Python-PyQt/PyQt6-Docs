.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 0270b02560971f13a694d06c2556cb8d

Returns the rotation of the current tool in degrees, where zero means the tip of the stylus is pointing towards the top of the tablet, a positive value means it's turned to the right, and a negative value means it's turned to the left. This can be given by a 4D Mouse or a rotation-capable stylus (such as the Wacom Art Pen or the Apple Pencil). If the device does not support rotation, this value is always 0.0.
