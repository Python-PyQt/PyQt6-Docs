.. sip:class-description::
    :status: todo
    :brief: Enables accepting or rejecting requests for local file system access from JavaScript applications
    :digest: 7041878950860079fcf48360d5bd7bbd

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFileSystemAccessRequest` class enables accepting or rejecting requests for local file system access from JavaScript applications.

To allow web applications to access local files of the computer, applications must connect to QWebEnginePage::fileSystemAccessRequested, which takes a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFileSystemAccessRequest` instance as an argument.

If a web applications requests access to local files or directories, QWebEnginePage::fileSystemAccessRequested will be emitted with an :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFileSystemAccessRequest` instance as an argument where :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFileSystemAccessRequest.accessFlags` indicates the type of the requested access: read, write or both. The signal handler needs to then either call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFileSystemAccessRequest.accept` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFileSystemAccessRequest.reject`.
