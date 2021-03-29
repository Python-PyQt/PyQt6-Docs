.. sip:class-description::
    :status: todo
    :brief: Allows you to query and manipulate the current state of Qt Designer's property editor
    :digest: f722a8863050732d844232e85456fc8c

The :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface` class allows you to query and manipulate the current state of Qt Designer's property editor.

:sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface` contains a collection of functions that is typically used to query the property editor for its current state, and several slots manipulating it's state. The interface also provide a signal, :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.propertyChanged`, which is emitted whenever a property changes in the property editor. The signal's arguments are the property that changed and its new value.

For example, when implementing a custom widget plugin, you can connect the signal to a custom slot:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractpropertyeditor.py
    :lines: 54-58

Then the custom slot can check if the new value is within the range we want when a specified property, belonging to a particular widget, changes:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_sdk_abstractpropertyeditor.py
    :lines: 63-72

The :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface` class is not intended to be instantiated directly. You can retrieve an interface to *Qt Designer*'s property editor using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.propertyEditor` function. A pointer to *Qt Designer*'s current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the examples above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. When implementing a custom widget plugin, you must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your plugin to *Qt Designer*.

The functions accessing the property editor are the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.core` function that you can use to retrieve an interface to the form editor, the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.currentPropertyName` function that returns the name of the currently selected property in the property editor, the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.object` function that returns the currently selected object in *Qt Designer*'s workspace, and the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.isReadOnly` function that returns true if the property editor is write proteced (otherwise false).

The slots manipulating the property editor's state are the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.setObject` slot that you can use to change the currently selected object in *Qt Designer*'s workspace, the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.setPropertyValue` slot that changes the value of a given property and the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertyEditorInterface.setReadOnly` slot that control the write protection of the property editor.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`.
