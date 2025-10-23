.. sip:class-description::
    :status: todo
    :brief: The core functionality of the help system
    :digest: 3c409c800cdaa49acdeacfd6eb49fd33

The :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore` class provides the core functionality of the help system.

Before the help engine can be used, it must be initialized by calling :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setupData`. At the beginning of the setup process the signal :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setupStarted` is emitted. From this point on until the signal :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setupFinished` is emitted, is the help data in an undefined meaning unusable state.

The core help engine can be used to perform different tasks. By calling :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.documentsForIdentifier` the engine returns URLs specifying the file locations inside the help system. The actual file data can then be retrieved by calling :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.fileData`.

The help engine can contain any number of custom filters. The management of the filters, including adding new filters, changing filter definitions, or removing existing filters, is done through the :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine` class, which can be accessed by the :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.filterEngine` method.

**Note:** :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine` replaces the older filter API that is deprecated since Qt 5.13. Call :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setUsesFilterEngine` with ``true`` to enable the new functionality.

The core help engine has two modes:

* Read-only mode, where the help collection file is not changed unless explicitly requested. This also works if the collection file is in a read-only location, and is the default.

* Fully writable mode, which requires the help collection file to be writable.

The mode can be changed by calling :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setReadOnly` method, prior to calling :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setupData`.

The help engine also offers the possibility to set and read values in a persistent way comparable to ini files or Windows registry entries. For more information see :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.setCustomValue` or :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.customValue`.

This class does not offer any GUI components or functionality for indices or contents. If you need one of those use :sip:ref:`~PyQt6.QtHelp.QHelpEngine` instead.
