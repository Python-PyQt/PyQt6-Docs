.. sip:method-description::
    :status: todo
    :pysig: 635c6e02f27780b3e0a44f858e692831
    :realsig: (uchar,QPixelFormat::TypeInterpretation)
    :digest: 151ca9a74092150a5f4fb6ae5c2354ee

Constructor function for creating a Grayscale format. Monochrome formats can be described by passing 1 to *channelSize*. Its also possible to define very accurate grayscale formats using doubles to describe each pixel by passing 8 as *channelSize* and :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.FloatingPoint` as *typeInterpretation*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation`.
