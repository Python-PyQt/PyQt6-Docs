.. sip:class-description::
    :status: todo
    :brief: Interface for supporting pixmaps and threaded image requests in QML
    :digest: c56b4592633423b3cca595b1f179746f

The :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider` class provides an interface for supporting pixmaps and threaded image requests in QML.

:sip:ref:`~PyQt6.QtQuick.QQuickImageProvider` is used to provide advanced image loading features in QML applications. It allows images in QML to be:

* Loaded using QPixmaps rather than actual image files

* Loaded asynchronously in a separate thread

To specify that an image should be loaded by an image provider, use the **"image:"** scheme for the URL source of the image, followed by the identifiers of the image provider and the requested image. For example:

This specifies that the image should be loaded by the image provider named "myimageprovider", and the image to be loaded is named "image.png". The QML engine invokes the appropriate image provider according to the providers that have been registered through :sip:ref:`~PyQt6.QtQml.QQmlEngine.addImageProvider`.

Note that the identifiers are case-insensitive, but the rest of the URL will be passed on with preserved case. For example, the below snippet would still specify that the image is loaded by the image provider named "myimageprovider", but it would request a different image than the above snippet ("Image.png" instead of "image.png").

If you want the rest of the URL to be case insensitive, you will have to take care of that yourself inside your image provider.

.. _qquickimageprovider-an-example:

An Example
..........

Here are two images. Their ``source`` values indicate they should be loaded by an image provider named "colors", and the images to be loaded are "yellow" and "red", respectively:

.. literalinclude:: ../../../snippets/qtdeclarative-src-quick-doc-snippets-imgprovider-imageprovider-example.qml

When these images are loaded by QML, it looks for a matching image provider and calls its :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider.requestImage` or :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider.requestPixmap` method (depending on its :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider.imageType`) to load the image. The method is called with the ``id`` parameter set to "yellow" for the first image, and "red" for the second.

Here is an image provider implementation that can load the images requested by the above QML. This implementation dynamically generates :sip:ref:`~PyQt6.QtGui.QPixmap` images that are filled with the requested color:

.. literalinclude:: ../../../snippets/qtdeclarative-src-quick-doc-snippets-imgprovider-imageprovider.py

To make this provider accessible to QML, it is registered with the QML engine with a "colors" identifier:

.. literalinclude:: ../../../snippets/qtdeclarative-src-quick-doc-snippets-imgprovider-imageprovider.py

.. literalinclude:: ../../../snippets/qtdeclarative-src-quick-doc-snippets-imgprovider-imageprovider.py

Now the images can be successfully loaded in QML:

.. image:: ../../../images/imageprovider.png

See the `Image Provider Example <https://doc.qt.io/qt-6/qtquick-imageprovider-example.html>`_ for the complete implementation. Note that the example registers the provider via a :sip:ref:`~PyQt6.QtQml.QQmlEngineExtensionPlugin` instead of registering it in the application ``main()`` function as shown above.

It is possible to provide "@nx" high DPI syntax.

.. _qquickimageprovider-asynchronous-image-loading:

Asynchronous Image Loading
..........................

Image providers that support :sip:ref:`~PyQt6.QtGui.QImage` or Texture loading automatically include support for asychronous loading of images. To enable asynchronous loading for an image source, set the ``asynchronous`` property to ``true`` for the relevant :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase.ImageType.Image` or `BorderImage <https://doc.qt.io/qt-6/qml-qtquick-borderimage.html>`_ object. When this is enabled, the image request to the provider is run in a low priority thread, allowing image loading to be executed in the background, and reducing the performance impact on the user interface.

To force asynchronous image loading, even for image sources that do not have the ``asynchronous`` property set to ``true``, you may pass the ``QQmlImageProviderBase::ForceAsynchronousImageLoading`` flag to the image provider constructor. This ensures that all image requests for the provider are handled in a separate thread.

Asynchronous loading for image providers that provide :sip:ref:`~PyQt6.QtGui.QPixmap` is only supported in platforms that have the ThreadedPixmaps feature, in platforms where pixmaps can only be created in the main thread (i.e. ThreadedPixmaps is not supported) if `asynchronous <https://doc.qt.io/qt-6/qml-qtquick-image.html#asynchronous-prop>`_ is set to ``true``, the value is ignored and the image is loaded synchronously.

Asynchronous image loading for providers of type other than ImageResponse are executed on a single thread per engine basis. That means that a slow image provider will block the loading of any other request. To avoid that we suggest using :sip:ref:`~PyQt6.QtQuick.QQuickAsyncImageProvider` and implement threading on the provider side via a ``QThreadPool`` or similar. See the `Image Response Provider Example <https://doc.qt.io/qt-6/qtquick-imageresponseprovider-example.html>`_ for a complete implementation.

.. _qquickimageprovider-image-caching:

Image Caching
.............

Images returned by a :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider` are automatically cached, similar to any image loaded by the QML engine. When an image with a "image://" prefix is loaded from cache, :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider.requestImage` and :sip:ref:`~PyQt6.QtQuick.QQuickImageProvider.requestPixmap` will not be called for the relevant image provider. If an image should always be fetched from the image provider, and should not be cached at all, set the ``cache`` property to ``false`` for the relevant :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase.ImageType.Image` or `BorderImage <https://doc.qt.io/qt-6/qml-qtquick-borderimage.html>`_ object.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.addImageProvider`.
