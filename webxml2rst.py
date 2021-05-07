# Copyright (c) 2021, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import hashlib
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as etree

from collections import namedtuple


def error(message):
    """ Write an error message to stderr and terminate with a non-zero exit
    code.
    """

    program_name = os.path.basename(sys.argv[0])
    sys.stderr.write("{}: {}\n".format(program_name, message))
    sys.exit(1)


def progress(message):
    """ Write a progress message to stdout. """

    print(message, flush=True)


def warning(message):
    """ Write a warning message to stderr. """

    program_name = os.path.basename(sys.argv[0])
    sys.stderr.write("{}: warning: {}\n".format(program_name, message))


class WebXMLMetadata:
    """ Encapsulate the meta-data for a WebXML module. """

    all_webxml = []

    def __init__(self, name, qdocconf, more_images=None, locations=None):
        """ Initialise the object. """

        # The name of the module.
        self.name = name

        # The name of the .qdocconf file relative to the source directory using
        # POSIX path separators.
        self._qdocconf = qdocconf

        # The names of directories containing 'images' sub-directories.  It
        # defaults to the directory containing the .qdocconf file.
        self.images = [os.path.dirname(qdocconf.replace('/', os.sep))]
        if more_images is not None:
            self.images.append(more_images.replace('/', os.sep))

        # The dict of object locations for those objects whose location is not
        # derived from the object name.
        self._locations = {} if locations is None else locations

        # Add this to the list of all modules.
        type(self).all_webxml.append(self)

    def create_qdocconf(self, webxml_root, qt_prefix, qt_source):
        """ Create the .qdocconf file and return its name. """

        qdocconf = os.path.join(webxml_root, self.name + '.qdocconf')

        with open(qdocconf, 'w') as qdocconf_f:
            qdocconf_f.write('outputformats = WebXML\n')
            qdocconf_f.write('WebXML.quotinginformation = true\n')
            qdocconf_f.write('WebXML.nosubdirs = true\n')
            qdocconf_f.write('WebXML.outputsubdir = {}\n'.format(self.name))

            parts = [qt_source]
            parts.extend(self._qdocconf.split('/'))
            qdocconf_f.write('include({})\n'.format(os.path.join(*parts)))

            # Note that this is hardcoded for Linux at the moment.
            plat_mkspec = 'linux-g++'

            qt_include = os.path.join(qt_prefix, 'include')
            qdocconf_f.write('includepaths +=')
            qdocconf_f.write(' -I ' + qt_include)
            qdocconf_f.write(
                    ' -I ' + os.path.join(qt_prefix, 'mkspecs', plat_mkspec))

            # Add the header directory for every Qt module.
            for module in ModuleMetadata.all_modules:
                qdocconf_f.write(
                        ' -I ' + os.path.join(qt_include, module.name))

            qdocconf_f.write('\n')

        return qdocconf

    @classmethod
    def find(cls, name):
        """ Find the meta-data for a WebXML module. """

        for webxml in cls.all_webxml:
            if webxml.name == name:
                return webxml

        # This is an internal error.
        error("unknown WebXML module '{}'".format(name))

    def get_object_webxml_name(self, object_name):
        """ Get the name of a WebXML file that contains the given name. """

        try:
            location = self._locations[object_name]
            if location is None:
                return None
        except KeyError:
            location = object_name.lower().replace('::', '-').replace('_', '-')

        return os.path.join(self.name, location + '.webxml')


# The WebXML meta-data.
WebXMLMetadata('qt3d', qdocconf='qt3d/src/core/doc/qt3d.qdocconf',
        locations={
            'Qt3DAnimation::QAbstractChannelMapping': 'qt3danimation',
            'Qt3DAnimation::QChannelComponent': 'qt3danimation',
            'Qt3DAnimation::QClock': 'qt3danimation',
            'Qt3DAnimation::QSkeletonMapping': 'qt3danimation',
            'Qt3DCore::QNodeIdTypePair': 'qt3dcore',
            'Qt3DExtras::QAbstractSpriteSheet': 'qt3dextras',
            'Qt3DExtras::QSpriteGrid': 'qt3dextras',
            'Qt3DExtras::QSpriteSheet': 'qt3dextras',
            'Qt3DExtras::QSpriteSheetItem': 'qt3dextras',
            'Qt3DExtras::Qt3DWindow': 'qt3dextras',
            'Qt3DRender::PropertyReaderInterface': 'qt3drender',
            'PYQT_3D_VERSION': None,
            'PYQT_3D_VERSION_STR': None,
        })
#WebXMLMetadata('qtactiveqt',
#        qdocconf='qtactiveqt/src/activeqt/doc/activeqt.qdocconf')
#WebXMLMetadata('qtandroidextras',
#        qdocconf='qtandroidextras/src/androidextras/doc/qtandroidextras.qdocconf')
#WebXMLMetadata('qtbluetooth',
#        qdocconf='qtconnectivity/src/bluetooth/doc/qtbluetooth.qdocconf')
WebXMLMetadata('qtcharts',
        qdocconf='qtcharts/src/charts/doc/qtcharts.qdocconf')
WebXMLMetadata('qtcore', qdocconf='qtbase/src/corelib/doc/qtcore.qdocconf',
        locations={
            'Q_ARG': 'qmetaobject',
            'Q_RETURN_ARG': 'qmetaobject',
            'QT_TR_NOOP': 'qtglobal',
            'QT_TRANSLATE_NOOP': 'qtglobal',
            'QT_VERSION': 'qtglobal',
            'QT_VERSION_STR': 'qtglobal',
            'QCalendar::YearMonthDay': 'qcalendar',
            'QCborKnownTags': 'qtcborcommon',
            'QCborSimpleType': 'qtcborcommon',
            'QIODeviceBase': None,
            'QStringConverterBase': None,
            'QtMsgType': 'qtglobal',
            'qAbs': 'qtglobal',
            'qAddPostRoutine': 'qcoreapplication',
            'qAddPreRoutine': 'qcoreapplication',
            'qChecksum': 'qbytearray',
            'qCompress': 'qbytearray',
            'qCritical': 'qtglobal',
            'qEnvironmentVariable': 'qtglobal',
            'qEnvironmentVariableIntValue': 'qtglobal',
            'qEnvironmentVariableIsEmpty': 'qtglobal',
            'qEnvironmentVariableIsSet': 'qtglobal',
            'qFatal': 'qtglobal',
            'qFloatDistance': 'qtglobal',
            'qFormatLogMessage': 'qtglobal',
            'qFuzzyCompare': 'qtglobal',
            'qInf': 'qtglobal',
            'qInfo': 'qtglobal',
            'qInstallMessageHandler': 'qtglobal',
            'qIsFinite': 'qtglobal',
            'qIsInf': 'qtglobal',
            'qIsNaN': 'qtglobal',
            'qQNaN': 'qtglobal',
            'qRemovePostRoutine': 'qcoreapplication',
            'qRound': 'qtglobal',
            'qRound64': 'qtglobal',
            'qSetFieldWidth': 'qtextstream',
            'qSetMessagePattern': 'qtglobal',
            'qSetPadChar': 'qtextstream',
            'qSetRealNumberPrecision': 'qtextstream',
            'qSNaN': 'qtglobal',
            'qUncompress': 'qbytearray',
            'qVersion': 'qtglobal',
            'qWarning': 'qtglobal',
            'bin': 'qt',
            'bom': 'qt',
            'center': 'qt',
            'convertFromPlainText': 'qt',
            'dec': 'qt',
            'endl': 'qt',
            'fixed': 'qt',
            'flush': 'qt',
            'forcepoint': 'qt',
            'forcesign': 'qt',
            'hex': 'qt',
            'left': 'qt',
            'lowercasebase': 'qt',
            'lowercasedigits': 'qt',
            'noforcepoint': 'qt',
            'noforcesign': 'qt',
            'noshowbase': 'qt',
            'oct': 'qt',
            'reset': 'qt',
            'right': 'qt',
            'scientific': 'qt',
            'showbase': 'qt',
            'uppercasebase': 'qt',
            'uppercasedigits': 'qt',
            'ws': 'qt',
            'PYQT_VERSION': None,
            'PYQT_VERSION_STR': None,
            'PyQtMutexLocker': None,
            'pyqtClassInfo': None,
            'pyqtEnum': None,
            'pyqtPickleProtocol': None,
            'pyqtRemoveInputHook': None,
            'pyqtRestoreInputHook': None,
            'pyqtSetPickleProtocol': None,
            'pyqtSlot': None,
        })
