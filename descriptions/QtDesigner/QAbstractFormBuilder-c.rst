.. sip:class-description::
    :status: todo
    :brief: Default implementation for classes that create user interfaces at run-time
    :digest: 6d84fd9b9d13533a52dd0120ed687490

The :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder` class provides a default implementation for classes that create user interfaces at run-time.

:sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder` provides a standard interface and a default implementation for constructing forms from user interface files. It is not intended to be instantiated directly. Use the :sip:ref:`~PyQt6.QtDesigner.QFormBuilder` class to create user interfaces from UI files at run-time. For example:

.. literalinclude:: ../../../snippets/qttools-src-designer-src-designer-doc-snippets-lib-tools_designer_src_lib_uilib_abstractformbuilder.py
    :lines: 54-66

To override certain aspects of the form builder's behavior, subclass :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder` and reimplement the relevant virtual functions:

* :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder.load` handles reading of UI format files from arbitrary QIODevices, and construction of widgets from the XML data that they contain.

* :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder.save` handles saving of widget details in UI format to arbitrary QIODevices.

* :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder.workingDirectory` and :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder.setWorkingDirectory` control the directory in which forms are held. The form builder looks for other resources on paths relative to this directory.

The :sip:ref:`~PyQt6.QtDesigner.QFormBuilder` class is typically used by custom components and applications that embed *Qt Designer*. Standalone applications that need to dynamically generate user interfaces at run-time use the QUiLoader, found in the Qt UI Tools module.

.. seealso:: Qt UI Tools.
