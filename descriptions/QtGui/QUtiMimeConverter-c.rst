.. sip:class-description::
    :status: todo
    :brief: Converts between a MIME type and a Uniform Type Identifier (UTI) format
    :digest: 980f8ba12e17a6a993aa957d580df4d6

The :sip:ref:`~PyQt6.QtGui.QUtiMimeConverter` class converts between a MIME type and a `Uniform Type Identifier (UTI) <https://developer.apple.com/documentation/uniformtypeidentifiers>`_ format.

Qt's drag and drop and clipboard facilities use the MIME standard. On X11, this maps trivially to the Xdnd protocol. On Mac, although some applications use MIME to describe clipboard contents, it is more common to use Apple's UTI format.

:sip:ref:`~PyQt6.QtGui.QUtiMimeConverter`'s role is to bridge the gap between MIME and UTI; By subclasses this class, one can extend Qt's drag and drop and clipboard handling to convert to and from unsupported, or proprietary, UTI formats.

Construct an instance of your converter implementation after instantiating :sip:ref:`~PyQt6.QtGui.QGuiApplication`:

::

    int main(int argc, char **argv)
    {
        QGuiApplication app(argc, argv);
        JsonMimeConverter jsonConverter;
    }

Destroying the instance will unregister the converter and remove support for the conversion. It is also valid to heap-allocate the converter instance; Qt takes ownership and will delete the converter object during :sip:ref:`~PyQt6.QtGui.QGuiApplication` shut-down.

Qt has predefined support for the following UTIs:

* public.utf8-plain-text - converts to "text/plain"

* public.utf16-plain-text - converts to "text/plain"

* public.text - converts to "text/plain"

* public.html - converts to "text/html"

* public.url - converts to "text/uri-list"

* public.file-url - converts to "text/uri-list"

* public.tiff - converts to "application/x-qt-image"

* public.vcard - converts to "text/plain"

* com.apple.traditional-mac-plain-text - converts to "text/plain"

* com.apple.pict - converts to "application/x-qt-image"

When working with MIME data, Qt will iterate through all instances of :sip:ref:`~PyQt6.QtGui.QUtiMimeConverter` to find find an instance that can convert to, or from, a specific MIME type. It will do this by calling mimeForUti() or utiForMime() on each instance, starting with (and choosing) the last created instance first. The actual conversions will be done by using convertToMime() and convertFromMime().