WebXMLMetadata('qtdbus', qdocconf='qtbase/src/dbus/doc/qtdbus.qdocconf',
        locations={
            'QPyDBusPendingReply': None,
            'QPyDBusReply': None,
        })
WebXMLMetadata('qtdatavis3d',
        qdocconf='qtdatavis3d/src/datavisualization/doc/qtdatavis3d.qdocconf')
WebXMLMetadata('qtdesigner',
        qdocconf='qttools/src/designer/src/designer/doc/qtdesigner.qdocconf',
        more_images='qttools/examples/designer/doc',
        locations={
            'QPyDesignerContainerExtension': None,
            'QPyDesignerCustomWidgetCollectionPlugin': None,
            'QPyDesignerCustomWidgetPlugin': None,
            'QPyDesignerMemberSheetExtension': None,
            'QPyDesignerPropertySheetExtension': None,
            'QPyDesignerTaskMenuExtension': None,
        })
WebXMLMetadata('qtgui', qdocconf='qtbase/src/gui/doc/qtgui.qdocconf',
        more_images='qtbase/doc/src',
        locations={
            'QColorConstants::Svg': 'qcolorconstants',
            'QMatrix2x2': 'qgenericmatrix',
            'QMatrix2x3': 'qgenericmatrix',
            'QMatrix2x4': 'qgenericmatrix',
            'QMatrix3x2': 'qgenericmatrix',
            'QMatrix3x3': 'qgenericmatrix',
            'QMatrix3x4': 'qgenericmatrix',
            'QMatrix4x2': 'qgenericmatrix',
            'QMatrix4x3': 'qgenericmatrix',
            'qAlpha': 'qcolor',
            'qBlue': 'qcolor',
            'qFuzzyCompare': 'qtransform',
            'qGray': 'qcolor',
            'qGreen': 'qcolor',
            'qPixelFormatAlpha': 'qpixelformat',
            'qPixelFormatCmyk': 'qpixelformat',
            'qPixelFormatGrayscale': 'qpixelformat',
            'qPixelFormatHsl': 'qpixelformat',
            'qPixelFormatHsv': 'qpixelformat',
            'qPixelFormatRgba': 'qpixelformat',
            'qPixelFormatYuv': 'qpixelformat',
            'qPremultiply': 'qcolor',
            'qRed': 'qcolor',
            'qRgb': 'qcolor',
            'qRgba': 'qcolor',
            'qUnpremultiply': 'qcolor',
            'qt_set_sequence_auto_mnemonic': 'qkeysequence',
        })
WebXMLMetadata('qthelp',
        qdocconf='qttools/src/assistant/help/doc/qthelp.qdocconf')
#WebXMLMetadata('qtlocation',
#        qdocconf='qtlocation/src/location/doc/qtlocation.qdocconf')
#WebXMLMetadata('qtmacextras',
#        qdocconf='qtmacextras/src/macextras/doc/qtmacextras.qdocconf')
#WebXMLMetadata('qtmultimedia',
#        qdocconf='qtmultimedia/src/multimedia/doc/qtmultimedia.qdocconf')
WebXMLMetadata('qtnetwork',
        qdocconf='qtbase/src/network/doc/qtnetwork.qdocconf',
        locations={
            # The following line doesn't seem to work. (Maybe there is an
            # unscoped reference?)
            'QOcspCertificateStatus': 'qocsresponse',
            'QOcspRevocationReason': 'qocsresponse',
        })
WebXMLMetadata('qtnetworkauth',
        qdocconf='qtnetworkauth/src/oauth/doc/qtnetworkauth.qdocconf',
        locations={
            # Both of these are marked as internal (and have no documentation)
            # but they are wrapped as it's not clear if they might be needed in
            # some circumstances.
            'QOAuthHttpServerReplyHandler': None,
            'QOAuthOobReplyHandler': None,
            'PYQT_NETWORKAUTH_VERSION': None,
            'PYQT_NETWORKAUTH_VERSION_STR': None,
        })
#WebXMLMetadata('qtnfc', qdocconf='qtconnectivity/src/nfc/doc/qtnfc.qdocconf')
WebXMLMetadata('qtopengl', qdocconf='qtbase/src/opengl/doc/qtopengl.qdocconf')
#WebXMLMetadata('qtpositioning',
#        qdocconf='qtlocation/src/positioning/doc/qtpositioning.qdocconf')
WebXMLMetadata('qtprintsupport',
        qdocconf='qtbase/src/printsupport/doc/qtprintsupport.qdocconf')
#WebXMLMetadata('qtpurchasing',
#        qdocconf='qtpurchasing/src/purchasing/doc/qtpurchasing.qdocconf')
WebXMLMetadata('qtqml', qdocconf='qtdeclarative/src/qml/doc/qtqml.qdocconf',
        locations={
            'qmlAttachedPropertiesObject': 'qqmlengine',
            'qmlClearTypeRegistrations': 'qqmlengine',
            'qmlContext': 'qqmlengine',
            'qmlEngine': 'qqmlengine',
            'qmlProtectModule': 'qqmlengine',
            'qmlRegisterAnonymousType': 'qqmlengine',
            'qmlRegisterModule': 'qqmlengine',
            'qmlRegisterRevision': 'qqmlengine',
            'qmlRegisterSingletonInstance': 'qqmlengine',
            'qmlRegisterSingletonType': 'qqmlengine',
            'qmlRegisterType': 'qqmlengine',
            'qmlRegisterTypeNotAvailable': 'qqmlengine',
            'qmlRegisterUncreatableMetaObject': 'qqmlengine',
            'qmlRegisterUncreatableType': 'qqmlengine',
            'qmlTypeId': 'qqmlengine',
        })
WebXMLMetadata('qtquick',
        qdocconf='qtdeclarative/src/quick/doc/qtquick.qdocconf',
        locations={
            'QNativeInterface': 'qnativeinterface-sub-qtquick',
            'QQuickItem::UpdatePaintNodeData': 'qquickitem',
            'QSGRenderNode::RenderState': 'qsgrendernode',
        })
WebXMLMetadata('qtquick3d',
        qdocconf='qtquick3d/src/imports/quick3d/doc/qtquick3d.qdocconf',
        locations={
            'QQuick3DGeometry::Attribute': 'qquick3dgeometry',
        })
#WebXMLMetadata('qtremoteobjects',
#        qdocconf='qtremoteobjects/src/remoteobjects/doc/qtremoteobjects.qdocconf')
#WebXMLMetadata('qtsensors',
#        qdocconf='qtsensors/src/sensors/doc/qtsensors.qdocconf')
#WebXMLMetadata('qtserialport',
#        qdocconf='qtserialport/src/serialport/doc/qtserialport.qdocconf')
WebXMLMetadata('qtsql', qdocconf='qtbase/src/sql/doc/qtsql.qdocconf')
WebXMLMetadata('qtsvg', qdocconf='qtsvg/src/svg/doc/qtsvg.qdocconf')
WebXMLMetadata('qttest', qdocconf='qtbase/src/testlib/doc/qttestlib.qdocconf')
#WebXMLMetadata('qtwebchannel',
#        qdocconf='qtwebchannel/src/webchannel/doc/qtwebchannel.qdocconf')
#WebXMLMetadata('qtwebengine',
#        qdocconf='qtwebengine/src/webengine/doc/qtwebengine.qdocconf')
#WebXMLMetadata('qtwebsockets',
#        qdocconf='qtwebsockets/src/websockets/doc/qtwebsockets.qdocconf')
WebXMLMetadata('qtwidgets',
        qdocconf='qtbase/src/widgets/doc/qtwidgets.qdocconf',
        locations={
            'QWIDGETSIZE_MAX': 'qwidget',
            'qDrawBorderPixmap': 'qdrawutil-h',
            'qDrawPlainRect': 'qdrawutil-h',
            'qDrawShadeLine': 'qdrawutil-h',
            'qDrawShadePanel': 'qdrawutil-h',
            'qDrawShadeRect': 'qdrawutil-h',
            'qDrawWinButton': 'qdrawutil-h',
            'qDrawWinPanel': 'qdrawutil-h',
        })
