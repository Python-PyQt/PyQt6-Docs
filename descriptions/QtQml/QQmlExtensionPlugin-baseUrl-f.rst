.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: () const
    :digest: 05d26d53491c0ebfb8453e83ad21f57a

This is unnecessary and doesn't work for optional plugins

Returns the URL of the directory from which the extension is loaded.

This is useful when the plugin also needs to load QML files or other assets from the same directory.

**Note:** You should not need this function. Other files that are part of the module's public interface should be specified accordingly in the build system and qmldir file. The build system makes sure that they end up both in the final module directory, and in the resource file system. You can use the copy from the resource file system in the plugin. Non-QML/JS files private to the plugin can be added to the resource file system manually. However, consider moving all such functionality out of the plugin and making the plugin optional.
