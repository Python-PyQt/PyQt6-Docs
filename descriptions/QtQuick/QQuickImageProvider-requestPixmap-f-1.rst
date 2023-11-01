.. sip:method-description::
    :status: todo
    :pysig: 1348008262067cfa72a73b854494e36b
    :realsig: (const QString&, QSize*, const QSize&)
    :digest: 2ada87163bb06b75ae8d9defbe882cec

Implement this method to return the pixmap with *id*. The default implementation returns an empty pixmap.

The *id* is the requested image source, with the "image:" scheme and provider identifier removed. For example, if the image `source <https://doc.qt.io/qt-6/qml-qtquick-image.html#source-prop>`_ was "image://myprovider/icons/home", the given *id* would be "icons/home".

The *requestedSize* corresponds to the `Image::sourceSize <https://doc.qt.io/qt-6/qml-qtquick-image.html#sourceSize-prop>`_ requested by an Image item. If *requestedSize* is a valid size, the image returned should be of that size.

In all cases, *size* must be set to the original size of the image. This is used to set the `width <https://doc.qt.io/qt-6/qml-qtquick-item.html#width-prop>`_ and `height <https://doc.qt.io/qt-6/qml-qtquick-item.html#height-prop>`_ of the relevant :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase.ImageType.Image` if these values have not been set explicitly.

**Note:** this method may be called by multiple threads, so ensure the implementation of this method is reentrant.
