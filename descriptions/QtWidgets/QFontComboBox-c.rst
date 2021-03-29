.. sip:class-description::
    :status: todo
    :brief: Combobox that lets the user select a font family
    :digest: f0989819b525aa9d3a0b5765d3a16567

The :sip:ref:`~PyQt6.QtWidgets.QFontComboBox` widget is a combobox that lets the user select a font family.

The combobox is populated with an alphabetized list of font family names, such as Arial, Helvetica, and Times New Roman. Family names are displayed using the actual font when possible. For fonts such as Symbol, where the name is not representable in the font itself, a sample of the font is displayed next to the family name.

:sip:ref:`~PyQt6.QtWidgets.QFontComboBox` is often used in toolbars, in conjunction with a `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_ for controlling the font size and two :sip:ref:`~PyQt6.QtWidgets.QToolButton`\ s for bold and italic.

When the user selects a new font, the :sip:ref:`~PyQt6.QtWidgets.QFontComboBox.currentFontChanged` signal is emitted in addition to currentIndexChanged().

Call :sip:ref:`~PyQt6.QtWidgets.QFontComboBox.setWritingSystem` to tell :sip:ref:`~PyQt6.QtWidgets.QFontComboBox` to show only fonts that support a given writing system, and :sip:ref:`~PyQt6.QtWidgets.QFontComboBox.setFontFilters` to filter out certain types of fonts as e.g. non scalable fonts or monospaced fonts.

.. image:: ../../../images/windowsvista-fontcombobox.png

.. seealso:: `QComboBox <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qcombobox>`_, `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_, :sip:ref:`~PyQt6.QtGui.QFontInfo`, :sip:ref:`~PyQt6.QtGui.QFontMetrics`, `QFontDatabase <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfontdatabase>`_, `Character Map Example <https://doc.qt.io/qt-6/qtwidgets-widgets-charactermap-example.html>`_.
