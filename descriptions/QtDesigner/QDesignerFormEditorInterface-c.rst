.. sip:class-description::
    :status: todo
    :brief: Allows you to access Qt Widgets Designer's various components
    :digest: 62a3238ecb9842676f1863bca3d3a409

The :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` class allows you to access Qt Widgets Designer's various components.

Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object holds information about all Qt Widgets Designer's components: The action editor, the object inspector, the property editor, the widget box, and the extension and form window managers. :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` contains a collection of functions that provides interfaces to all these components. They are typically used to query (and manipulate) the respective component. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractobjectinspector.py
    :lines: 54-60

:sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` is not intended to be instantiated directly. A pointer to Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. When implementing a custom widget plugin, you must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your plugin to Qt Widgets Designer.

:sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` also provides functions that can set the action editor, property editor, object inspector and widget box. These are only useful if you want to provide your own custom components.

If designer is embedded in another program, one could to provide its own settings manager. The manager is used by the components of Qt Widgets Designer to store/retrieve persistent configuration settings. The default manager uses :sip:ref:`~PyQt6.QtCore.QSettings` as the backend.

Finally, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` provides the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.topLevel` function that returns Qt Widgets Designer's top-level widget.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface`.
