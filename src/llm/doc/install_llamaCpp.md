1. created conda env with python 3.13
2. install gcc, which was already installed
3. run command to install llama_cpp pckg: pip install llama-cpp-python -v
reference: https://llama-cpp-python.readthedocs.io/en/latest/


what I tried and failed to install llamacpp
- unable to install with python=3.10.14, faced following error.
```
[84/84] : && /usr/bin/g++  -pthread -B /home/user/miniconda3/envs/llamacpp-test/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-mtmd-cli  -Wl,-rpath,/tmp/tmpbgthcjyn/build/vendor/llama.cpp/tools/mtmd:/tmp/tmpbgthcjyn/build/bin:  vendor/llama.cpp/common/libcommon.a  vendor/llama.cpp/tools/mtmd/libmtmd.so  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
  FAILED: [code=1] vendor/llama.cpp/tools/mtmd/llama-mtmd-cli
  : && /usr/bin/g++  -pthread -B /home/user/miniconda3/envs/llamacpp-test/compiler_compat -O3 -DNDEBUG  vendor/llama.cpp/tools/mtmd/CMakeFiles/llama-mtmd-cli.dir/mtmd-cli.cpp.o -o vendor/llama.cpp/tools/mtmd/llama-mtmd-cli  -Wl,-rpath,/tmp/tmpbgthcjyn/build/vendor/llama.cpp/tools/mtmd:/tmp/tmpbgthcjyn/build/bin:  vendor/llama.cpp/common/libcommon.a  vendor/llama.cpp/tools/mtmd/libmtmd.so  bin/libllama.so  bin/libggml.so  bin/libggml-cpu.so  bin/libggml-base.so && :
  /home/user/miniconda3/envs/llamacpp-test/compiler_compat/ld: warning: libgomp.so.1, needed by bin/libggml-cpu.so, not found (try using -rpath or -rpath-link)
  /home/user/miniconda3/envs/llamacpp-test/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_barrier@GOMP_1.0'
  /home/user/miniconda3/envs/llamacpp-test/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_parallel@GOMP_4.0'
  /home/user/miniconda3/envs/llamacpp-test/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_thread_num@OMP_1.0'
  /home/user/miniconda3/envs/llamacpp-test/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `GOMP_single_start@GOMP_1.0'
  /home/user/miniconda3/envs/llamacpp-test/compiler_compat/ld: bin/libggml-cpu.so: undefined reference to `omp_get_num_threads@OMP_1.0'
  collect2: error: ld returned 1 exit status
  ninja: build stopped: subcommand failed.


  *** CMake build failed
  error: subprocess-exited-with-error
  
  × Building wheel for llama-cpp-python (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> See above for output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  full command: /home/user/miniconda3/envs/llamacpp-test/bin/python3.10 /home/user/miniconda3/envs/llamacpp-test/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py build_wheel /tmp/tmpzxinuc94
  cwd: /tmp/pip-install-z48mw3__/llama-cpp-python_aab24d2b0a4d433da0ae3ed403de83a5
  Building wheel for llama-cpp-python (pyproject.toml) ... error
  ERROR: Failed building wheel for llama-cpp-python
Failed to build llama-cpp-python
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects

```
- unable to install by passing cmake argument like OpenBLAS etc





new updated, also added here: https://github.com/abetlen/llama-cpp-python/issues/2036

pip install https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.2/llama_cpp_python-0.3.2-cp311-cp311-linux_x86_64.whl
sudo apt install musl-dev
sudo ln -s /usr/lib/x86_64-linux-musl/libc.so /lib/libc.musl-x86_64.so.1


