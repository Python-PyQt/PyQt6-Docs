.. sip:class-description::
    :status: todo
    :brief: Gives information about and control over a page frame
    :digest: f42bb47bed665f3baa8fb2f90d241a9c

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFrame` class gives information about and control over a page frame.

A web engine frame represents a single frame within a web page, such as those created by ``<frame>`` or ``<iframe>`` HTML elements. An active :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` has one or more frames arranged in a tree structure. The top-level frame, the root of this tree, can be accessed through the mainFrame() method, and :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFrame.children` provides a frame's direct descendants.

A frame's lifetime is, at most, as long as the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` object that produced it. However, frames may be created and deleted spontaneously and dynamically, for example through navigation and script execution. Because of this, many :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFrame` methods return optional values, which will be ``std::nullopt`` if the frame no longer exists.
