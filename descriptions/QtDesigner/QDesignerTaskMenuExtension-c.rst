.. sip:class-description::
    :status: todo
    :brief: Allows you to add custom menu entries to Qt Designer's task menu
    :digest: 8ae5ee9b47cbbe6792a1024dea685004

The :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class allows you to add custom menu entries to Qt Designer's task menu.

:sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` provides an interface for creating custom task menu extensions. It is typically used to create task menu entries that are specific to a plugin in *Qt Designer*.

*Qt Designer* uses the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` to feed its task menu. Whenever a task menu is requested, *Qt Designer* will query for the selected widget's task menu extension.

.. image:: ../../../images/taskmenuextension-example-faded.png

A task menu extension is a collection of QActions. The actions appear as entries in the task menu when the plugin with the specified extension is selected. The image above shows the custom **Edit State...** action which appears in addition to *Qt Designer*'s default task menu entries: **Cut**, **Copy**, **Paste** etc.

To create a custom task menu extension, your extension class must inherit from both :sip:ref:`~PyQt6.QtCore.QObject` and :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension`. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 178-196

Since we are implementing an interface, we must ensure that it is made known to the meta-object system using the Q_INTERFACES() macro. This enables *Qt Designer* to use the qobject_cast() function to query for supported interfaces using nothing but a :sip:ref:`~PyQt6.QtCore.QObject` pointer.

You must reimplement the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension.taskActions` function to return a list of actions that will be included in *Qt Designer* task menu. Optionally, you can reimplement the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension.preferredEditAction` function to set the action that is invoked when selecting your plugin and pressing **F2**. The preferred edit action must be one of the actions returned by :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension.taskActions` and, if it's not defined, pressing the **F2** key will simply be ignored.

In *Qt Designer*, extensions are not created until they are required. A task menu extension, for example, is created when you click the right mouse button over a widget in *Qt Designer*'s workspace. For that reason you must also construct an extension factory, using either :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` or a subclass, and register it using *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`.

When a task menu extension is required, *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` will run through all its registered factories calling :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` for each until it finds one that is able to create a task menu extension for the selected widget. This factory will then make an instance of the extension.

There are four available types of extensions in *Qt Designer*: :sip:ref:`~PyQt6.QtDesigner.QDesignerContainerExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerMemberSheetExtension`, :sip:ref:`~PyQt6.QtDesigner.QDesignerPropertySheetExtension`, and :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension`. *Qt Designer*'s behavior is the same whether the requested extension is associated with a container, a member sheet, a property sheet or a task menu.

The :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` class provides a standard extension factory, and can also be used as an interface for custom extension factories. You can either create a new :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory` and reimplement the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 201-211

Or you can use an existing factory, expanding the :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` function to make the factory able to create a task menu extension as well. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 216-230

For a complete example using the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class, see the `Task Menu Extension example <https://doc.qt.io/qt-6/qtdesigner-taskmenuextension-example.html>`_. The example shows how to create a custom widget plugin for *Qt Designer*, and how to to use the :sip:ref:`~PyQt6.QtDesigner.QDesignerTaskMenuExtension` class to add custom items to *Qt Designer*'s task menu.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`, `Creating Custom Widget Extensions <https://doc.qt.io/qt-6/designer-creating-custom-widgets-extensions.html>`_.
