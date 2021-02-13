.. sip:enum-description::
    :status: todo
    :digest: 7af10642cf7a07a3af50e68868c07473

.. image:: ../../../images/palette.png

The  enum defines the different symbolic color roles used in current GUIs.

The central roles are:

There are some color roles used mostly for 3D bevel and shadow effects. All of these are normally derived from ``Window``, and used in ways that depend on that relationship. For example, buttons depend on it to make the bevels look attractive, and Motif scroll bars depend on ``Mid`` to be slightly different from ``Window``.

Selected (marked) items have two roles:

There are two color roles related to hyperlinks:

Note that we do not use the ``Link`` and ``LinkVisited`` roles when rendering rich text in Qt, and that we recommend that you use CSS and the :sip:ref:`~PyQt6.QtGui.QTextDocument.setDefaultStyleSheet` function to alter the appearance of links. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-css-main.py
    :lines: 60-63