#WebXMLMetadata('qtwinextras',
#        qdocconf='qtwinextras/src/winextras/doc/qtwinextras.qdocconf')
#WebXMLMetadata('qtx11extras',
#        qdocconf='qtx11extras/src/x11extras/doc/qtx11extras.qdocconf')
WebXMLMetadata('qtxml',
        qdocconf='qtbase/src/xml/doc/qtxml.qdocconf')


class ModuleMetadata:
    """ Encapsulate the meta-data for a module. """

    # The list of all modules.
    all_modules = []

    def __init__(self, name, webxml=None, qt_docs_prefix=''):
        """ Initialise the object. """

        # The name of the module.
        self.name = name

        # The prefix for links in the online Qt documentation for this module.
        self.qt_docs_prefix = qt_docs_prefix

        if webxml is None:
            self.webxml = None
        else:
            self.webxml = WebXMLMetadata.find(webxml)

        # TODO: because some WebXML is shared between modules, should the cache
        # be in the WebXML meta-data and never be cleared?
        self.clear_cache()

        # Add this to the list of all modules.
        type(self).all_modules.append(self)

    def clear_cache(self):
        """ Clear the cache of parsed WebXML data. """

        self._webxml_cache = {}

    @classmethod
    def find(cls, name):
        """ Find the meta-data for a module. """

        for module in cls.all_modules:
            if module.name == name:
                return module

        return None

    def webxml_root_element(self, target, context):
        """ Return a 3-tuple of the root element of the WebXML, the contained
        targets for an object name and the name of the WebXML file or (None,
        None, None) if none could be found.
        """

        result = (None, None, None)

        # The cache is keyed on the name of the .webxml file within the root
        # directory.
        key = self.webxml.get_object_webxml_name(target)
        if key is None:
            return result

        # See if we have already handled this file.
        try:
            return self._webxml_cache[key]
        except KeyError:
            pass

        # See if the file exists.
        webxml_path = os.path.join(context.webxml_root, key)
        if os.path.isfile(webxml_path):
            root_el = etree.parse(webxml_path).getroot()
            if root_el is None:
                error("'{}' is not a valid XML file".format(key))
            else:
                result = (root_el, get_targets(root_el), key)
        else:
            if context.verbose:
                progress(
                        "Unable to find a WebXML file containing '{}'".format(
                                target))

        self._webxml_cache[key] = result

        return result


# The module meta-data.
#ModuleMetadata('QAxContainer', webxml='qtactiveqt')
ModuleMetadata('Qt3DAnimation', webxml='qt3d', qt_docs_prefix='qt3danimation-')
ModuleMetadata('Qt3DCore', webxml='qt3d', qt_docs_prefix='qt3dcore-')
ModuleMetadata('Qt3DExtras', webxml='qt3d', qt_docs_prefix='qt3dextras-')
ModuleMetadata('Qt3DInput', webxml='qt3d', qt_docs_prefix='qt3dinput-')
ModuleMetadata('Qt3DLogic', webxml='qt3d', qt_docs_prefix='qt3dlogic-')
ModuleMetadata('Qt3DRender', webxml='qt3d', qt_docs_prefix='qt3drender-')
#ModuleMetadata('QtAndroidExtras', webxml='qtandroidextras')
#ModuleMetadata('QtBluetooth', webxml='qtbluetooth')
ModuleMetadata('QtCharts', webxml='qtcharts')
ModuleMetadata('QtCore', webxml='qtcore')
ModuleMetadata('QtDataVisualization', webxml='qtdatavis3d')
ModuleMetadata('QtDBus', webxml='qtdbus')
ModuleMetadata('QtDesigner', webxml='qtdesigner')
ModuleMetadata('QtGui', webxml='qtgui')
ModuleMetadata('QtHelp', webxml='qthelp')
#ModuleMetadata('QtLocation', webxml='qtlocation')
#ModuleMetadata('QtMacExtras', webxml='qtmacextras')
#ModuleMetadata('QtMultimedia', webxml='qtmultimedia')
#ModuleMetadata('QtMultimediaWidgets', webxml='qtmultimedia')
ModuleMetadata('QtNetwork', webxml='qtnetwork')
ModuleMetadata('QtNetworkAuth', webxml='qtnetworkauth')
#ModuleMetadata('QtNfc', webxml='qtnfc')
ModuleMetadata('QtOpenGL', webxml='qtopengl')
ModuleMetadata('QtOpenGLWidgets', webxml='qtopengl')
#ModuleMetadata('QtPositioning', webxml='qtpositioning')
ModuleMetadata('QtPrintSupport', webxml='qtprintsupport')
#ModuleMetadata('QtPurchasing', webxml='qtpurchasing')
ModuleMetadata('QtQml', webxml='qtqml')
ModuleMetadata('QtQuick', webxml='qtquick')
ModuleMetadata('QtQuick3D', webxml='qtquick3d')
ModuleMetadata('QtQuickWidgets', webxml='qtquick')
#ModuleMetadata('QtRemoteObjects', webxml='qtremoteobjects')
#ModuleMetadata('QtSensors', webxml='qtsensors')
#ModuleMetadata('QtSerialPort', webxml='qtserialport')
ModuleMetadata('QtSql', webxml='qtsql')
ModuleMetadata('QtSvg', webxml='qtsvg')
ModuleMetadata('QtSvgWidgets', webxml='qtsvg')
ModuleMetadata('QtTest', webxml='qttest')
#ModuleMetadata('QtWebChannel', webxml='qtwebchannel')
#ModuleMetadata('QtWebEngine', webxml='qtwebengine')
#ModuleMetadata('QtWebEngineCore', webxml='qtwebengine')
#ModuleMetadata('QtWebEngineWidgets', webxml='qtwebengine')
#ModuleMetadata('QtWebSockets', webxml='qtwebsockets')
ModuleMetadata('QtWidgets', webxml='qtwidgets')
#ModuleMetadata('QtWinExtras', webxml='qtwinextras')
#ModuleMetadata('QtX11Extras', webxml='qtx11extras')
ModuleMetadata('QtXml', webxml='qtxml')
ModuleMetadata('lupdate')
ModuleMetadata('sip')
ModuleMetadata('uic')


class Module:
    """ Encapsulate a documented module. """

    # The list of all modules.
    all_modules = []

    def __init__(self, name, descriptions_dir, verbose):
        """ Initialise the object. """

        self.name = name

        # Get the module's meta-data if it is supported.
        self.metadata = ModuleMetadata.find(name)
        if self.metadata is None:
            warning("unsupported module '{}'".format(name))

        # Introspect the descriptions directory for the individual real API
        # names.
        self.api = {}
        self.descriptions = []

        for desc_name in sorted(os.listdir(descriptions_dir)):
            if not desc_name.endswith('.rst'):
                continue

            desc = Description(os.path.join(descriptions_dir, desc_name), self,
                    verbose)
            self.descriptions.append(desc)

            # Lookups will always find the first overload.
            if desc.real_name not in self.api:
                self.api[desc.real_name] = desc

        # Add this to the list of all modules.
        type(self).all_modules.append(self)

    def resolve_name(self, name, scopes, package):
        """ Return the full package name of a C++ name or None if the name
        wasn't in the API.
        """

        # Assume it will be found in the current module.
        module = self

        # Look in the current module first.
        desc = self.api.get(name)

        if desc is None:
            # Search the scopes.
            for scope in scopes:
                desc = self.api.get(scope + '::' + name)
                if desc is not None:
                    break
            else:
                # Look in the remaining modules.
                for module in type(self).all_modules:
                    if module is not self:
                        desc = module.api.get(name)

                        if desc is not None:
                            break

        if desc is None:
            return None

        prefix = (package + '.') if package else ''

        return '{}{}.{}'.format(prefix, module.name, desc.name)


