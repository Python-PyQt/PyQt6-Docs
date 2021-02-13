.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: b070cef9ede72078885ebd41c9fd781f

The image description. Some image formats, such as GIF and PNG, allow embedding of text or comments into the image data (e.g., for storing copyright information). It's common that the text is stored in key-value pairs, but some formats store all text in one continuous block. :sip:ref:`~PyQt6.QtGui.QImageIOHandler` returns the text as one QString, where keys and values are separated by a ':', and keys-value pairs are separated by two newlines (\\n\\n). For example, "Title: Sunset\\n\\nAuthor: Jim Smith\\nSarah Jones\\n\\n". Formats that store text in a single block can use "Description" as the key.
