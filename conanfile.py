from conans import ConanFile

class test(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "qmake"
    requires = "qt/5.15.2"
    build_policy = "missing"

    def configure(self):
        if self.settings.os == "Windows":
            self.options["libcurl"].with_winssl = True
            self.options["libcurl"].with_openssl = False
