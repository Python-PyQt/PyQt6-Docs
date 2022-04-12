:orphan:

.. sip:class:: PyQt6.QtWidgets.QFontComboBox
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QComboBox`
    :description: QtWidgets/QFontComboBox-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QFontComboBox.FontFilter
        :description: QtWidgets/QFontComboBox-FontFilter-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontComboBox.FontFilter.AllFonts
            :description: QtWidgets/QFontComboBox-FontFilter-AllFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontComboBox.FontFilter.MonospacedFonts
            :description: QtWidgets/QFontComboBox-FontFilter-MonospacedFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontComboBox.FontFilter.NonScalableFonts
            :description: QtWidgets/QFontComboBox-FontFilter-NonScalableFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontComboBox.FontFilter.ProportionalFonts
            :description: QtWidgets/QFontComboBox-FontFilter-ProportionalFonts-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFontComboBox.FontFilter.ScalableFonts
            :description: QtWidgets/QFontComboBox-FontFilter-ScalableFonts-v.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QFontComboBox-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.currentFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontComboBox-currentFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.displayFont
        :args:
            str
        :returns:
            Optional[:sip:ref:`~PyQt6.QtGui.QFont`]
        :description: QtWidgets/QFontComboBox-displayFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QFontComboBox-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.fontFilters
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFontComboBox.FontFilter`
        :description: QtWidgets/QFontComboBox-fontFilters-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.sampleTextForFont
        :args:
            str
        :returns:
            str
        :description: QtWidgets/QFontComboBox-sampleTextForFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.sampleTextForSystem
        :args:
            :sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem`
        :returns:
            str
        :description: QtWidgets/QFontComboBox-sampleTextForSystem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.setCurrentFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontComboBox-setCurrentFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.setDisplayFont
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontComboBox-setDisplayFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.setFontFilters
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFontComboBox.FontFilter`
        :description: QtWidgets/QFontComboBox-setFontFilters-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.setSampleTextForFont
        :args:
            str
            str
        :description: QtWidgets/QFontComboBox-setSampleTextForFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.setSampleTextForSystem
        :args:
            :sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem`
            str
        :description: QtWidgets/QFontComboBox-setSampleTextForSystem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.setWritingSystem
        :args:
            :sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem`
        :description: QtWidgets/QFontComboBox-setWritingSystem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QFontComboBox-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFontComboBox.writingSystem
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFontDatabase.WritingSystem`
        :description: QtWidgets/QFontComboBox-writingSystem-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QFontComboBox.currentFontChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QFontComboBox-currentFontChanged-s.rst
