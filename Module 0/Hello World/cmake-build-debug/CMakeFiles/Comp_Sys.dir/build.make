# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /snap/clion/124/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /snap/clion/124/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/reptar/Documents/Comp-Sys

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/reptar/Documents/Comp-Sys/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Comp_Sys.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Comp_Sys.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Comp_Sys.dir/flags.make

CMakeFiles/Comp_Sys.dir/simple_c_program.c.o: CMakeFiles/Comp_Sys.dir/flags.make
CMakeFiles/Comp_Sys.dir/simple_c_program.c.o: ../simple_c_program.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/reptar/Documents/Comp-Sys/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Comp_Sys.dir/simple_c_program.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Comp_Sys.dir/simple_c_program.c.o   -c /home/reptar/Documents/Comp-Sys/simple_c_program.c

CMakeFiles/Comp_Sys.dir/simple_c_program.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Comp_Sys.dir/simple_c_program.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/reptar/Documents/Comp-Sys/simple_c_program.c > CMakeFiles/Comp_Sys.dir/simple_c_program.c.i

CMakeFiles/Comp_Sys.dir/simple_c_program.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Comp_Sys.dir/simple_c_program.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/reptar/Documents/Comp-Sys/simple_c_program.c -o CMakeFiles/Comp_Sys.dir/simple_c_program.c.s

# Object files for target Comp_Sys
Comp_Sys_OBJECTS = \
"CMakeFiles/Comp_Sys.dir/simple_c_program.c.o"

# External object files for target Comp_Sys
Comp_Sys_EXTERNAL_OBJECTS =

Comp_Sys: CMakeFiles/Comp_Sys.dir/simple_c_program.c.o
Comp_Sys: CMakeFiles/Comp_Sys.dir/build.make
Comp_Sys: CMakeFiles/Comp_Sys.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/reptar/Documents/Comp-Sys/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Comp_Sys"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Comp_Sys.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Comp_Sys.dir/build: Comp_Sys

.PHONY : CMakeFiles/Comp_Sys.dir/build

CMakeFiles/Comp_Sys.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Comp_Sys.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Comp_Sys.dir/clean

CMakeFiles/Comp_Sys.dir/depend:
	cd /home/reptar/Documents/Comp-Sys/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/reptar/Documents/Comp-Sys /home/reptar/Documents/Comp-Sys /home/reptar/Documents/Comp-Sys/cmake-build-debug /home/reptar/Documents/Comp-Sys/cmake-build-debug /home/reptar/Documents/Comp-Sys/cmake-build-debug/CMakeFiles/Comp_Sys.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Comp_Sys.dir/depend

