.. sip:method-description::
    :status: todo
    :pysig: 705bcd4afd27d378938e95437247bfbe
    :realsig: (const QUrl&,const QString&)
    :digest: e4906780b0f0da4101d37b8e2d04c1a8

Downloads the resource from the location given by *url* to a local file.

If *filename* is given, it is used as the suggested file name. If it is relative, the file is saved in the standard download location with the given name. If it is a null or empty QString, the default file name is used.

This will emit :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested` after the download has started.