class Description:
    """ Encapsulate a description file. """

    def __init__(self, desc_path, module, verbose):
        """ Initialise the object. """

        if verbose:
            progress("Reading {}...".format(desc_path))

        with open(desc_path) as desc_fd:
            desc_lines = desc_fd.read().split('\n')

        # The first blank line separates the header from the (optional) body.
        for line_nr, line in enumerate(desc_lines):
            if line.strip() == '':
                break
        else:
            line_nr = len(desc_lines)

        self._header = desc_lines[:line_nr]
        self._body = desc_lines[line_nr + 1:]

        self._desc_path = desc_path
        self._module = module
        self._updated = False

        # Introspect the file name to determine what is being described.
        object_name = os.path.basename(desc_path)[:-4].split('-')

        # Get the type character while discarding any unique identifier.
        self.object_type = object_name.pop()

        try:
            int(self.object_type)
        except ValueError:
            pass
        else:
            self.object_type = object_name.pop()

        self.name = '.'.join(object_name)

        # Get the real name.
        self.real_name = self.get_rst(':realname:')
        if self.real_name is None:
            real_name_parts = object_name
            self.real_name = '::'.join(real_name_parts)
        else:
            real_name_parts = self.real_name.split('::')

        # For dunder names use the corresponding name of the C++ equivalent (if
        # there is one).
        base = real_name_parts[-1]

        if self.object_type == 'f' and base.startswith('__') and base.endswith('__'):
            # TODO: handle all Python slots with a corresponding C++ name.
            if base == '__init__':
                cpp = real_name_parts[-2]
            else:
                cpp = None

            if cpp:
                real_name_parts[-1] = cpp
                self.real_name = '::'.join(real_name_parts)
            else:
                # There is no real equivalent.
                self.real_name = None

        # Get any real signature.
        self.real_sig = self.get_rst(':realsig:')
        if self.real_sig is not None:
            self.real_sig = self.real_sig.replace(' ', '')

        self.inline_images = {}

    def find_webxml(self, context):
        """ Return a 3-tuple of the root element, all targets defined in the
        document, and the name of the WebXML file.
        """

        # Assume the object is in the WebXML file containing the immediate
        # scope.
        if self.object_type == 'c':
            target = self.real_name
        else:
            parts = self.real_name.split('::')

            if self.object_type == 'v':
                del parts[-1]

            if len(parts) > 1:
                del parts[-1]

            target = '::'.join(parts)

        return self._module.metadata.webxml_root_element(target, context)

    def get_rst(self, name):
        """ Return the value of a field or None if it doesn't exist. """

        _, value = self._find_rst(name)

        return value

    def is_todo(self):
        """ Return True if the status is 'todo'. """

        return self.get_rst(':status:') == 'todo'

    def same_signature(self, el):
        """ Return True if the signature in an element matches the one for this
        description.
        """

        # Get the signature.
        real_sig = el.attrib['signature']

        # Get rid of everything up to and including the opening parenthesis.
        real_sig = real_sig[real_sig.find('(') + 1:]

        # Extract any tail.
        closing = real_sig.find(')')
        tail = real_sig[closing + 1:]
        real_sig = real_sig[:closing]

        # Strip out anything that looks like an argument name.
        no_names = []
        if real_sig:
            for arg in real_sig.split(','):
                ptr = arg.find('*')
                ref = arg.find('&')
                end = max(ptr, ref)

                if end >= 0:
                    # Anything after a pointer or reference is a name.
                    arg = arg[:end + 1]
                else:
                    words = arg.split()
                    nr_words = len(words)
                    assert nr_words > 0

                    if nr_words == 1 or (nr_words == 2 and words[0] == 'const'):
                        # There is nothing after the type.
                        pass
                    else:
                        # Remove the name.
                        del words[-1]

                    arg = ' '.join(words)

                no_names.append(arg)

        # Build a 'normalised' real signature.
        real_sig = '({}){}'.format(','.join(no_names), tail).replace(' ', '')

        return real_sig == self.real_sig

    def update_description(self, el, targets, webxml, context, digest=None, description_el=None):
        """ Update the description in an element and update the meta-data
        accordingly.
        """

        # Provide a digest if needed.
        if digest is None:
            digest = Digest()

        # Get the 'description' element if needed.
        if description_el is None:
            description_els = el.findall('./description')
            if len(description_els) != 1:
                error(
                        "exactly one description tag expected for '{}'".format(
                                self.real_name))

            description_el = description_els[0]

        # There are lots of cases where webxml doesn't extract any description
        # at all.  If this is the case then leave without changing anything.
        if len(description_el) == 0:
            return

        self._updated = False

        digest.update_from_element(description_el)
        new_digest = str(digest)

        if new_digest != self.get_rst(':digest:'):
            self.update_rst(':digest:', new_digest)
            force = True
        else:
            force = context.force

        if self.is_todo():
            if force:
                scopes = []

                if self.object_type == 'c':
                    scopes.append(self.real_name)
                else:
                    parts = self.real_name.split('::')
                    del parts[-1]
                    if parts:
                        scopes.append('::'.join(parts))

                        # For enum values also add the enum's scope.
                        if self.object_type == 'v':
                            del parts[-1]
                            if parts:
                                scopes.append('::'.join(parts))

                fmt = Formatter()
                self.render_container(fmt, description_el, scopes, targets,
                        webxml, context)

                # Handle any in-line images.
                leading_blank = True
                for label, image_fn in self.inline_images.items():
                    # TODO: this makes assumptions about the name of the images
                    # directory.
                    fmt.write_line(
                            '.. |{}| image:: ../../../images/{}'.format(label,
                                    os.path.basename(image_fn)),
                            leading_blank=leading_blank)
                    leading_blank = False

                self._body = fmt.lines
                self._updated = True
        else:
            self.update_rst(':status:', 'review')

        if self._updated:
            if context.verbose:
                progress("Updating {}...".format(self._desc_path))

            with open(self._desc_path, 'w') as desc_fd:
                desc_fd.write('\n'.join(self._header))
                desc_fd.write('\n')

                if self._body:
                    desc_fd.write('\n'.join(self._body))
                    desc_fd.write('\n')

    def update_rst(self, name, value):
        """ Update the value of a field. """

        # Find any existing value.
        line_nr, old_value = self._find_rst(name)

        if value:
            # Add a new value or update the existing value.
            if line_nr < 0:
                # Append a new unused line.
                line_nr = len(self._header)
                self._header.append(None)

            self._header[line_nr] = '    {} {}'.format(name, value)
            self._updated = True

        elif line_nr >= 0:
            # Delete the old value.
            del self._header[line_nr]
            self._updated = True

    def _find_rst(self, name):
        """ Return the header line number and value of a field or (-1, None) if
        it doesn't exist.
        """

        for line_nr, line in enumerate(self._header):
            line = line.lstrip()
            if line.startswith(name):
                value = line[len(name):].strip()
                break
        else:
            line_nr, value = -1, None

        return line_nr, value

    def _render_code(self, fmt, code_el):
        """ Render a code element. """

        fmt.write_line('::')
        fmt.indent()

        leading_blank = True
        for line in code_el.text.split('\n'):
            fmt.write_line(line, leading_blank=leading_blank)
            leading_blank = False

        fmt.deindent()

    def render_container(self, fmt, container_el, scopes, targets, webxml, context):
        """ Render a generic container element. """

        for sub_el in container_el:
            if sub_el.tag in ('argument', 'italic'):
                self._render_quoted_text(fmt, sub_el, scopes, targets, webxml,
                        context, '*')

            elif sub_el.tag == 'bold':
                self._render_quoted_text(fmt, sub_el, scopes, targets, webxml,
                        context, '**')

            elif sub_el.tag == 'brief':
                self._render_text(fmt, sub_el, scopes, targets, webxml,
                        context)
                fmt.flush()

            elif sub_el.tag in ('badcode', 'code', 'newcode', 'oldcode'):
                self._render_code(fmt, sub_el)

            elif sub_el.tag in ('codeline', 'dots'):
                # This are specified between snippets (and maybe elswhere).  We
                # just leave them as separate snippets.
                pass

            elif sub_el.tag == 'heading':
                self._render_heading(fmt, sub_el, scopes, targets, webxml,
                        context)

            elif sub_el.tag == 'inlineimage':
                self._render_inline_image(fmt, sub_el, context)

            elif sub_el.tag == 'image':
                self._render_image(fmt, sub_el, context)

            elif sub_el.tag == 'index':
                # This only seems to be used once (maybe it's a bug) and the
                # element text is discarded, so we do the same.
                pass

            elif sub_el.tag == 'legalese':
                fmt.write_line('.. container:: legalese')
                fmt.indent()
                self.render_container(fmt, sub_el, scopes, targets, webxml,
                        context)
                fmt.deindent()

            elif sub_el.tag == 'link':
                self._render_link(fmt, sub_el, scopes, targets, webxml,
                        context)

            elif sub_el.tag == 'list':
                self._render_list(fmt, sub_el, scopes, targets, webxml,
                        context)

            elif sub_el.tag == 'para':
                # Always strip leading whitespace from a paragraph so as not to
                # screw up the indentation.  (All the times this seems to
                # happen can be put down to qdoc bugs.)
                if sub_el.text:
                    sub_el.text = sub_el.text.lstrip()

                self._render_text(fmt, sub_el, scopes, targets, webxml,
                        context)
                fmt.flush()

            elif sub_el.tag == 'quotefile':
                # TODO
                # Include the contents of a file.  At the moment the only known
                # use is in a non-supported class.
                pass

            elif sub_el.tag == 'see-also':
                self._render_see_also(fmt, sub_el, scopes, targets, webxml,
                        context)

            elif sub_el.tag == 'section':
                self.render_container(fmt, sub_el, scopes, targets, webxml,
                        context)

            elif sub_el.tag == 'snippet':
                self._render_snippet(fmt, sub_el, context)

            elif sub_el.tag == 'superscript':
                if fmt.buffer and fmt.buffer[-1] != ' ':
                    fmt.write_inline('\\ ')

                fmt.write_inline(':sup:`{}`'.format(sub_el.text))

            elif sub_el.tag == 'table':
                self._render_table(fmt, sub_el, scopes, targets, webxml,
                        context)

            elif sub_el.tag == 'target':
                # Ignore it if it is a heading.
                name = sub_el.attrib['name']

                try:
                    _, is_heading = targets[name]
                except KeyError:
                    # It must have been a discarded untitled target.
                    is_heading = False

                if not is_heading:
                    self._render_target_name(fmt, name, webxml)

            elif sub_el.tag == 'teletype':
                self._render_text(fmt, sub_el, scopes, targets, webxml,
                        context, quotes='``', escape_backslash=False)

                if sub_el.tail:
                    if sub_el.tail[0].isalpha() or sub_el.tail[0].isnumeric():
                        fmt.write_inline('\\ ')

            elif sub_el.tag == 'underline':
                # TODO
                pass

            elif sub_el.tag in ('quotefromfile', 'skipto', 'printuntil'):
                # These are used to extract text fragments from a file.  The
                # only know use is to extract C++ code from a Qt source file,
                # so we just ignore them.
                pass

            else:
                warning(
                        "{}: unsupported description tag: '{}'".format(webxml,
                                sub_el.tag))

            self._render_text_fragment(fmt, sub_el.tail)

    def _render_definition_list(self, fmt, list_el, scopes, targets, webxml, context):
        """ Render a list element that is a definition list. """

        table = Table()
        table.set_headings(("Constant", "Description"), webxml)

        defs = []
        items = []

        for sub_el in list_el:
            if sub_el.tag == 'definition':
                cell = Formatter()
                cell.write_line(sub_el[0].text.strip())
                defs.append(cell)
            elif sub_el.tag == 'item':
                cell = Formatter()
                self.render_container(cell, sub_el, scopes, targets, webxml,
                        context)
                items.append(cell)
            else:
                warning(
                        "{}: ignoring unexpected tag '{}' in definition list".format(webxml, sub_el.tag))

        for row in zip(defs, items):
            table.rows.append(row)

        table.render(fmt)

    def _render_heading(self, fmt, heading_el, scopes, targets, webxml, context):
        """ Render a heading element. """

        level = heading_el.attrib['level']
        if level == '1':
            under_char = '-'
        elif level == '2':
            under_char = '.'
        elif level == '3':
            under_char = '^'
        else:
            warning(
                    "{}: unsupported section heading level: '{}'".format(
                            webxml, level))

        # If the heading is in the targets then generate a reference to it.  We
        # don't generate a reference for every heading as there can be
        # duplicate headings even in the same file.
        for name, (title, is_heading) in targets.items():
            if heading_el.text == title and is_heading:
                self._render_target_name(fmt, name, webxml)
                break

        self._render_text(fmt, heading_el, scopes, targets, webxml, context)
        fmt.write_line(under_char * len(fmt.buffer), leading_blank=False)

    def _render_inline_image(self, fmt, image_el, context):
        """ Render an in-line image element. """

        href = image_el.attrib['href']
        image_fn = self._copy_image(href, context)
        label = 'image-' + os.path.basename(image_fn).replace('.', '-')

        if label not in self.inline_images:
            self.inline_images[label] = image_fn

        fmt.write_inline('|{}|'.format(label))

    def _render_image(self, fmt, image_el, context):
        """ Render an image element. """

        href = image_el.attrib['href']

        image_fn = self._copy_image(href, context)

        # TODO: this makes assumptions about the name of the images directory.
        fmt.write_line(
                '.. image:: ../../../images/' + os.path.basename(image_fn))

    def _render_link(self, fmt, link_el, scopes, targets, webxml, context):
        """ Render a link element. """

        # The text to render if we can't resolve the link.
        text = link_el.text

        href = link_el.attrib['href']

        link_type = link_el.attrib['type']
        if link_type in ('class', 'enum', 'function', 'module', 'namespace'):
            raw = link_el.attrib['raw']

            # It's not clear why this can have a leading '#'.
            if raw.startswith('#'):
                raw = raw[1:]

            # Remove any parentheses from functions.
            if raw.endswith('()'):
                raw = raw[:-2]

            # The 'enum' link type is used for both enums and enum members.
            # For enum members the raw name doesn't include the enum itself.
            # TODO: what about C++11 scoped enums?
            member = ''
            if link_type == 'enum':
                real_enum_name = link_el.attrib['enum']
                if raw != real_enum_name:
                    # It must be a link to an enum member to get the member
                    # name and the name of the enum.
                    member = '.' + raw.split('::')[-1]
                    raw = real_enum_name

            # Get the fully qualified name.
            if link_type == 'module':
                full_name = raw
                if context.package:
                    full_name = context.package + '.' + full_name
            else:
                if link_type == 'class' and scopes:
                    # A class may refer to itself.  If we simply looked it up
                    # then we would get back it's first ctor rather than the
                    # class itself.  We detect this first and massage things so
                    # that the class is returned.
                    class_scope = scopes[0]
                    if class_scope.split('::')[-1] == raw:
                        raw = class_scope
                        scopes = scopes[1:]

                full_name = self._module.resolve_name(raw, scopes,
                        context.package)

            if full_name is not None:
                text = ':sip:ref:`~{}{}`'.format(full_name, member)

                # Insert an escaped space if necessary.
                if fmt.buffer and fmt.buffer[-1] != ' ':
                    text = '\\ ' + text
                    
            elif '#' in href:
                # Convert the href to a ref.  If it doesn't exist then Sphinx
                # will complain.
                doc, name = href.split('#', maxsplit=1)

                for title, is_heading in targets.values():
                    if title == raw:
                        label = '{}-{}'.format(doc.replace('.html', ''), name)

                        if is_heading:
                            text = ':ref:`{}`'.format(label)
                        else:
                            text = ':ref:`{}<{}>`'.format(text, label)

                        # If the link is embedded in a word then add an escaped
                        # space.
                        if link_el.tail:
                            tail_ch = link_el.tail[0]

                            if tail_ch == '(' or tail_ch.isalpha():
                                text += '\\ '

                        break
            else:
                # TODO: handle mapped types.
                pass

        elif link_type in ('', 'page'):
            # TODO: Look for any WebXML for the page and process it.
            # TODO: Implement :sip:external`` so that the URL isn't hardcoded.
            text = '`{} <https://doc.qt.io/qt-6/{}>`_'.format(text, href)

        elif link_type == 'property':
            # TODO
            pass

        elif link_type == 'alias':
            # TODO
            pass

        elif link_type == 'typedef':
            # TODO
            pass

        elif link_type == 'variable':
            # TODO
            pass

        elif link_type == 'external':
            text = '`{} <{}>`_'.format(text, href)

        else:
            warning(
                    "{}: unsupported link type: '{}'".format(webxml,
                            link_type))

        fmt.write_inline(text)

    def _render_list(self, fmt, list_el, scopes, targets, webxml, context):
        """ Render a list element. """

        list_type = list_el.attrib['type']

        if list_type == 'enum':
            # This is handled elsewhere.
            return

        if list_type == 'definition':
            self._render_definition_list(fmt, list_el, scopes, targets, webxml,
                    context)

            return

        if list_type == 'bullet':
            item_prefix = '*'
        elif list_type == 'ordered':
            if list_el.attrib['start'] != '1':
                warning("ordered lists may only start at 1")

            item_prefix = '#.'
        else:
            warning(
                    "{}: unsupported list type: '{}'".format(webxml,
                            list_type))

            # As good a default as any.
            item_prefix = '*'

        for sub_el in list_el:
            if sub_el.tag == 'item':
                fmt.indent(ListItemIndenter(item_prefix))
                self.render_container(fmt, sub_el, scopes, targets, webxml,
                        context)
                fmt.deindent()
            else:
                warning(
                        "{}: unsupported list tag: '{}'".format(webxml,
                                sub_el.tag))

    def _render_quoted_text(self, fmt, text_el, scopes, targets, webxml, context, quotes):
        """ Render a text element that is implemented by quoting the text. """

        # If it is after the start of a word then prepend an escaped space.
        if fmt.buffer and fmt.buffer[-1] != ' ':
            fmt.write_inline('\\ ')

        self._render_text(fmt, text_el, scopes, targets, webxml, context,
                quotes=quotes)

        # If it is before the end of a word then append an escaped space.
        if text_el.tail:
            tail_ch = text_el.tail[0]
            if tail_ch.isalpha() or tail_ch.isnumeric():
                fmt.write_inline('\\ ')

    def _render_see_also(self, fmt, see_also_el, scopes, targets, webxml, context):
        """ Render a see-also element. """

        fmt.flush()
        fmt.write_inline('.. seealso:: ')

        need_comma = False

        for sub_el in see_also_el:
            # TODO: some links are implemented as simple text (converted to
            # lower case).  Some simple text is actually multiple 'links' run
            # together (ie. no separating space or comma).  Some text is just
            # wrong - it looks like it can be ignored if there are explicit
            # links.
            if sub_el.tag == 'link':
                if need_comma:
                    fmt.write_inline(", ")
                else:
                    need_comma = True

                self._render_link(fmt, sub_el, scopes, targets, webxml,
                        context)
            else:
                warning(
                        "{}: unsupported see-also tag: '{}'".format(webxml,
                                sub_el.tag))

        # The WebXML may be just plain text.
        text = see_also_el.text.strip()
        if text:
            if need_comma:
                fmt.write_inline(", ")

            name = text
            if name.endswith('()'):
                name = name[:-2]

            full_name = self._module.resolve_name(name, scopes,
                    context.package)

            if full_name is not None:
                fmt.write_inline(':sip:ref:`~{}`'.format(full_name))
            else:
                self._render_text_fragment(fmt, text)

        fmt.write_inline(".")
        fmt.flush()

    def _render_snippet(self, fmt, snippet_el, context):
        """ Render a snippet element. """

        # Qt renders consecutive snippets and dots into a single snippet.  We
        # render each snippet separately and ignore any dots - and the same for
        # empty code lines.

        snippet = snippet_el.attrib['path']

        # Snippets can only be uniquely identified by their path relative to
        # the source directory.
        snippet_name = os.path.relpath(snippet,
                os.path.realpath(context.qt_source)).replace(os.sep, '-')

        for ext in ('.cpp', '.h'):
            if snippet_name.endswith(ext):
                snippet_name = snippet_name[:-len(ext)] + '.py'

        snippet_abs_path = os.path.join(context.snippets, snippet_name)

        # Find the start and end of the snippet within the file.
        start_line = end_line = -1

        if not os.path.exists(snippet_abs_path):
            # Copy the C++ code and convert it to Python by turning each line
            # into a comment.
            with open(snippet, 'r') as sf:
                snippet_lines = sf.read().split('\n')

            with open(snippet_abs_path, 'w') as sf:
                sf.write("# This code needs porting to Python.\n\n")

                for line in snippet_lines:
                    if line.strip():
                        line = '# ' + line.replace('//! [', '#! [')

                    sf.write(line + '\n')

        # See if only a section is required.
        ident = snippet_el.attrib.get('identifier')
        if ident:
            ident = '#! [{}]'.format(ident)

            with open(snippet_abs_path, 'r') as sf:
                line_nr = 0
                line = sf.readline()
                while line:
                    if ident in line:
                        if start_line < 0:
                            start_line = line_nr
                        else:
                            end_line = line_nr
                            break

                    line = sf.readline()
                    line_nr += 1

        # TODO: this makes assumptions about the name of the snippets
        # directory.
        fmt.write_line('.. literalinclude:: ../../../snippets/' + snippet_name)

        if end_line >= 0:
            fmt.indent()
            fmt.write_line(':lines: {}-{}'.format(start_line + 2, end_line),
                    leading_blank=False)
            fmt.deindent()

    def _render_table(self, fmt, table_el, scopes, targets, webxml, context):
        """ Render a table element. """

        table = None

        for sub_el in table_el:
            if sub_el.tag == 'header':
                # A table can have multiple headers.  We start a new table if
                # we find a header after the first row.
                if table is not None:
                    table.render(fmt)

                table = Table()

                table.parse_header(sub_el, self, scopes, targets, webxml,
                        context)
            elif sub_el.tag == 'row':
                if table is None:
                    table = Table()

                table.parse_row(sub_el, self, scopes, targets, webxml, context)
            else:
                warning(
                        "{}: unsupported table tag: '{}'".format(webxml,
                                sub_el.tag))

        if table is not None:
            table.render(fmt)

    def _render_target_name(self, fmt, name, webxml):
        """ Render the target of a reference. """

        fmt.write_line(
                '.. _{}-{}:'.format(
                        os.path.basename(webxml).replace('.webxml', ''), name))

    def _render_text(self, fmt, text_el, scopes, targets, webxml, context, quotes='', escape_backslash=True, leading_blank=True):
        """ Render an element that contains text. """

        if quotes:
            fmt.write_inline(quotes, leading_blank=leading_blank)

            if quotes == '"':
                fmt.escape_dquotes = True

        self._render_text_fragment(fmt, text_el.text,
                escape_backslash=escape_backslash, leading_blank=leading_blank)

        # Render any sub-elements.
        self.render_container(fmt, text_el, scopes, targets, webxml, context)

        if quotes:
            if quotes == '"':
                fmt.escape_dquotes = False

            fmt.write_inline(quotes)

    @staticmethod
    def _render_text_fragment(fmt, fragment, escape_backslash=True, leading_blank=True):
        """ Render a fragment of text. """

        if fragment:
            # A text or tail containing only whitespace may be significant text
            # or it may be just insignificant layout.  We assume that a single
            # space is significant.
            if fragment == ' ' or fragment.strip():
                if escape_backslash:
                    fragment = fragment.replace('\\', '\\\\')

                fragment= fragment.replace('*', '\\*')

                # Insert an escaped space if we don't have an alphanumeric
                # after a reference.
                if not fmt.buffer.endswith('``') and fmt.buffer.endswith('`'):
                    frag_ch = fragment[0]
                    if frag_ch.isalpha() or frag_ch.isnumeric() or frag_ch == '(':
                        fmt.write_inline('\\ ', leading_blank=leading_blank)

                fmt.write_inline(fragment, leading_blank=leading_blank)

    def _copy_image(self, href, context):
        """ Copy an image and return its filename. """

        fn = href.replace('/', os.sep)
        dst = os.path.join(context.images, os.path.basename(fn))

        for image_dir in self._module.metadata.webxml.images:
            src = os.path.join(context.qt_source, image_dir, fn)

            if os.path.isfile(src):
                shutil.copyfile(src, dst)
                break
        else:
            error("unable to find image file '{}'".format(fn))

        return dst


