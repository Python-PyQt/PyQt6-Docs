.. sip:class-description::
    :status: todo
    :brief: Allows you to create a factory that is able to make instances of custom extensions in Qt Designer
    :digest: 1de3ad751dc0e9578cce75f1911b604a

The :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` class allows you to create a factory that is able to make instances of custom extensions in Qt Designer.

In *Qt Designer* the extensions are not created until they are required. For that reason, when implementing a custom extension, you must also create a :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, i.e. a class that is able to make an instance of your extension, and register it using *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`.

The :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` class provides extension management facilities for Qt Designer. When an extension is required, Qt Designer's :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` will run through all its registered factories calling :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` for each until the first one that is able to create a requested extension for the selected object, is found. This factory will then make an instance of the extension.

There are four available types of extensions in Qt Designer: :sip:ref:`~PyQt6.QtDesigner.QDesignerContainerExtension` , :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` and :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension`. Qt Designer's behavior is the same whether the requested extension is associated with a multi page container, a member sheet, a property sheet or a task menu.

You can either create a new :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` and reimplement the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_extension_default_extensionfactory.py
    :lines: 54-65

Or you can use an existing factory, expanding the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function to make the factory able to create your extension as well. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_extension_default_extensionfactory.py
    :lines: 70-84

For a complete example using the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` class, see the `Task Menu Extension example <https://doc.qt.io/qt-6/qtdesigner-taskmenuextension-example.html>`_. The example shows how to create a custom widget plugin for Qt Designer, and how to to use the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class to add custom items to Qt Designer's task menu.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`, :sip:ref:`~PyQt6.QtDesigner.QAbstractExtensionFactory`.
