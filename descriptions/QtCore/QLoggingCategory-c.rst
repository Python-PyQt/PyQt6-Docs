.. sip:class-description::
    :status: todo
    :brief: Represents a category, or 'area' in the logging infrastructure
    :digest: 223fa5b914bc288cfc05090ffe7b8ffc

The :sip:ref:`~PyQt6.QtCore.QLoggingCategory` class represents a category, or 'area' in the logging infrastructure.

:sip:ref:`~PyQt6.QtCore.QLoggingCategory` represents a certain logging category - identified by a string - at runtime. A category can be configured to enable or disable logging of messages per message type.

To check whether a message type is enabled or not, use one of these methods: :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isDebugEnabled`, :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isInfoEnabled`, :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isWarningEnabled`, and :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isCriticalEnabled`.

All objects are meant to be configured by a common registry, as described in :ref:`qloggingcategory-configuring-categories`. Different objects can also represent the same category. Therefore, it's **not** recommended to export objects across module boundaries, to manipulate the objects directly, or to inherit from :sip:ref:`~PyQt6.QtCore.QLoggingCategory`.

.. _qloggingcategory-creating-category-objects:

Creating Category Objects
-------------------------

The Q_DECLARE_LOGGING_CATEGORY() and Q_LOGGING_CATEGORY() macros conveniently declare and create :sip:ref:`~PyQt6.QtCore.QLoggingCategory` objects:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qloggingcategory-main.py

Category names are free text; to configure categories using :ref:`qloggingcategory-logging-rules`, their names should follow this convention:

* Use letters and numbers only.

* Use dots to further structure categories into common areas.

* Avoid the category names: ``debug``, ``info``, ``warning``, and ``critical``.

* Category names with the ``qt`` prefix are solely reserved for Qt modules.

:sip:ref:`~PyQt6.QtCore.QLoggingCategory` objects that are implicitly defined by Q_LOGGING_CATEGORY() are created on first use, in a thread-safe manner.

.. _qloggingcategory-checking-category-configuration:

Checking Category Configuration
-------------------------------

:sip:ref:`~PyQt6.QtCore.QLoggingCategory` provides :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isDebugEnabled`, :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isInfoEnabled`, :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isWarningEnabled`, :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isCriticalEnabled`, as well as :sip:ref:`~PyQt6.QtCore.QLoggingCategory.isEnabled` to check whether messages for the given message type should be logged.

The qCDebug(), qCWarning(), and qCCritical() macros prevent arguments from being evaluated if the respective message types are not enabled for the category, so explicit checking is not needed:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qloggingcategory-main.py

.. _qloggingcategory-default-category-configuration:

Default Category Configuration
------------------------------

Both the :sip:ref:`~PyQt6.QtCore.QLoggingCategory` constructor and the Q_LOGGING_CATEGORY() macro accept an optional :sip:ref:`~PyQt6.QtCore.QtMsgType` argument, which disables all message types with a lower severity. That is, a category declared with

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qloggingcategory-main.py

logs messages of type ``QtWarningMsg``, ``QtCriticalMsg``, ``QtFatalMsg``, but ignores messages of type ``QtDebugMsg`` and ``QtInfoMsg``.

If no argument is passed, all messages are logged. Only Qt internal categories which start with ``qt`` are handled differently: For these, only messages of type ``QtInfoMsg``, ``QtWarningMsg``, and ``QtCriticalMsg`` are logged by default.

**Note:** Logging categories are not affected by your C++ build configuration. That is, whether messages are printed does not change depending on whether the code is compiled with debug symbols ('Debug Build'), optimizations ('Release Build'), or some other combination.

.. _qloggingcategory-configuring-categories:

Configuring Categories
----------------------

You can override the default configuration for categories either by setting logging rules, or by installing a custom filter.

.. _qloggingcategory-logging-rules:

Logging Rules
.............

Logging rules let you enable or disable logging for categories in a flexible way. Rules are specified in text, where every line must have the format:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qloggingcategory.py
    :lines: 54-54

``<category>`` is the name of the category, potentially with ``\*`` as a wildcard symbol for the first or last character; or at both positions. The optional ``<type>`` must be ``debug``, ``info``, ``warning``, or ``critical``. Lines that don't fit this scheme are ignored.

Rules are evaluated in text order, from first to last. That is, if two rules apply to a category/type, the rule that comes later is applied.

Rules can be set via :sip:ref:`~PyQt6.QtCore.QLoggingCategory.setFilterRules`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qloggingcategory.py
    :lines: 58-59

Logging rules are automatically loaded from the ``[Rules]`` section in a logging configuration file. These configuration files are looked up in the QtProject configuration directory, or explicitly set in a ``QT_LOGGING_CONF`` environment variable:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qloggingcategory.py
    :lines: 63-65

Logging rules can also be specified in a ``QT_LOGGING_RULES`` environment variable; multiple rules can also be separated by semicolons:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qloggingcategory.py
    :lines: 69-69

Rules set by :sip:ref:`~PyQt6.QtCore.QLoggingCategory.setFilterRules` take precedence over rules specified in the QtProject configuration directory. In turn, these rules can be overwritten by those from the configuration file specified by ``QT_LOGGING_CONF``, and those set by ``QT_LOGGING_RULES``.

The order of evaluation is as follows:

#. [\ :sip:ref:`~PyQt6.QtCore.QLibraryInfo.LibraryPath.DataPath`]/qtlogging.ini

#. QtProject/qtlogging.ini

#. :sip:ref:`~PyQt6.QtCore.QLoggingCategory.setFilterRules`

#. ``QT_LOGGING_CONF``

#. ``QT_LOGGING_RULES``

The ``QtProject/qtlogging.ini`` file is looked up in all directories returned by :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.GenericConfigLocation`.

Set the ``QT_LOGGING_DEBUG`` environment variable to find out where your logging rules are loaded from.

.. _qloggingcategory-installing-a-custom-filter:

Installing a Custom Filter
..........................

As a lower-level alternative to the text rules, you can also implement a custom filter via installFilter(). All filter rules are ignored in this case.

.. _qloggingcategory-printing-the-category:

Printing the Category
---------------------

Use the ``%{category}`` placeholder to print the category in the default message handler:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qloggingcategory-main.py
