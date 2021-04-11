cmake_minimum_required(VERSION 3.19)

project(helloqt VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET 10.9)

    set(conan_args -s os.version=${CMAKE_OSX_DEPLOYMENT_TARGET} -s compiler.version=12.0 -o qt:shared=False -o qt:with_mysql=False)

    #set(conan_args -s os.version=${CMAKE_OSX_DEPLOYMENT_TARGET} -s compiler.version=12.0 -o qt:shared=False -o qt:openssl=False -o qt:with_pcre2=False -o qt:with_glib=False -o qt:with_freetype=False -o qt:with_harfbuzz=False -o qt:with_libjpeg=False -o qt:with_libpng=False -o qt:with_sqlite3=False -o qt:with_mysql=False -o qt:with_pq=False -o qt:with_odbc=False -o qt:with_libalsa=False -o qt:with_openal=False)
elseif(UNIX)
    set(conan_args -s compiler=gcc -s compiler.version=10 -s compiler.libcxx=libstdc++11)
elseif(WIN32)
    set(conan_args -s arch=x86 -s compiler.version=16 -s compiler.runtime=MT)
endif()

execute_process(
    COMMAND conan remote add public-conan https://api.bintray.com/conan/bincrafters/public-conan --insert --force
    COMMAND conan install --install-folder ${CMAKE_BINARY_DIR} --update ${CMAKE_SOURCE_DIR} --build=missing ${conan_args}
    RESULT_VARIABLE conan_result
)
if(conan_result)
    message(FATAL_ERROR "Conan error")
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 COMPONENTS Core REQUIRED)

add_executable(helloqt)

target_sources(helloqt PRIVATE
    hello.cpp
)

target_link_libraries(helloqt
    CONAN_PKG::qt
)
