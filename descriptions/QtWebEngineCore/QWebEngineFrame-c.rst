.. sip:class-description::
    :status: todo
    :brief: Gives information about and control over a page frame
    :digest: 119c91a6052fc0136d913f33782cefd0

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFrame` class gives information about and control over a page frame.

A web engine frame represents a single frame within a web page, such as those created by ``<frame>`` or ``<iframe>`` HTML elements. An active :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` has one or more frames arranged in a tree structure. The top-level frame, the root of this tree, can be accessed through the mainFrame() method, and children() provides a frame's direct descendants.

A frame's lifetime is, at most, as long as the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` object that produced it. However, frames may be created and deleted spontaneously and dynamically, for example through navigation and script execution. Because of this, many :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFrame` methods return optional values, which will be ``std::nullopt`` if the frame no longer exists.
