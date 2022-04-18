from conans import ConanFile, Meson, tools
import os 

required_conan_version = ">=1.33.0"

class GlibmmConan(ConanFile):
    name = "glibmm"
    version = "2.72.0"
    description = "The GLibmm package is a set of C++ bindings for GLib"
    topics = ("giolibmm", "gobject")
    license = "MIT"
    generators = "pkg_config"
    
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    exports_sources = ["Findglibmm.cmake", "CMakeLists.txt"]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("libsigcpp/3.0.0")
        self.requires("glib/2.71.2")

    def build_requirements(self):
        self.build_requires("meson/0.61.2")
        self.build_requires("pkgconf/1.7.4")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True, destination=self._source_subfolder)

    def _configure_meson(self):
        meson = Meson(self)
        meson.configure(
            source_folder=self._source_subfolder,
            args=["--wrap-mode=nofallback"],
            build_folder=self._build_subfolder
        )
        return meson 

    def build(self):
        meson = self._configure_meson()
        meson.build() 

    def package_info(self):
        self.cpp_info.components["glibmm-2.0"].libs = ["glibmm"]
        self.cpp_info.components["glibmm-2.0"].requires.append("libsigcpp::libsigcpp")
        self.cpp_info.components["glibmm-2.0"].requires.append("glib::glib")
        self.cpp_info.components["glibmm-2.0"].includedirs.append(
            os.path.join("lib" "glibmm-2.0", "include")
        )

        self.cpp_info.components["giomm-2.0"].libs = ["giomm"]
        self.cpp_info.components["giomm-2.0"].includedirs.append(
            os.path.join("lib" "giomm-2.0", "include")
        )

        self.cpp_info.components["glibmm-2.0"].resdirs = ['share']

    def package(self):
        #self.copy(pattern="COPYING", dst="licenses", src=self._source_subfolder)
        self.copy("Findglibmm.cmake", ".", ".")
        self.copy("CMakeLists.txt", ".", ".")
        meson = self._configure_meson()
        meson.install()

