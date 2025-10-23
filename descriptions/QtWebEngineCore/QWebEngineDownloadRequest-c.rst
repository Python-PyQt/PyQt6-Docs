.. sip:class-description::
    :status: todo
    :brief: Information about a download
    :digest: cdcc7686bd40632294a7c4f4e16754c9

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest` class provides information about a download.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest` models a download throughout its life cycle, starting with a pending download request and finishing with a completed download. It can be used, for example, to get information about new downloads, to monitor progress, and to pause, resume, and cancel downloads.

Downloads are usually triggered by user interaction on a web page. It is the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile`'s responsibility to notify the application of new download requests, which it does by emitting the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested` signal together with a newly created :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest`. The application can then examine this item and decide whether to accept it or not. When a decision is made, the application must explicitly call :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.accept` or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.cancel` on the item for Qt WebEngine to actually start downloading or rejecting the request.

**Note:** Some properties, such as setting the path and file name where the file will be saved (see :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadDirectory` and :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadFileName`), can only be changed before calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.accept`.

.. _qwebenginedownloadrequest-object-life-cycle:

Object Life Cycle
.................

In each and every case, the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` takes the ownership of the item. However, it is safe for the application to delete the item at any time, except during the handling of the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested` signal. The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile` being a long-lived object, it is in fact recommended that the application delete any items it is no longer interested in.

**Note:** Deleting an item will also automatically cancel a download since 5.12.2, but it is recommended to cancel manually before deleting for portability.

.. _qwebenginedownloadrequest-web-page-downloads:

Web Page Downloads
..................

In addition to normal file downloads, which consist simply of retrieving some raw bytes from the network and writing them to disk, Qt WebEngine also supports saving complete web pages, which involves parsing the page's HTML, downloading any dependent resources, and potentially packaging everything into a special file format (\ :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.savePageFormat`). To check if a download is for a file or a web page, use :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isSavePageDownload`.

Web page save requests are accepted automatically and started from :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInProgress` state by convenience reasons. The first directly connected :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested` signal handler can prevent this by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.cancel`, otherwise the save operation will start writing data to the disk.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.downloadRequested`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.download`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.save`.
