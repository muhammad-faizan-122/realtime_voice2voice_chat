# PyAudio Installation issues and Fixes
## issues
Any version of PyAudio is not compatible for python version > 3.11. When I try to install pyaudio in conda env with python=3.13 using following command, faced following error
command: 
```
conda install PyAudio
```
Error:
```
Could not solve for environment specs
The following packages are incompatible
├─ pin-1 is installable and it requires
│  └─ python 3.13.* , which can be installed;
└─ pyaudio is not installable because there are no viable options
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=2.7,<2.8.0a0 , which conflicts with any installable versions previously reported;
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=3.10,<3.11.0a0 , which conflicts with any installable versions previously reported;
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=3.11,<3.12.0a0 , which conflicts with any installable versions previously reported;
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=3.5,<3.6.0a0 , which conflicts with any installable versions previously reported;
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=3.6,<3.7.0a0 , which conflicts with any installable versions previously reported;
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=3.7,<3.8.0a0 , which conflicts with any installable versions previously reported;
   ├─ pyaudio 0.2.11 would require
   │  └─ python >=3.8,<3.9.0a0 , which conflicts with any installable versions previously reported;
   └─ pyaudio 0.2.11 would require
      └─ python >=3.9,<3.10.0a0 , which conflicts with any installable versions previously reported.


```
## How to resolve it:

Used the miniconda for creating virtual environment.
python version = 3.11
Installation step
```
pip install PyAudio
```
if faced following error:
```
ImportError: /home/muhammad-faizan/miniconda3/envs/voice_agent/lib/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by /lib/x86_64-linux-gnu/libjack.so.0)

```


run following command
```
conda install -c conda-forge libstdcxx-ng
```