:orphan:

.. sip:class:: PyQt6.QtQml.QQmlEngine
    :inherits: :sip:ref:`~PyQt6.QtQml.QJSEngine`
    :description: QtQml/QQmlEngine-c.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtQml/QQmlEngine-__init__-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.addImageProvider
        :args:
            str
            :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase`
        :description: QtQml/QQmlEngine-addImageProvider-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.addImportPath
        :args:
            str
        :description: QtQml/QQmlEngine-addImportPath-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.addPluginPath
        :args:
            str
        :description: QtQml/QQmlEngine-addPluginPath-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.addUrlInterceptor
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor`
        :description: QtQml/QQmlEngine-addUrlInterceptor-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.baseUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QQmlEngine-baseUrl-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.clearComponentCache
        :description: QtQml/QQmlEngine-clearComponentCache-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.clearSingletons
        :description: QtQml/QQmlEngine-clearSingletons-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.contextForObject
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :static:
        :description: QtQml/QQmlEngine-contextForObject-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtQml/QQmlEngine-event-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.imageProvider
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlImageProviderBase`
        :description: QtQml/QQmlEngine-imageProvider-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.importPathList
        :returns:
            List[str]
        :description: QtQml/QQmlEngine-importPathList-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.importPlugin
        :args:
            str
            str
            Iterable[:sip:ref:`~PyQt6.QtQml.QQmlError`]
        :returns:
            bool
        :description: QtQml/QQmlEngine-importPlugin-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.incubationController
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubationController`
        :description: QtQml/QQmlEngine-incubationController-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.interceptUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            :sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor.DataType`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QQmlEngine-interceptUrl-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.networkAccessManager
        :returns:
            :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`
        :description: QtQml/QQmlEngine-networkAccessManager-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.networkAccessManagerFactory
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory`
        :description: QtQml/QQmlEngine-networkAccessManagerFactory-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.offlineStorageDatabaseFilePath
        :args:
            str
        :returns:
            str
        :description: QtQml/QQmlEngine-offlineStorageDatabaseFilePath-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.offlineStoragePath
        :returns:
            str
        :description: QtQml/QQmlEngine-offlineStoragePath-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.outputWarningsToStandardError
        :returns:
            bool
        :description: QtQml/QQmlEngine-outputWarningsToStandardError-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.pluginPathList
        :returns:
            List[str]
        :description: QtQml/QQmlEngine-pluginPathList-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.removeImageProvider
        :args:
            str
        :description: QtQml/QQmlEngine-removeImageProvider-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.removeUrlInterceptor
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor`
        :description: QtQml/QQmlEngine-removeUrlInterceptor-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.retranslate
        :description: QtQml/QQmlEngine-retranslate-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.rootContext
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :description: QtQml/QQmlEngine-rootContext-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setBaseUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQml/QQmlEngine-setBaseUrl-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setContextForObject
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :static:
        :description: QtQml/QQmlEngine-setContextForObject-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setImportPathList
        :args:
            Iterable[str]
        :description: QtQml/QQmlEngine-setImportPathList-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setIncubationController
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlIncubationController`
        :description: QtQml/QQmlEngine-setIncubationController-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setNetworkAccessManagerFactory
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory`
        :description: QtQml/QQmlEngine-setNetworkAccessManagerFactory-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setOfflineStoragePath
        :args:
            str
        :description: QtQml/QQmlEngine-setOfflineStoragePath-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setOutputWarningsToStandardError
        :args:
            bool
        :description: QtQml/QQmlEngine-setOutputWarningsToStandardError-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.setPluginPathList
        :args:
            Iterable[str]
        :description: QtQml/QQmlEngine-setPluginPathList-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.singletonInstance
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlEngine-singletonInstance-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.singletonInstance
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, str]
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, str]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtQml/QQmlEngine-singletonInstance-f-1.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.trimComponentCache
        :description: QtQml/QQmlEngine-trimComponentCache-f.rst

    .. sip:method:: PyQt6.QtQml.QQmlEngine.urlInterceptors
        :returns:
            List[:sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor`]
        :description: QtQml/QQmlEngine-urlInterceptors-f.rst

    .. sip:signal:: PyQt6.QtQml.QQmlEngine.exit
        :args:
            int
        :description: QtQml/QQmlEngine-exit-s.rst

    .. sip:signal:: PyQt6.QtQml.QQmlEngine.offlineStoragePathChanged
        :description: QtQml/QQmlEngine-offlineStoragePathChanged-s.rst

    .. sip:signal:: PyQt6.QtQml.QQmlEngine.quit
        :description: QtQml/QQmlEngine-quit-s.rst

    .. sip:signal:: PyQt6.QtQml.QQmlEngine.warnings
        :args:
            Iterable[:sip:ref:`~PyQt6.QtQml.QQmlError`]
        :description: QtQml/QQmlEngine-warnings-s.rst
