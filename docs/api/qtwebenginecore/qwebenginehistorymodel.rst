:orphan:

.. sip:class:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractListModel`
    :description: QtWebEngineCore/QWebEngineHistoryModel-c.rst

    .. sip:enum:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.Roles
        :description: QtWebEngineCore/QWebEngineHistoryModel-Roles-e.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.Roles.IconUrlRole
            :description: QtWebEngineCore/QWebEngineHistoryModel-Roles-IconUrlRole-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.Roles.OffsetRole
            :description: QtWebEngineCore/QWebEngineHistoryModel-Roles-OffsetRole-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.Roles.TitleRole
            :description: QtWebEngineCore/QWebEngineHistoryModel-Roles-TitleRole-v.rst

        .. sip:enum-member:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.Roles.UrlRole
            :description: QtWebEngineCore/QWebEngineHistoryModel-Roles-UrlRole-v.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtWebEngineCore/QWebEngineHistoryModel-data-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.reset
        :description: QtWebEngineCore/QWebEngineHistoryModel-reset-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtWebEngineCore/QWebEngineHistoryModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtWebEngineCore.QWebEngineHistoryModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtWebEngineCore/QWebEngineHistoryModel-rowCount-f.rst
