# opengl-3d-visualizer

Repository for a work of the discipline: Graphic Computation

<img src="./socket.jpeg"/>

# How to compile and execute

Softwares used in this project:

- Qt Creator 4.13.3
- Qt 5.15.2
- GCC 5.3.1 20160406 (Red Hat 5.3.1-6) 64 bit
- CMake 3.19.0
- QMake 3.1

Compiling and running on Linux:
```
qmake openglvisualization.pro
make
./openglvisualization
```

Maybe you can find qmake on Linux through this command `sudo find / -name "qmake" -type f`

In my case, qmake is at `$HOME/Qt/5.15.2/gcc_64/bin/qmake`

You will use the same commands on Windows. To find qmake on Windows, go to your Qt installation folder and run `dir /s qmake.exe` or `dir /s qmake` for CMD or `ls -r qmake` or `ls -r qmake.exe` for PowerShell
