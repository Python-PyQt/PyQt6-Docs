:orphan:

.. sip:class:: PyQt6.QtWidgets.QDialog
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QDialog-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QDialog.DialogCode
        :description: QtWidgets/QDialog-DialogCode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDialog.DialogCode.Accepted
            :description: QtWidgets/QDialog-DialogCode-Accepted-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDialog.DialogCode.Rejected
            :description: QtWidgets/QDialog-DialogCode-Rejected-v.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags` = Qt.WindowFlags()
        :description: QtWidgets/QDialog-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.accept
        :description: QtWidgets/QDialog-accept-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.closeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QCloseEvent`
        :description: QtWidgets/QDialog-closeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QDialog-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.done
        :args:
            int
        :description: QtWidgets/QDialog-done-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QDialog-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.exec
        :returns:
            int
        :description: QtWidgets/QDialog-exec-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.isSizeGripEnabled
        :returns:
            bool
        :description: QtWidgets/QDialog-isSizeGripEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QDialog-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QDialog-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.open
        :description: QtWidgets/QDialog-open-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.reject
        :description: QtWidgets/QDialog-reject-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QDialog-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.result
        :returns:
            int
        :description: QtWidgets/QDialog-result-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.setModal
        :args:
            bool
        :description: QtWidgets/QDialog-setModal-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.setResult
        :args:
            int
        :description: QtWidgets/QDialog-setResult-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.setSizeGripEnabled
        :args:
            bool
        :description: QtWidgets/QDialog-setSizeGripEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.setVisible
        :args:
            bool
        :description: QtWidgets/QDialog-setVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QDialog-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDialog.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QDialog-sizeHint-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QDialog.accepted
        :description: QtWidgets/QDialog-accepted-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QDialog.finished
        :args:
            int
        :description: QtWidgets/QDialog-finished-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QDialog.rejected
        :description: QtWidgets/QDialog-rejected-s.rst
