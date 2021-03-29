.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: (bool)
    :digest: a3083de0779d5e0eb208ffe21b6f4ed5

If *testMode* is ``true``, this enables a special "test mode" in :sip:ref:`~PyQt6.QtCore.QStandardPaths`, which changes writable locations to point to test directories. This prevents auto tests from reading or writing to the current user's configuration.

It affects the locations into which test programs might write files: ``GenericDataLocation``, ``AppDataLocation``, ``ConfigLocation``, ``GenericConfigLocation``, ``AppConfigLocation``, ``GenericCacheLocation``, and ``CacheLocation``. Other locations are not affected.

On Unix, ``XDG_DATA_HOME`` is set to ``~/.qttest/share``, ``XDG_CONFIG_HOME`` is set to ``~/.qttest/config``, and ``XDG_CACHE_HOME`` is set to ``~/.qttest/cache``.

On macOS, data goes to ``~/.qttest/Application Support``, cache goes to ``~/.qttest/Cache``, and config goes to ``~/.qttest/Preferences``.

On Windows, everything goes to a "qttest" directory under ``%APPDATA%``.
