@echo off

del /F /S /Q build
rmdir /S /Q build
del /F /S /Q dist
rmdir /S /Q dist

del /F /S /Q purge_line_generator.egg-info
rmdir /S /Q purge_line_generator.egg-info
del /F /S /Q purge_line_generator.egg
