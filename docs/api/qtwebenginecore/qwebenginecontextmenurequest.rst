:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWebEngineCore/QWebEngineContextMenuRequest-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanCopy
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanCopy-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanCut
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanCut-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanDelete
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanDelete-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanEditRichly
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanEditRichly-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanPaste
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanPaste-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanRedo
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanRedo-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanSelectAll
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanSelectAll-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanTranslate
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanTranslate-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag.CanUndo
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-EditFlag-CanUndo-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaCanPrint
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaCanPrint-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaCanRotate
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaCanRotate-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaCanSave
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaCanSave-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaCanToggleControls
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaCanToggleControls-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaControls
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaControls-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaHasAudio
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaHasAudio-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaInError
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaInError-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaLoop
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaLoop-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaMuted
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaMuted-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag.MediaPaused
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaFlag-MediaPaused-v.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypeAudio
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypeAudio-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypeCanvas
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypeCanvas-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypeFile
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypeFile-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypeImage
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypeImage-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypeNone
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypeNone-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypePlugin
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypePlugin-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType.MediaTypeVideo
            :description: QtWebEngineCore/QWebEngineContextMenuRequest-MediaType-MediaTypeVideo-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.editFlags
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.EditFlag`
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-editFlags-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.isAccepted
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-isAccepted-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.isContentEditable
        :returns:
            bool
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-isContentEditable-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.linkText
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-linkText-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.linkUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-linkUrl-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.mediaFlags
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaFlag`
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-mediaFlags-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.mediaType
        :returns:
            :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.MediaType`
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-mediaType-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.mediaUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-mediaUrl-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.misspelledWord
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-misspelledWord-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.position
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-position-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.selectedText
        :returns:
            str
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-selectedText-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.setAccepted
        :args:
            bool
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-setAccepted-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineContextMenuRequest.spellCheckerSuggestions
        :returns:
            List[str]
        :description: QtWebEngineCore/QWebEngineContextMenuRequest-spellCheckerSuggestions-f.rst
