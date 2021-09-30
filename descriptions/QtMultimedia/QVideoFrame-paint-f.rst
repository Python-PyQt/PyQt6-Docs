.. sip:method-description::
    :status: todo
    :pysig: 10fd38a5f94d7419eaa2d5edbccc7abc
    :realsig: (QPainter*,const QRectF&,const QVideoFrame::PaintOptions&)
    :digest: 5161ac4eb2d17ff2d0e04372d372ae2a

Uses a :sip:ref:`~PyQt6.QtGui.QPainter`, *painter*, to render this :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` to *rect*. The PaintOptions *options* can be used to specify a background color and how *rect* should be filled with the video.

**Note:** that rendering will usually happen without hardware acceleration when using this method.