class Table:
    """ A table parser and renderer. """

    def __init__(self):
        """ Initialise the object. """

        self.rows = []
        self._has_header = False

    def parse_header(self, header_el, desc, scopes, targets, webxml, context):
        """ Parse a table header element. """

        self.parse_row(header_el, desc, scopes, targets, webxml, context)
        self._has_header = True

    def parse_row(self, row_el, desc, scopes, targets, webxml, context):
        """ Parse a table row element. """

        cells = []

        for sub_el in row_el:
            if sub_el.tag == 'item':
                cell = Formatter()
                desc.render_container(cell, sub_el, scopes, targets, webxml,
                        context)
                cells.append(cell)
            else:
                warning(
                        "{}: unsupported table item tag: '{}'".format(webxml,
                                sub_el.tag))

        self.rows.append(cells)

    def render(self, fmt):
        """ Render a parsed table. """

        # Calculate the width of each column and the height of each row.
        col_widths = []
        row_heights = []

        for row in self.rows:
            row_height = 0

            for col_nr, cell in enumerate(row):
                # See if this is a new column.
                if col_nr >= len(col_widths):
                    col_widths.append(0)

                # See if the size of the cell affects the overall dimenstions.
                for line in cell.lines:
                    width = len(line)

                    if col_widths[col_nr] < width:
                        col_widths[col_nr] = width

                height = len(cell.lines)
                if row_height < height:
                    row_height = height

            row_heights.append(row_height)

        # Render each row.
        sections = ['-' * (w + 2) for w in col_widths]
        row_separator = '+' + '+'.join(sections) + '+'

        fmt.write_line(row_separator)

        for row_nr, row in enumerate(self.rows):
            if row_nr == 0:
                pass
            elif row_nr == 1 and self._has_header:
                fmt.write_line(row_separator.replace('-', '='),
                        leading_blank=False)
            else:
                fmt.write_line(row_separator, leading_blank=False)

            # Render each line of the row.
            for line_nr in range(row_heights[row_nr]):
                sections = []
                line_is_blank = True

                for col_nr in range(len(col_widths)):
                    if col_nr < len(row):
                        try:
                            line = row[col_nr].lines[line_nr]
                        except IndexError:
                            line = ''
                    else:
                        line = ''

                    if line:
                        line_is_blank = False

                    # Pad the line.
                    line += ' ' * (col_widths[col_nr] - len(line))

                    sections.append(' ' + line + ' ')

                # Ignore the first line of a row if it is blank.
                if line_nr > 0 or not line_is_blank:
                    fmt.write_line('|' + '|'.join(sections) + '|',
                            leading_blank=False)

        fmt.write_line(row_separator, leading_blank=False)

    def set_headings(self, headings, webxml):
        """ Set explicit heading for the table. """

        cells = []

        for heading in headings:
            cell = Formatter()
            cell.write_line(heading, leading_blank=False)
            cells.append(cell)

        self.rows.append(cells)

        self._has_header = True


