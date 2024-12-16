.. sip:class-description::
    :status: todo
    :brief: Allows you to change the focus of Qt Widgets Designer's object inspector
    :digest: 63bc7effc67b47a9de1b2011969fa9b7

The :sip:ref:`~PyQt6.QtDesigner.QDesignerObjectInspectorInterface` class allows you to change the focus of Qt Widgets Designer's object inspector.

You can use the :sip:ref:`~PyQt6.QtDesigner.QDesignerObjectInspectorInterface` to change the current form window selection. For example, when implementing a custom widget plugin:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractobjectinspector.py
    :lines: 54-60

The :sip:ref:`~PyQt6.QtDesigner.QDesignerObjectInspectorInterface` class is not intended to be instantiated directly. You can retrieve an interface to Qt Widgets Designer's object inspector using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.objectInspector` function. A pointer to Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. When implementing a custom widget plugin, you must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your plugin to Qt Widgets Designer.

The interface provides the :sip:ref:`~PyQt6.QtDesigner.QDesignerObjectInspectorInterface.core` function that you can use to retrieve a pointer to Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerObjectInspectorInterface.setFormWindow` function that enables you to change the current form window selection.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`.
