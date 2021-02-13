.. sip:method-description::
    :status: todo
    :pysig: 635c6e02f27780b3e0a44f858e692831
    :realsig: (uchar,QPixelFormat::TypeInterpretation)
    :digest: b5cc34793f8cee4b169d1d4d2c15286f

Constructor function for creating an Alpha format. A mask format can be described by passing 1 to *channelSize*. Its also possible to define very accurate alpha formats using doubles to describe each pixel by passing 8 as *channelSize* and :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.FloatingPoint` as *typeInterpretation*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation`.