class Digest:
    """ A digest for WebXML content. """

    def __init__(self):
        """ Initialise the object. """

        self._digest = hashlib.new('md5')

    def __str__(self):
        """ Return the hexadecimal value of the digest. """

        return self._digest.hexdigest()

    def update(self, text):
        """ Update the digest with some UTF-8 text. """

        # Remove all whitespace.
        text = text.replace(' ', '').replace('\n', '')

        self._digest.update(text.encode('utf8'))

    def update_from_element(self, el):
        """ Update the digest with the text of an element. """

        if el.text is not None:
            self.update(el.text)

        for sub_el in el:
            self.update_from_element(sub_el)


class FixedIndenter:
    """ The implementation of a indenter that indents by a fixed amount. """

    def indent(self):
        """ Return the indent. """

        return '    '


class ListItemIndenter:
    """ The implementation of a indenter that indents list items. """

    def __init__(self, item_prefix):
        """ Initialise the object. """

        self._item_prefix = item_prefix

    def indent(self):
        """ Return the indent. """

        indent = self._item_prefix + ' '
        self._item_prefix = ' ' * len(self._item_prefix)

        return indent


class Formatter:
    """ A class for formatting output as a list of lines. """

    def __init__(self):
        """ Initialise the object. """

        self._indenters = []

        self.escape_dquotes = False
        self.buffer = ''
        self.lines = []

    def deindent(self):
        """ De-indent subsequent text. """

        self.flush()

        try:
            old_indenter = self._indenters.pop()
        except IndexError:
            old_indenter = None

        return old_indenter

    def flush(self):
        """ Make sure any pending in-line text is added to the body. """

        pending = self.buffer.rstrip()
        self.buffer = ''

        if pending:
            self._write_indented_line(pending)

    def indent(self, indenter=FixedIndenter()):
        """ Indent subsequent text. """

        self.flush()

        if indenter is not None:
            self._indenters.append(indenter)

    def write_inline(self, text, leading_blank=True):
        """ Write some text in-line. """

        # Precede the start of a 'paragraph' with a blank line.
        if leading_blank and not self.buffer:
            self._write_blank_line()

        if self.escape_dquotes:
            text = text.replace('"', '""')

        self.buffer += text

    def write_line(self, text='', leading_blank=True):
        """ Write some text as a single line. """

        self.flush()

        if text:
            if leading_blank:
                self._write_blank_line()

            self._write_indented_line(text)
        else:
            self._write_blank_line()

    def _write_blank_line(self):
        """ Write a blank line. """

        self.lines.append('')

    def _write_indented_line(self, line):
        """ Write an indented line. """

        full_line = ''

        for indenter in self._indenters:
            full_line += indenter.indent()

        full_line += line

        self.lines.append(full_line)


