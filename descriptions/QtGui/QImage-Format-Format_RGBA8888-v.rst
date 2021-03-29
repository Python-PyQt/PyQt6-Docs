.. sip:enum-member-description::
    :status: todo
    :value: 17
    :digest: ad9303ab6332091fa606e39ac00cacad

The image is stored using a 32-bit byte-ordered RGBA format (8-8-8-8). Unlike ARGB32 this is a byte-ordered format, which means the 32bit encoding differs between big endian and little endian architectures, being respectively (0xRRGGBBAA) and (0xAABBGGRR). The order of the colors is the same on any architecture if read as bytes 0xRR,0xGG,0xBB,0xAA. (added in Qt 5.2)
