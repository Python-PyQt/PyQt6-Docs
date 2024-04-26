.. sip:class-description::
    :status: todo
    :brief: Allows you to manipulate a widget's member functions which is displayed when configuring connections using Qt Designer's mode for editing signals and slots
    :digest: 519d4e62c950043c5a81f238dfe49af6

The :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension` class allows you to manipulate a widget's member functions which is displayed when configuring connections using *Qt Designer*'s mode for editing signals and slots.

:sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension` is a collection of functions that is typically used to query a widget's member functions, and to manipulate the member functions' appearance in *Qt Designer*'s signals and slots editing mode. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 59-66

When implementing a custom widget plugin, a pointer to *Qt Designer*'s current :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` object (``formEditor`` in the example above) is provided by the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function's parameter.

The member sheet (and any other extension), can be retrieved by querying *Qt Designer*'s extension manager using the qt_extension() function. When you want to release the extension, you only need to delete the pointer.

All widgets have a default member sheet used in *Qt Designer*'s signals and slots editing mode with the widget's member functions. But :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension` also provides an interface for creating custom member sheet extensions.

**Warning:** *Qt Designer* uses the :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension` to facilitate the signal and slot editing mode. Whenever a connection between two widgets is requested, *Qt Designer* will query for the widgets' member sheet extensions. If a widget has an implemented member sheet extension, this extension will override the default member sheet.

To create a member sheet extension, your extension class must inherit from both :sip:ref:`~PyQt6.QtCore.QObject` and :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension`. Then, since we are implementing an interface, we must ensure that it's made known to the meta object system using the Q_INTERFACES() macro:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 71-79

This enables *Qt Designer* to use qobject_cast() to query for supported interfaces using nothing but a :sip:ref:`~PyQt6.QtCore.QObject` pointer.

In *Qt Designer* the extensions are not created until they are required. For that reason, when implementing a member sheet extension, you must also create a :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, i.e a class that is able to make an instance of your extension, and register it using *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`.

When a widget's member sheet extension is required, *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` will run through all its registered factories calling :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` for each until the first one that is able to create a member sheet extension for that widget, is found. This factory will then make an instance of the extension. If no such factory is found, *Qt Designer* will use the default member sheet.

There are four available types of extensions in *Qt Designer*: :sip:ref:`~PyQt6.QtDesigner.QDesignerContainerExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension` and :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension`. *Qt Designer*'s behavior is the same whether the requested extension is associated with a multi page container, a member sheet, a property sheet or a task menu.

The :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` class provides a standard extension factory, and can also be used as an interface for custom extension factories. You can either create a new :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` and reimplement the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 84-95

Or you can use an existing factory, expanding the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function to make the factory able to create a member sheet extension as well. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 100-114

For a complete example using an extension class, see `Task Menu Extension example <https://doc.qt.io/qt-6/qtdesigner-taskmenuextension-example.html>`_. The example shows how to create a custom widget plugin for Qt Designer, and how to use the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class to add custom items to *Qt Designer*'s task menu.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`, `Creating Custom Widget Extensions <https://doc.qt.io/qt-6/designer-creating-custom-widgets-extensions.html>`_.
