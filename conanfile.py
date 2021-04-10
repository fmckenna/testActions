from conans import ConanFile

class test(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "qmake"
    requires = "qt/5.15.2"
    build_policy = "missing"

    def configure(self):
            self.options["qt"].qt3d = True
            self.options["qt"].qtcharts = True
            self.options["qt"].qttools = True            
