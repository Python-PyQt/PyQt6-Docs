:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineCore/QWebEngineDownloadRequest-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason
        :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileAccessDenied
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileAccessDenied-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileBlocked
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileBlocked-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileFailed
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileFailed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileHashMismatch
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileHashMismatch-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileNameTooLong
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileNameTooLong-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileNoSpace
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileNoSpace-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileSecurityCheckFailed
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileSecurityCheckFailed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileTooLarge
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileTooLarge-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileTooShort
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileTooShort-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileTransientError
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileTransientError-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.FileVirusInfected
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-FileVirusInfected-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.NetworkDisconnected
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-NetworkDisconnected-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.NetworkFailed
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-NetworkFailed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.NetworkInvalidRequest
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-NetworkInvalidRequest-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.NetworkServerDown
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-NetworkServerDown-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.NetworkTimeout
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-NetworkTimeout-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.NoReason
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-NoReason-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.ServerBadContent
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-ServerBadContent-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.ServerCertProblem
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-ServerCertProblem-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.ServerFailed
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-ServerFailed-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.ServerForbidden
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-ServerForbidden-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.ServerUnauthorized
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-ServerUnauthorized-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.ServerUnreachable
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-ServerUnreachable-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason.UserCanceled
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadInterruptReason-UserCanceled-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState
        :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadState-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadCancelled
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadState-DownloadCancelled-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadCompleted
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadState-DownloadCompleted-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInProgress
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadState-DownloadInProgress-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadInterrupted
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadState-DownloadInterrupted-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState.DownloadRequested
            :description: QtWebEngineCore/QWebEngineDownloadRequest-DownloadState-DownloadRequested-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat
        :description: QtWebEngineCore/QWebEngineDownloadRequest-SavePageFormat-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat.CompleteHtmlSaveFormat
            :description: QtWebEngineCore/QWebEngineDownloadRequest-SavePageFormat-CompleteHtmlSaveFormat-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat.MimeHtmlSaveFormat
            :description: QtWebEngineCore/QWebEngineDownloadRequest-SavePageFormat-MimeHtmlSaveFormat-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat.SingleHtmlSaveFormat
            :description: QtWebEngineCore/QWebEngineDownloadRequest-SavePageFormat-SingleHtmlSaveFormat-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat.UnknownSaveFormat
            :description: QtWebEngineCore/QWebEngineDownloadRequest-SavePageFormat-UnknownSaveFormat-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.accept
        :description: QtWebEngineCore/QWebEngineDownloadRequest-accept-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.cancel
        :description: QtWebEngineCore/QWebEngineDownloadRequest-cancel-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadDirectory
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-downloadDirectory-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadFileName
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-downloadFileName-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.id
        :returns:
            int
        :description: QtWebEngineCore/QWebEngineDownloadRequest-id-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.interruptReason
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadInterruptReason`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-interruptReason-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.interruptReasonString
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-interruptReasonString-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isFinished
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineDownloadRequest-isFinished-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isPaused
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineDownloadRequest-isPaused-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isSavePageDownload
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineDownloadRequest-isSavePageDownload-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.mimeType
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-mimeType-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.page
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-page-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.pause
        :description: QtWebEngineCore/QWebEngineDownloadRequest-pause-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.receivedBytes
        :returns:
            int
        :description: QtWebEngineCore/QWebEngineDownloadRequest-receivedBytes-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.resume
        :description: QtWebEngineCore/QWebEngineDownloadRequest-resume-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.savePageFormat
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-savePageFormat-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.setDownloadDirectory
        :args:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-setDownloadDirectory-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.setDownloadFileName
        :args:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-setDownloadFileName-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.setSavePageFormat
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.SavePageFormat`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-setSavePageFormat-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.state
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-state-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.suggestedFileName
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineDownloadRequest-suggestedFileName-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.totalBytes
        :returns:
            int
        :description: QtWebEngineCore/QWebEngineDownloadRequest-totalBytes-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.url
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-url-f.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadDirectoryChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-downloadDirectoryChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.downloadFileNameChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-downloadFileNameChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.interruptReasonChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-interruptReasonChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isFinishedChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-isFinishedChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.isPausedChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-isPausedChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.receivedBytesChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-receivedBytesChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.savePageFormatChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-savePageFormatChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.DownloadState`
        :description: QtWebEngineCore/QWebEngineDownloadRequest-stateChanged-s.rst

    .. sip:signal:: PyQt6.QtWebEngineCore.QWebEngineDownloadRequest.totalBytesChanged
        :description: QtWebEngineCore/QWebEngineDownloadRequest-totalBytesChanged-s.rst
