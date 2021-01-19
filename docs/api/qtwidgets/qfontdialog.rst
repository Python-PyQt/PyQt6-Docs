:orphan:

.. sip:class:: PyQt6.QtWidgets.QFontDialog
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QDialog`
    :description: QtWidgets/QFontDialog-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions
        :description: QtWidgets/QFontDialog-FontDialogOptions-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions.DontUseNativeDialog
            :description: QtWidgets/QFontDialog-FontDialogOptions-DontUseNativeDialog-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions.MonospacedFonts
            :description: QtWidgets/QFontDialog-FontDialogOptions-MonospacedFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions.NoButtons
            :description: QtWidgets/QFontDialog-FontDialogOptions-NoButtons-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions.NonScalableFonts
            :description: QtWidgets/QFontDialog-FontDialogOptions-NonScalableFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions.ProportionalFonts
            :description: QtWidgets/QFontDialog-FontDialogOptions-ProportionalFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontDialog.FontDialogOptions.ScalableFonts
            :description: QtWidgets/QFontDialog-FontDialogOptions-ScalableFonts-v.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QFontDialog-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QFontDialog-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QFontDialog-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.currentFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontDialog-currentFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.done
        :args:
            int
        :description: QtWidgets/QFontDialog-done-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QFontDialog-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.getFont
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
            bool
        :static:
        :description: QtWidgets/QFontDialog-getFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.getFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFontDialog.FontDialogOptions` = QFontDialog.FontDialogOptions()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
            bool
        :static:
        :description: QtWidgets/QFontDialog-getFont-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.open
        :description: QtWidgets/QFontDialog-open-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.open
        :args:
            PYQT_SLOT
        :description: QtWidgets/QFontDialog-open-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.options
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFontDialog.FontDialogOptions`
        :description: QtWidgets/QFontDialog-options-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.selectedFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontDialog-selectedFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.setCurrentFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontDialog-setCurrentFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.setOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFontDialog.FontDialogOptions`
            on: bool = True
        :description: QtWidgets/QFontDialog-setOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.setOptions
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFontDialog.FontDialogOptions`
        :description: QtWidgets/QFontDialog-setOptions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.setVisible
        :args:
            bool
        :description: QtWidgets/QFontDialog-setVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontDialog.testOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFontDialog.FontDialogOptions`
        :returns:
            bool
        :description: QtWidgets/QFontDialog-testOption-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QFontDialog.currentFontChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontDialog-currentFontChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFontDialog.fontSelected
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontDialog-fontSelected-s.rst
