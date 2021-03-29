.. sip:class-description::
    :status: todo
    :brief: Handle functionality for the splitter
    :digest: 3b78ce47c4b1a985cf5209e704a003fc

The :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle` class provides handle functionality for the splitter.

:sip:ref:`~PyQt6.QtWidgets.QSplitterHandle` is typically what people think about when they think about a splitter. It is the handle that is used to resize the widgets.

A typical developer using :sip:ref:`~PyQt6.QtWidgets.QSplitter` will never have to worry about :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle`. It is provided for developers who want splitter handles that provide extra features, such as popup menus.

The typical way one would create splitter handles is to subclass :sip:ref:`~PyQt6.QtWidgets.QSplitter` and then reimplement :sip:ref:`~PyQt6.QtWidgets.QSplitter.createHandle` to instantiate the custom splitter handle. For example, a minimum :sip:ref:`~PyQt6.QtWidgets.QSplitter` subclass might look like this:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-splitterhandle-splitter.py
    :lines: 63-70

The :sip:ref:`~PyQt6.QtWidgets.QSplitter.createHandle` implementation simply constructs a custom splitter handle, called ``Splitter`` in this example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-splitterhandle-splitter.py

Information about a given handle can be obtained using functions like :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle.orientation` and :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle.opaqueResize`, and is retrieved from its parent splitter. Details like these can be used to give custom handles different appearances depending on the splitter's orientation.

The complexity of a custom handle subclass depends on the tasks that it needs to perform. A simple subclass might only provide a :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle.paintEvent` implementation:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-splitterhandle-splitter.py
    :lines: 63-70

In this example, a predefined gradient is set up differently depending on the orientation of the handle. :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle` provides a reasonable size hint for the handle, so the subclass does not need to provide a reimplementation of :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle.sizeHint` unless the handle has special size requirements.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter`.
