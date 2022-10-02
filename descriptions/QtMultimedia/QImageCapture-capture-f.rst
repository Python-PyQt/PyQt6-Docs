.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: eec81d9fc05031b8540c856bccc66791

Capture the image and make it available as a :sip:ref:`~PyQt6.QtGui.QImage`. This operation is asynchronous in majority of cases, followed by signals :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageExposed`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured` or :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.error`.

QImageCapture::capture returns the capture Id parameter, used with :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageExposed`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured` and :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageSaved` signals.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.isReadyForCapture`.
