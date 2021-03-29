.. sip:class-description::
    :status: todo
    :brief: Information about the fonts available in the underlying window system
    :digest: 16e7f7d513253512c257fdf8b60d1187

The `QFontDatabase <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfontdatabase>`_ class provides information about the fonts available in the underlying window system.

The most common uses of this class are to query the database for the list of font :sip:ref:`~PyQt6.QtGui.QFontDatabase.families` and for the :sip:ref:`~PyQt6.QtGui.QFontDatabase.pointSizes` and :sip:ref:`~PyQt6.QtGui.QFontDatabase.styles` that are available for each family. An alternative to :sip:ref:`~PyQt6.QtGui.QFontDatabase.pointSizes` is :sip:ref:`~PyQt6.QtGui.QFontDatabase.smoothSizes` which returns the sizes at which a given family and style will look attractive.

If the font family is available from two or more foundries the foundry name is included in the family name; for example: "Helvetica [Adobe]" and "Helvetica [Cronyx]". When you specify a family, you can either use the old hyphenated "foundry-family" format or the bracketed "family [foundry]" format; for example: "Cronyx-Helvetica" or "Helvetica [Cronyx]". If the family has a foundry it is always returned using the bracketed format, as is the case with the value returned by :sip:ref:`~PyQt6.QtGui.QFontDatabase.families`.

The :sip:ref:`~PyQt6.QtGui.QFontDatabase.font` function returns a `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ given a family, style and point size.

A family and style combination can be checked to see if it is :sip:ref:`~PyQt6.QtGui.QFontDatabase.italic` or :sip:ref:`~PyQt6.QtGui.QFontDatabase.bold`, and to retrieve its :sip:ref:`~PyQt6.QtGui.QFontDatabase.weight`. Similarly we can call :sip:ref:`~PyQt6.QtGui.QFontDatabase.isBitmapScalable`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.isSmoothlyScalable`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.isScalable` and :sip:ref:`~PyQt6.QtGui.QFontDatabase.isFixedPitch`.

Use the :sip:ref:`~PyQt6.QtGui.QFontDatabase.styleString` to obtain a text version of a style.

The `QFontDatabase <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfontdatabase>`_ class provides some helper functions, for example, :sip:ref:`~PyQt6.QtGui.QFontDatabase.standardSizes`. You can retrieve the description of a writing system using :sip:ref:`~PyQt6.QtGui.QFontDatabase.writingSystemName`, and a sample of characters in a writing system with :sip:ref:`~PyQt6.QtGui.QFontDatabase.writingSystemSample`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-qfontdatabase-qfontdatabase_snippets.py
    :lines: 59-80

This example gets the list of font families, the list of styles for each family, and the point sizes that are available for each combination of family and style, displaying this information in a tree view.

.. seealso:: `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_, :sip:ref:`~PyQt6.QtGui.QFontInfo`, :sip:ref:`~PyQt6.QtGui.QFontMetrics`, `Character Map Example <https://doc.qt.io/qt-6/qtwidgets-widgets-charactermap-example.html>`_.
