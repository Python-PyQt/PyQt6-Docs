.. sip:enum-description::
    :status: todo
    :digest: fb8d57431997e8b5ff5e9b79b82840d5

This enum selects the supported feature set when reading or writing Markdown.

Specifically, the supported subset of the GitHub dialect includes everything from CommonMark, plus:

* recognizing URLs, www and email addresses and turning them into links

* strikethrough

* underline (distinct from italics; in CommonMark it's the same)

* tables

* task lists

* :sip:ref:`~PyQt6.QtGui.QTextDocument.metaInformation`

"Front matter" is often metadata in YAML format. Qt does not currently include a parser for that; but you may choose a third-party parser, call :sip:ref:`~PyQt6.QtGui.QTextDocument.metaInformation` to get the whole block, and invoke your own parser after Qt has parsed the Markdown file.

**Note:** The Markdown output from :sip:ref:`~PyQt6.QtGui.QTextDocument.toMarkdown` currently may include GitHub features even if you attempt to disable them by specifying another enum value. This may be fixed in a future version of Qt.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.toMarkdown`, :sip:ref:`~PyQt6.QtGui.QTextDocument.setMarkdown`.
