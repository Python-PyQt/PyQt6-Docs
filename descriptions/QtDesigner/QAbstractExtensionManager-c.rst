.. sip:class-description::
    :status: todo
    :brief: Interface for extension managers in Qt Designer
    :digest: 605661a0903c6b9bf7bae35b76a359fb

The :sip:ref:`~PyQt6.QtDesigner.QAbstractExtensionManager` class provides an interface for extension managers in *Qt Designer*.

:sip:ref:`~PyQt6.QtDesigner.QAbstractExtensionManager` is not intended to be instantiated directly; use the :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` instead.

In *Qt Designer*, extension are not created until they are required. For that reason, when implementing a custom extension, you must also create a :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`, i.e a class that is able to make an instance of your extension, and register it using *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`.

When an extension is required, *Qt Designer*'s :sip:ref:`~PyQt6.QtDesigner.QExtensionManager` will run through all its registered factories calling :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory.createExtension` for each until the first one that is able to create the requested extension for the selected object, is found. This factory will then make an instance of the extension.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QExtensionManager`, :sip:ref:`~PyQt6.QtDesigner.QExtensionFactory`.
