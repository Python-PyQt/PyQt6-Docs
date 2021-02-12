.. sip:class-description::
    :status: todo
    :brief: Convenient way of selecting file variants
    :digest: 34cae4b288ec3e5dac4e6e5fdc169641

:sip:ref:`~PyQt6.QtCore.QFileSelector` provides a convenient way of selecting file variants.

:sip:ref:`~PyQt6.QtCore.QFileSelector` is a convenience for selecting file variants based on platform or device characteristics. This allows you to develop and deploy one codebase containing all the different variants more easily in some circumstances, such as when the correct variant cannot be determined during the deploy step.

.. _qfileselector-using-qfileselector:

Using QFileSelector
-------------------

If you always use the same file you do not need to use :sip:ref:`~PyQt6.QtCore.QFileSelector`.

Consider the following example usage, where you want to use different settings files on different locales. You might select code between locales like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileselector.py
    :lines: 54-60

Similarly, if you want to pick a different data file based on target platform, your code might look something like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileselector.py
    :lines: 64-70

:sip:ref:`~PyQt6.QtCore.QFileSelector` provides a convenient alternative to writing such boilerplate code, and in the latter case it allows you to start using an platform-specific configuration without a recompile. :sip:ref:`~PyQt6.QtCore.QFileSelector` also allows for chaining of multiple selectors in a convenient way, for example selecting a different file only on certain combinations of platform and locale. For example, to select based on platform and/or locale, the code is as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileselector.py
    :lines: 74-75

The files to be selected are placed in directories named with a ``'+'`` and a selector name. In the above example you could have the platform configurations selected by placing them in the following locations:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileselector.py
    :lines: 79-81

To find selected files, :sip:ref:`~PyQt6.QtCore.QFileSelector` looks in the same directory as the base file. If there are any directories of the form +<selector> with an active selector, :sip:ref:`~PyQt6.QtCore.QFileSelector` will prefer a file with the same file name from that directory over the base file. These directories can be nested to check against multiple selectors, for example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileselector.py
    :lines: 85-86

With those files available, you would select a different file on the android platform, but only if the locale was en_GB.

For error handling in the case no valid selectors are present, it is recommended to have a default or error-handling file in the base file location even if you expect selectors to be present for all deployments.

In a future version, some may be marked as deploy-time static and be moved during the deployment step as an optimization. As selectors come with a performance cost, it is recommended to avoid their use in circumstances involving performance-critical code.

.. _qfileselector-adding-selectors:

Adding Selectors
----------------

Selectors normally available are

* platform, any of the following strings which match the platform the application is running on (list not exhaustive): android, ios, osx, darwin, mac, macos, linux, qnx, unix, windows. On Linux, if it can be determined, the name of the distribution too, like debian, fedora or opensuse.

* locale, same as QLocale().name().

Further selectors will be added from the ``QT_FILE_SELECTORS`` environment variable, which when set should be a set of comma separated selectors. Note that this variable will only be read once; selectors may not update if the variable changes while the application is running. The initial set of selectors are evaluated only once, on first use.

You can also add extra selectors at runtime for custom behavior. These will be used in any future calls to :sip:ref:`~PyQt6.QtCore.QFileSelector.select`. If the extra selectors list has been changed, calls to :sip:ref:`~PyQt6.QtCore.QFileSelector.select` will use the new list and may return differently.

.. _qfileselector-conflict-resolution-when-multiple-selectors-apply:

Conflict Resolution when Multiple Selectors Apply
-------------------------------------------------

When multiple selectors could be applied to the same file, the first matching selector is chosen. The order selectors are checked in are:

#. Selectors set via :sip:ref:`~PyQt6.QtCore.QFileSelector.setExtraSelectors`, in the order they are in the list

#. Selectors in the ``QT_FILE_SELECTORS`` environment variable, from left to right

#. Locale

#. Platform

Here is an example involving multiple selectors matching at the same time. It uses platform selectors, plus an extra selector named "admin" is set by the application based on user credentials. The example is sorted so that the lowest matching file would be chosen if all selectors were present:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileselector.py
    :lines: 90-94

Because extra selectors are checked before platform the ``+admin/background.png`` will be chosen on Windows when the admin selector is set, and ``+windows/background.png`` will be chosen on Windows when the admin selector is not set. On Linux, the ``+admin/+linux/background.png`` will be chosen when admin is set, and the ``+linux/background.png`` when it is not.
