find_path(GLIB_INCLUDE_DIR NAMES glib.h PATHS ${CONAN_INCLUDE_DIRS_GLIB})
find_library(GLIB_LIBRARY NAMES ${CONAN_LIBS_GLIB} PATHS ${CONAN_LIB_DIRS_GLIB})

set(GLIB_FOUND TRUE)
set(GLIB_INCLUDE_DIRS ${GLIB_INCLUDE_DIR})
set(GLIB_LIBRARIES ${GLIB_LIBRARY})
mark_as_advanced(GLIB_LIBRARY GLIB_INCLUDE_DIR)