def get_all_modules(descriptions_dir, verbose):
    """ Introspect the description file names to get the complete API on a
    module by module basis.
    """

    for m in sorted(os.listdir(descriptions_dir)):
        Module(m, os.path.join(descriptions_dir, m), verbose)


def get_modules_to_update(requested_modules):
    """ Return the list of supported modules to update. """

    # Validate any list of specifically requested modules.
    if requested_modules:
        for name in requested_modules:
            for module in Module.all_modules:
                if module.name == name:
                    if module.metadata is None:
                        error("'{}' module is unsupported".format(name))

                    break
            else:
                error("unknown module '{}'".format(name))

            modules.append(module)

        return modules

    # Return the list of all supported modules.
    return [m for m in Module.all_modules
            if m.metadata is not None and m.metadata.webxml is not None]


def generate_webxml(modules, qt_prefix, qt_source):
    """ Generate the WebXML for a list of modules and return the root directory
    containing sub-directories for each module.
    """

    # Create the WebXML root directory if it doesn't already exist.
    webxml_root = os.path.abspath('webxml')
    os.makedirs(webxml_root, exist_ok=True)

    # Find all the WebXML modules needed.
    webxml_needed = set()
    for module in modules:
        webxml_needed.add(module.metadata.webxml)

    # Create the master .qdocconf file containing the names of the individual
    # module .qdocconf files.
    master_path = os.path.join(webxml_root, 'master.qdocconf')
    with open(master_path, 'w') as master_f:
        for webxml in webxml_needed:
            qdocconf = webxml.create_qdocconf(webxml_root, qt_prefix,
                    qt_source)
            master_f.write(qdocconf + '\n')

    # Configure the environment.
    versioned_dir = os.path.dirname(qt_prefix)
    qt_version = os.path.basename(versioned_dir)
    qt_install_docs = os.path.join(os.path.dirname(versioned_dir), 'Docs',
            'Qt-' + qt_version)
    os.environ['QT_INSTALL_DOCS'] = qt_install_docs

    # These environment variables need to have values but aren't used.
    os.environ['QT_VERSION'] = '1.0.0'
    os.environ['QT_VER'] = '1.0'
    os.environ['QT_VERSION_TAG'] = '100'
    os.environ['BUILDDIR'] = webxml_root

    # Run qdoc.
    run(os.path.join(qt_prefix, 'bin', 'qdoc'), '--single-exec', '--outputdir',
            webxml_root, master_path)

    return webxml_root


