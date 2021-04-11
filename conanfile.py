from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def requirements(self):
        #self.requires("openssl/1.1.1j")
        #self.requires("qt/5.15.2@bincrafters/stable")
        #self.requires("qt/6.0.1@bincrafters/stable")
        self.requires("qt/5.15.2")
