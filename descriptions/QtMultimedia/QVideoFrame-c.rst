.. sip:class-description::
    :status: todo
    :brief: Represents a frame of video data
    :digest: db81a776879aef44ad510422a730fb46

The :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` class represents a frame of video data.

A :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` encapsulates the pixel data of a video frame, and information about the frame.

Video frames can come from several places - decoded :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, a :sip:ref:`~PyQt6.QtMultimedia.QCamera`, or generated programmatically. The way pixels are described in these frames can vary greatly, and some pixel formats offer greater compression opportunities at the expense of ease of use.

The pixel contents of a video frame can be mapped to memory using the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map` function. After a successful call to :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map`, the video data can be accessed through various functions. Some of the YUV pixel formats provide the data in several planes. The :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.planeCount` method will return the amount of planes that being used.

While mapped, the video data of each plane can accessed using the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.bits` function, which returns a pointer to a buffer. The size of this buffer is given by the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mappedBytes` function, and the size of each line is given by :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.bytesPerLine`. The return value of the handle() function may also be used to access frame data using the internal buffer's native APIs (for example - an OpenGL texture handle).

A video frame can also have timestamp information associated with it. These timestamps can be used to determine when to start and stop displaying the frame.

:sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` objects can consume a significant amount of memory or system resources and should not be held for longer than required by the application.

**Note:** Since video frames can be expensive to copy, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` is explicitly shared, so any change made to a video frame will also apply to any copies.
