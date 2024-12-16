.. sip:class-description::
    :status: todo
    :brief: Extension management facilities for Qt Widgets Designer
    :digest: 2d574ccb834021f549c98c8b9d3058ea

The :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` class provides extension management facilities for Qt Widgets Designer.

In Qt Widgets Designer the extensions are not created until they are required. For that reason, when implementing an extension, you must also create a :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, i.e a class that is able to make an instance of your extension, and register it using Qt Widgets Designer's extension manager.

The registration of an extension factory is typically made in the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_extension_qextensionmanager.py
    :lines: 54-66

The :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` is not intended to be instantiated directly. You can retrieve an interface to Qt Widgets Designer's extension manager using the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface.extensionManager` function. A pointer to Qt Widgets Designer's current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter. When implementing a custom widget plugin, you must subclass the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your plugin to Qt Widgets Designer.

Then, when an extension is required, Qt Widgets Designer's extension manager will run through all its registered factories calling :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` for each until the first one that is able to create the requested extension for the selected object, is found. This factory will then make an instance of the extension.

There are four available types of extensions in Qt Widgets Designer: :sip:ref:`~PyQt6.QtDesigner.QDesignerContainerExtension` , :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` and :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension`. Qt Widgets Designer's behavior is the same whether the requested extension is associated with a container, a member sheet, a property sheet or a task menu.

For a complete example using the :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` class, see the `Task Menu Extension example <https://doc.qt.io/qt-6/qtdesigner-taskmenuextension-example.html>`_. The example shows how to create a custom widget plugin for Qt Designer, and how to use the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class to add custom items to Qt Widgets Designer's task menu.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, :sip:ref:`~PyQt6.QtDesigner.QAbstractExtensionManager`.
