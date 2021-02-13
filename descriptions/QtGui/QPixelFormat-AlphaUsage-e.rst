.. sip:enum-description::
    :status: todo
    :digest: 7253fef24a6996fab52337c31732a7be

This enum describes if the alpha channel is used or not. Sometimes the pixelformat will have a size for the alpha channel, but the pixel format does actually not use the alpha channel. For example RGB32 is such a format. The RGB channels are 8 bits each, and there is no alpha channel. But the complete size for each pixel is 32. Therefore the alpha channel size is 8, but the alpha channel is ignored. Its important to note that in such situations the position of the alpha channel is significant.
