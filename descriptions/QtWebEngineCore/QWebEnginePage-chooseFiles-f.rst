.. sip:method-description::
    :status: todo
    :pysig: f3541caa13986a68c37c6741530d85a7
    :realsig: (QWebEnginePage::FileSelectionMode,const QStringList&,const QStringList&)
    :digest: 5e9181abd96e2c7851ee4289c37f3531

This function is called when the web content requests a file name, for example as a result of the user clicking on a file upload button in an HTML form.

*mode* indicates whether only one file or multiple files are expected to be returned.

A suggested filename may be provided as the first entry of *oldFiles*. *acceptedMimeTypes* is ignored by the default implementation, but might be used by overrides.
