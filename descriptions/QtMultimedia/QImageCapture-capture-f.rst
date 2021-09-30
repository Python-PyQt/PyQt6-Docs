.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: 08d1d2c0bfae557c75bc0a6ef9f7bf71

Capture the image and make it available as a :sip:ref:`~PyQt6.QtGui.QImage`. This operation is asynchronous in majority of cases, followed by signals :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageExposed`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured` or :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.error`.

returns the capture Id parameter, used with :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageExposed`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured` and :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageSaved` signals.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.isReadyForCapture`.
