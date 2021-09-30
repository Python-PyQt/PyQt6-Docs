.. sip:class-description::
    :status: todo
    :brief: Specifies the stream format of a video presentation surface
    :digest: 8deb1244474adef5b5e2988497d18b51

The :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat` class specifies the stream format of a video presentation surface.

A video sink presents a stream of video frames. :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat` describes the type of the frames and determines how they should be presented.

The core properties of a video stream required to setup a video sink are the pixel format given by :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.pixelFormat`, and the frame dimensions given by :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.frameSize`.

The region of a frame that is actually displayed on a video surface is given by the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.viewport`. A stream may have a viewport less than the entire region of a frame to allow for videos smaller than the nearest optimal size of a video frame. For example the width of a frame may be extended so that the start of each scan line is eight byte aligned.

Other common properties are the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.scanLineDirection`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.frameRate` and the yCrCbColorSpace().
