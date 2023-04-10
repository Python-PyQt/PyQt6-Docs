.. sip:class-description::
    :status: todo
    :brief: Converts between a MIME type and a Uniform Type Identifier (UTI) format
    :digest: d6777a10bfca33af6ebf27e5a6b10598

The :sip:ref:`~PyQt6.QtGui.QUtiMimeConverter` class converts between a MIME type and a `Uniform Type Identifier (UTI) <https://developer.apple.com/documentation/uniformtypeidentifiers>`_ format.

Qt's drag and drop and clipboard facilities use the MIME standard. On X11, this maps trivially to the Xdnd protocol. On Mac, although some applications use MIME to describe clipboard contents, it is more common to use Apple's UTI format.

:sip:ref:`~PyQt6.QtGui.QUtiMimeConverter`'s role is to bridge the gap between MIME and UTI; By subclasses this class, one can extend Qt's drag and drop and clipboard handling to convert to and from unsupported, or proprietary, UTI formats.

A subclass of :sip:ref:`~PyQt6.QtGui.QUtiMimeConverter` will automatically be registered, and active, upon instantiation.

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
