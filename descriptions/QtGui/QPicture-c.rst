.. sip:class-description::
    :status: todo
    :brief: Paint device that records and replays QPainter commands
    :digest: 6b210237d91ecbaa7b0e3b1516949ec4

The :sip:ref:`~PyQt6.QtGui.QPicture` class is a paint device that records and replays :sip:ref:`~PyQt6.QtGui.QPainter` commands.

A picture serializes painter commands to an IO device in a platform-independent format. They are sometimes referred to as meta-files.

Qt pictures use a proprietary binary format. Unlike native picture (meta-file) formats on many window systems, Qt pictures have no limitations regarding their contents. Everything that can be painted on a widget or pixmap (e.g., fonts, pixmaps, regions, transformed graphics, etc.) can also be stored in a picture.

:sip:ref:`~PyQt6.QtGui.QPicture` is resolution independent, i.e. a :sip:ref:`~PyQt6.QtGui.QPicture` can be displayed on different devices (for example svg, pdf, ps, printer and screen) looking the same. This is, for instance, needed for WYSIWYG print preview. :sip:ref:`~PyQt6.QtGui.QPicture` runs in the default system dpi, and scales the painter to match differences in resolution depending on the window system.

Example of how to record a picture:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-picture-picture.py
    :lines: 58-63

Note that the list of painter commands is reset on each call to the :sip:ref:`~PyQt6.QtGui.QPainter.begin` function.

Example of how to replay a picture:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-picture-picture.py
    :lines: 73-78

Pictures can also be drawn using :sip:ref:`~PyQt6.QtGui.QPicture.play`. Some basic data about a picture is available, for example, :sip:ref:`~PyQt6.QtGui.QPicture.size`, :sip:ref:`~PyQt6.QtGui.QPicture.isNull` and :sip:ref:`~PyQt6.QtGui.QPicture.boundingRect`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QMovie`.
