.. sip:enum-description::
    :status: todo
    :digest: 6eb7e898349525b05e1c49695d371054

This enum describes the mode the printer should work in. It basically presets a certain resolution and working mode.

**Note:** When rendering text on a :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` device, it is important to realize that the size of text, when specified in points, is independent of the resolution specified for the device itself. Therefore, it may be useful to specify the font size in pixels when combining text with graphics to ensure that their relative sizes are what you expect.
