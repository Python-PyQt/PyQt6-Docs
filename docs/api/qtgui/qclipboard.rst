:orphan:

.. sip:class:: PyQt6.QtGui.QClipboard
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QClipboard-c.rst

    .. sip:enum:: PyQt6.QtGui.QClipboard.Mode
        :description: QtGui/QClipboard-Mode-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QClipboard.Mode.Clipboard
            :description: QtGui/QClipboard-Mode-Clipboard-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QClipboard.Mode.FindBuffer
            :description: QtGui/QClipboard-Mode-FindBuffer-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QClipboard.Mode.Selection
            :description: QtGui/QClipboard-Mode-Selection-v.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.clear
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :description: QtGui/QClipboard-clear-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.image
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGui/QClipboard-image-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.mimeData
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtGui/QClipboard-mimeData-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.ownsClipboard
        :returns:
            bool
        :description: QtGui/QClipboard-ownsClipboard-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.ownsFindBuffer
        :returns:
            bool
        :description: QtGui/QClipboard-ownsFindBuffer-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.ownsSelection
        :returns:
            bool
        :description: QtGui/QClipboard-ownsSelection-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.pixmap
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtGui/QClipboard-pixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.setImage
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :description: QtGui/QClipboard-setImage-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.setMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :description: QtGui/QClipboard-setMimeData-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.setPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :description: QtGui/QClipboard-setPixmap-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.setText
        :args:
            Optional[str]
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :description: QtGui/QClipboard-setText-f-1.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.supportsFindBuffer
        :returns:
            bool
        :description: QtGui/QClipboard-supportsFindBuffer-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.supportsSelection
        :returns:
            bool
        :description: QtGui/QClipboard-supportsSelection-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.text
        :args:
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :returns:
            str
        :description: QtGui/QClipboard-text-f.rst

    .. sip:method:: PyQt6.QtGui.QClipboard.text
        :args:
            Optional[str]
            mode: :sip:ref:`~PyQt6.QtGui.QClipboard.Mode` = :sip:ref:`~PyQt6.QtGui.QClipboard.Mode.Clipboard`
        :returns:
            Tuple[str, str]
        :description: QtGui/QClipboard-text-f-2.rst

    .. sip:signal:: PyQt6.QtGui.QClipboard.changed
        :args:
            :sip:ref:`~PyQt6.QtGui.QClipboard.Mode`
        :description: QtGui/QClipboard-changed-s.rst

    .. sip:signal:: PyQt6.QtGui.QClipboard.dataChanged
        :description: QtGui/QClipboard-dataChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QClipboard.findBufferChanged
        :description: QtGui/QClipboard-findBufferChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QClipboard.selectionChanged
        :description: QtGui/QClipboard-selectionChanged-s.rst
