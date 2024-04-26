:orphan:

.. sip:class:: PyQt6.QtQuick.QQuickTextDocument
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtQuick/QQuickTextDocument-c.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickTextDocument.Status
        :description: QtQuick/QQuickTextDocument-Status-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.Loaded
            :description: QtQuick/QQuickTextDocument-Status-Loaded-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.Loading
            :description: QtQuick/QQuickTextDocument-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.NonLocalFileError
            :description: QtQuick/QQuickTextDocument-Status-NonLocalFileError-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.Null
            :description: QtQuick/QQuickTextDocument-Status-Null-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.ReadError
            :description: QtQuick/QQuickTextDocument-Status-ReadError-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.Saved
            :description: QtQuick/QQuickTextDocument-Status-Saved-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.Saving
            :description: QtQuick/QQuickTextDocument-Status-Saving-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickTextDocument.Status.WriteError
            :description: QtQuick/QQuickTextDocument-Status-WriteError-v.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.__init__
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickItem`
        :description: QtQuick/QQuickTextDocument-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.errorString
        :returns:
            str
        :description: QtQuick/QQuickTextDocument-errorString-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.isModified
        :returns:
            bool
        :description: QtQuick/QQuickTextDocument-isModified-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.save
        :description: QtQuick/QQuickTextDocument-save-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.saveAs
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQuick/QQuickTextDocument-saveAs-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.setModified
        :args:
            bool
        :description: QtQuick/QQuickTextDocument-setModified-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQuick/QQuickTextDocument-setSource-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.setTextDocument
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtQuick/QQuickTextDocument-setTextDocument-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQuick/QQuickTextDocument-source-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.status
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickTextDocument.Status`
        :description: QtQuick/QQuickTextDocument-status-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickTextDocument.textDocument
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtQuick/QQuickTextDocument-textDocument-f.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickTextDocument.errorStringChanged
        :description: QtQuick/QQuickTextDocument-errorStringChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickTextDocument.modifiedChanged
        :description: QtQuick/QQuickTextDocument-modifiedChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickTextDocument.sourceChanged
        :description: QtQuick/QQuickTextDocument-sourceChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickTextDocument.statusChanged
        :description: QtQuick/QQuickTextDocument-statusChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickTextDocument.textDocumentChanged
        :description: QtQuick/QQuickTextDocument-textDocumentChanged-s.rst
