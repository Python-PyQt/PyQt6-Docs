.. sip:class-description::
    :status: todo
    :brief: Enables Qt Designer to access and construct custom widgets
    :digest: 51ebd22c62656c9560f263e886952bfd

The :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` class enables Qt Designer to access and construct custom widgets.

:sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` provides a custom widget with an interface. The class contains a set of functions that must be subclassed to return basic information about the widget, such as its class name and the name of its header file. Other functions must be implemented to initialize the plugin when it is loaded, and to construct instances of the custom widget for *Qt Designer* to use.

When implementing a custom widget you must subclass :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` to expose your widget to *Qt Designer*. For example, this is the declaration for the plugin used in the `Custom Widget Plugin example <https://doc.qt.io/qt-6/qtdesigner-customwidgetplugin-example.html>`_ that enables an analog clock custom widget to be used by *Qt Designer*:

.. literalinclude:: ../../../snippets/qttools-examples-designer-customwidgetplugin-customwidgetplugin.py
    :lines: 59-81

Note that the only part of the class definition that is specific to this particular custom widget is the class name. In addition, since we are implementing an interface, we must ensure that it's made known to the meta object system using the Q_INTERFACES() macro. This enables *Qt Designer* to use the qobject_cast() function to query for supported interfaces using nothing but a :sip:ref:`~PyQt6.QtCore.QObject` pointer.

After *Qt Designer* loads a custom widget plugin, it calls the interface's :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.initialize` function to enable it to set up any resources that it may need. This function is called with a :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface` parameter that provides the plugin with a gateway to all of *Qt Designer*'s API.

*Qt Designer* constructs instances of the custom widget by calling the plugin's :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface.createWidget` function with a suitable parent widget. Plugins must construct and return an instance of a custom widget with the specified parent widget.

Exporting your custom widget plugin to *Qt Designer* using the Q_PLUGIN_METADATA() macro. For example, if a library called ``libcustomwidgetplugin.so`` (on Unix) or ``libcustomwidget.dll`` (on Windows) contains a widget class called ``MyCustomWidget``, we can export it by adding the following line to the file containing the plugin header:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-plugins-doc_src_qtdesigner.py
    :lines: 276-276

This macro ensures that *Qt Designer* can access and construct the custom widget. Without this macro, there is no way for *Qt Designer* to use it.

When implementing a custom widget plugin, you build it as a separate library. If you want to include several custom widget plugins in the same library, you must in addition subclass :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetCollectionInterface`.

**Warning:** If your custom widget plugin contains `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ properties, be aware that only the following types are supported:

* QVariant::ByteArray

* QVariant::Bool

* QVariant::Color

* QVariant::Cursor

* QVariant::Date

* QVariant::DateTime

* QVariant::Double

* QVariant::Int

* QVariant::Point

* QVariant::Rect

* QVariant::Size

* QVariant::SizePolicy

* QVariant::String

* QVariant::Time

* QVariant::UInt

For a complete example using the :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetInterface` class, see the `Custom Widget Example <https://doc.qt.io/qt-6/qtdesigner-customwidgetplugin-example.html>`_. The example shows how to create a custom widget plugin for *Qt Designer*.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerCustomWidgetCollectionInterface`, `Creating Custom Widgets for Qt Designer <https://doc.qt.io/qt-6/designer-creating-custom-widgets.html>`_.
