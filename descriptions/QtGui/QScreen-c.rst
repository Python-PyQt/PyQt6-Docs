.. sip:class-description::
    :status: todo
    :brief: Used to query screen properties
    :digest: 242a95834692e8f989605c06a038c472

The :sip:ref:`~PyQt6.QtGui.QScreen` class is used to query screen properties.

A note on logical vs physical dots per inch: physical DPI is based on the actual physical pixel sizes when available, and is useful for print preview and other cases where it's desirable to know the exact physical dimensions of screen displayed contents.

Logical dots per inch are used to convert font and user interface elements from point sizes to pixel sizes, and might be different from the physical dots per inch. The logical dots per inch are sometimes user-settable in the desktop environment's settings panel, to let the user globally control UI and font sizes in different applications.

**Note:** Both physical and logical DPI are expressed in device-independent dots. Multiply by :sip:ref:`~PyQt6.QtGui.QScreen.devicePixelRatio` to get device-dependent density.
