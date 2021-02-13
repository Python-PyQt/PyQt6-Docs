.. sip:class-description::
    :status: todo
    :brief: Allows you to include several custom widgets in one single library
    :digest: 61404d44084b5c908a842f2dd212ee4a

The :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetCollectionInterface` class allows you to include several custom widgets in one single library.

When implementing a custom widget plugin, you build it as a separate library. If you want to include several custom widget plugins in the same library, you must in addition subclass :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetCollectionInterface`.

:sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetCollectionInterface` contains one single function returning a list of the collection's :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` objects. For example, if you have several custom widgets ``CustomWidgetOne``, ``CustomWidgetTwo`` and ``CustomWidgetThree``, the class definition may look like this:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 235-255

In the class constructor you add the interfaces to your custom widgets to the list which you return in the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetCollectionInterface.customWidgets` function:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 260-271

Note that instead of exporting each custom widget plugin using the Q_PLUGIN_METADATA() macro, you export the entire collection. The Q_PLUGIN_METADATA() macro ensures that *Qt Designer* can access and construct the custom widgets. Without this macro, there is no way for *Qt Designer* to use them.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface`, `Creating Custom Widgets for Qt Designer <https://doc.qt.io/qt-6/designer-creating-custom-widgets.html>`_.