def update_module_descriptions(module, context):
    """ Update the description .rst files for a module. """

    for desc in module.descriptions:
        # Handle each type.
        if desc.object_type == 'a':
            update_attribute(desc, context)
        elif desc.object_type == 'c':
            update_class(desc, context)
        elif desc.object_type in 'fs':
            update_callable(desc, context)
        elif desc.object_type == 'e':
            update_enum(desc, context)
        elif desc.object_type == 'm':
            update_module(desc, context)
        elif desc.object_type == 'v':
            update_enum_member(desc, context)

    module.metadata.clear_cache()


def update_attribute(desc, context):
    """ Update, if necessary, the description file for an attribute. """

    root_el, targets, webxml = desc.find_webxml(context)
    if root_el is None:
        return

    # Look for class attributes.
    for el in root_el.findall(".//variable"):
        if el.attrib.get('fullname') == desc.real_name:
            desc.update_description(el, targets, webxml, context)
            return

    # Look for macros.
    for el in root_el.findall(".//function[@meta='macrowithoutparams']"):
        if el.attrib.get('name') == desc.real_name:
            desc.update_description(el, targets, webxml, context)
            return


def update_callable(desc, context):
    """ Update, if necessary, the description file for a callable. """

    # Ignore if there is no C++ equivallent.
    if desc.real_name is None:
        return

    root_el, targets, webxml = desc.find_webxml(context)
    if root_el is None:
        return

    for el in root_el.findall(".//function"):
        # Global callables don't have a full name.
        name = el.attrib.get('fullname')
        if name is None:
            name = el.attrib.get('name')

        if name == desc.real_name:
            # Macros with arguments don't have complete signatures.
            if el.attrib.get('meta') == 'macrowithparams':
                break

            if desc.real_sig is not None and desc.same_signature(el):
                break
    else:
        return

    desc.update_description(el, targets, webxml, context)


def update_class(desc, context):
    """ Update, if necessary, the description file for a class. """

    root_el, targets, webxml = desc.find_webxml(context)
    if root_el is None:
        return

    for el in root_el.findall(".//class"):
        # Global classes don't have a full name.
        name = el.attrib.get('fullname')
        if name is None:
            name = el.attrib.get('name')

        if name == desc.real_name:
            break
    else:
        return

    # Get the 'brief' attribute (which is usually a shorter version of the
    # 'brief' element of the 'description' element).
    digest = Digest()
    brief = el.attrib.get('brief')

    if brief is not None:
        digest.update(brief)

        if desc.is_todo():
            desc.update_rst(':brief:', brief)

    desc.update_description(el, targets, webxml, context, digest=digest)

    # Update the reference to the original docs.
    desc.update_rst(':external:', el.attrib.get('href'))


def update_enum(desc, context):
    """ Update, if necessary, the description file for an enum. """

    root_el, targets, webxml = desc.find_webxml(context)
    if root_el is None:
        return

    for el in root_el.findall(".//enum"):
        # Global enums don't have a full name.
        name = el.attrib.get('fullname')
        if name is None:
            name = el.attrib.get('name')

        if name == desc.real_name:
            break
    else:
        return

    desc.update_description(el, targets, webxml, context)


def update_enum_member(desc, context):
    """ Update, if necessary, the description file for an enum member. """

    root_el, targets, webxml = desc.find_webxml(context)
    if root_el is None:
        return

    # Get the component parts of the real name.
    parts = desc.real_name.split('::')
    member_real_name = parts.pop()
    enum_real_name = '::'.join(parts)

    # Find the enum element.
    for el in root_el.findall(".//enum"):
        # Global enums don't have a full name.
        name = el.attrib.get('fullname')
        if name is None:
            name = el.attrib.get('name')

        if name == enum_real_name:
            break
    else:
        return

    # Update the value.
    if desc.is_todo():
        for value_el in el.findall("./value[@name='{}']".format(member_real_name)):
            desc.update_rst(':value:', value_el.attrib['value'])
            break

    # Find the correct definition/item pair in the enum list.
    for list_el in el.findall(".//list[@type='enum']"):
        use_next_item = False

        for sub_el in list_el:
            if sub_el.tag == 'definition' and sub_el[0].tail == member_real_name:
                # The next 'item' tag is the one we want.
                use_next_item = True
            elif sub_el.tag == 'item' and use_next_item:
                desc.update_description(el, targets, webxml, context,
                        description_el=sub_el)
                break


def update_module(desc, context):
    """ Update, if necessary, the description file for a module. """

    # TODO


def get_targets(root_el):
    """ Get the targets defined in a root element. """

    targets = {}

    for sub_el in root_el.findall('./document//contents'):
        name = sub_el.attrib['name']

        # It's possible for a heading to appear more than once.  We choose to
        # use the first appearence.
        if name not in targets:
            title = sub_el.attrib['title']
            targets[name] = (title, True)

    for sub_el in root_el.findall('./document//target'):
        name = sub_el.attrib['name']
        title = sub_el.attrib.get('title')

        # Ignore targets with no titles as they also seem to have contents
        # elements as well.
        if title:
            targets[name] = (title, False)

    return targets


def run(*args):
    """ Run an external command. """

    progress("Running {}...".format(' '.join(args)))

    try:
        subprocess.run(args, stderr=subprocess.PIPE, check=True,
                universal_newlines=True)
    except subprocess.CalledProcessError as e:
        error(e.stderr)


if __name__ == '__main__':

    # Parse the command line.
    import argparse

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument('--descriptions', metavar='DIR',
            default='descriptions',
            help="the name of the directory where the module's description .rst files can be found")

    arg_parser.add_argument('--force', action='store_true', default=False,
            help="re-write the reST for unchanged Qt sources")

    arg_parser.add_argument('--images', metavar='DIR',
            default='images',
            help="the name of the directory where any images can be found")

    arg_parser.add_argument('--package', metavar='NAME', default='',
            help="the name of the optional top-level package")

    arg_parser.add_argument('--qt-prefix', metavar='DIR', required=True,
            help="the name of the Qt prefix directory")

    arg_parser.add_argument('--snippets', metavar='DIR',
            default='snippets',
            help="the name of the directory where any code snippets can be found")

    arg_parser.add_argument('--verbose', action='store_true', default=False,
               help="enable verbose progress messages")

    arg_parser.add_argument('modules', metavar='module',
            nargs=argparse.REMAINDER,
            help="the name of a module within the top-level package")

    args = arg_parser.parse_args()

    # Regularise the arguments.
    descriptions = os.path.abspath(args.descriptions)
    force = args.force
    images = os.path.abspath(args.images)
    qt_prefix = os.path.abspath(args.qt_prefix)
    package = args.package
    snippets = os.path.abspath(args.snippets)
    verbose = args.verbose

    qt_source = os.path.join(os.path.dirname(qt_prefix), 'Src')

    # Make sure the images and snippets directories exist.
    os.makedirs(images, exist_ok=True)
    os.makedirs(snippets, exist_ok=True)

    # Get the API of all modules.
    get_all_modules(descriptions, verbose)

    # Get the list of modules to update.
    modules = get_modules_to_update(args.modules)

    # Generate the WebXML for the modules.
    webxml_root = generate_webxml(modules, qt_prefix, qt_source)

    # The context is a collection of unrelated global read-only values.
    Context = namedtuple('Context',
            ('force', 'images', 'package', 'qt_source', 'snippets', 'verbose',
                    'webxml_root'))
    context = Context(force=force, images=images, package=package,
            qt_source=qt_source, snippets=snippets, verbose=verbose,
            webxml_root=webxml_root)

    # Update the descriptions for each module.
    for module in modules:
        update_module_descriptions(module, context)
