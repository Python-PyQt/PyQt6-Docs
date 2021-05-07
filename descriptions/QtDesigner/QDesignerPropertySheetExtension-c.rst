.. sip:class-description::
    :status: todo
    :brief: Allows you to manipulate a widget's properties which is displayed in Qt Designer's property editor
    :digest: ea6088cfc7b9be27e7b4ccfa812075cb

The :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` class allows you to manipulate a widget's properties which is displayed in Qt Designer's property editor.

:sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` provides a collection of functions that are typically used to query a widget's properties, and to manipulate the properties' appearance in the property editor. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 281-290

Note that if you change the value of a property using the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension.setProperty` function, the undo stack is not updated. To ensure that a property's value can be reverted using the undo stack, you must use the :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setProperty` function, or its buddy :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface.setWidgetProperty`, instead.

When implementing a custom widget plugin, a pointer to *Qt Designer*'s current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter.

The property sheet, or any other extension, can be retrieved by querying *Qt Designer*'s extension manager using the qt_extension() function. When you want to release the extension, you only need to delete the pointer.

All widgets have a default property sheet which populates *Qt Designer*'s property editor with the widget's properties (i.e the ones defined with the Q_PROPERTY() macro). But :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` also provides an interface for creating custom property sheet extensions.

Keep the following limitations in mind:

* *Qt Designer* uses the :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` to feed its property editor. Whenever a widget is selected in its workspace, *Qt Designer* will query for the widget's property sheet extension. If the selected widget has an implemented property sheet extension, this extension will override the default property sheet.

* The data types used by the property sheet for some properties are opaque custom :sip:ref:`~PyQt6.QtCore.QVariant` types containing additional information instead of plain Qt data types. For example, this is the case for enumerations, flags, icons, pixmaps and strings.

* *Qt Designer*'s property editor has no implementation for handling Q_PROPERTY types for custom types that have been declared with .

To create a property sheet extension, your extension class must inherit from both :sip:ref:`~PyQt6.QtCore.QObject` and :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension`. Then, since we are implementing an interface, we must ensure that it's made known to the meta object system using the Q_INTERFACES() macro:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 295-303

This enables *Qt Designer* to use qobject_cast() to query for supported interfaces using nothing but a :sip:ref:`~PyQt6.QtCore.QObject` pointer.

In *Qt Designer* the extensions are not created until they are required. For that reason, when implementing a property sheet extension, you must also create a :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, i.e a class that is able to make an instance of your extension, and register it using *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`.

When a property sheet extension is required, *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` will run through all its registered factories calling :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` for each until the first one that is able to create a property sheet extension for the selected widget, is found. This factory will then make an instance of the extension. If no such factory can be found, *Qt Designer* will use the default property sheet.

There are four available types of extensions in *Qt Designer*: :sip:ref:`~PyQt6.QtDesigner.QDesignerContainerExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` and :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension`. Qt Designer's behavior is the same whether the requested extension is associated with a multi page container, a member sheet, a property sheet or a task menu.

The :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` class provides a standard extension factory, and can also be used as an interface for custom extension factories. You can either create a new :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` and reimplement the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 308-319

Or you can use an existing factory, expanding the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function to make the factory able to create a property sheet extension extension as well. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 324-338

For a complete example using an extension class, see the `Task Menu Extension example <https://doc.qt.io/qt-6/qtdesigner-taskmenuextension-example.html>`_. The example shows how to create a custom widget plugin for Qt Designer, and how to to use the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class to add custom items to *Qt Designer*'s task menu.

.. seealso:: QDesignerDynamicPropertySheetExtension, :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`, `Creating Custom Widget Extensions <https://doc.qt.io/qt-6/designer-creating-custom-widgets-extensions.html>`_.
