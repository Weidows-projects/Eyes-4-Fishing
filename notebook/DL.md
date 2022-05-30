---
title: 👩‍❤️‍💋‍👨Code-4-Deep-Learning
password: ""
tags:
  - 人工智能
  - 深度学习
  - python
katex: false
comments: true
aside: true
date: 2022-04-21 00:26:11
cover: https://www.helloimg.com/images/2022/04/21/RHe8xK.png
top_img:
---

<!--
 * @?: *********************************************************************
 * @Author: Weidows
 * @LastEditors: Weidows
 * @LastEditTime: 2022-04-20 23:11:24
 * @FilePath: \Blog-private\scaffolds\post.md
 * @Description:
 * @!: *********************************************************************
-->

## 序

此文为其他文章的代码部分:

> [⚡再啃-Deep-Learning](../../../python/AI/DL)

也提供了 notebook 形式: [代码地址](https://github.com/Weidows-projects/public-post/blob/main/notebook/DL/DL.ipynb)

<a>![分割线](https://fastly.jsdelivr.net/gh/Weidows/Images/img/divider.png)</a>


## 神经网络

### 感知器



```python
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


# 非门只取一个输入,另一个不管
def NOT(x1, x2):
    w1, w2, theta = -1, 0, 0
    tmp = x1 * w1 + x2 * w2 + 1
    return tmp


# 异或门是非线性运算, 需要多层感知器组合
def XOR(x1, x2):
    # 异或门 = (与非门 与 或门)
    return AND(OR(x1, x2), not AND(x1, x2))


print(AND(0, 1), AND(1, 1), OR(0, 1), OR(0, 0))
print(NOT(0, 1), NOT(1, 1), NOT(0, 0), NOT(1, 0))
print(XOR(0, 1), XOR(1, 1), XOR(0, 0), XOR(1, 0))

```

    0 1 1 0
    1 0 1 0
    1 0 0 1
    

## OpenMMLab

### MMDetection

#### 装环境

从安装到放弃 ( <sup id='cite_ref-1'>[\[1\]](#cite_note-1)</sup>

> 跟着这篇装的环境:<sup id='cite_ref-2'>[\[2\]](#cite_note-2)</sup>, 官方 document 并不是很全面: <sup id='cite_ref-3'>[\[3\]](#cite_note-3)</sup>



```python
!conda create -n openmmlab -y
!conda activate openmmlab
# !conda init
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    
    ==> WARNING: A newer version of conda exists. <==
      current version: 4.12.0
      latest version: 4.13.0
    
    Please update conda by running
    
        $ conda update -n base -c defaults conda
    
    
    
    ## Package Plan ##
    
      environment location: /home/codespace/.conda/envs/openmmlab
    
    
    
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate openmmlab
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate
    
    
    CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
    To initialize your shell, run
    
        $ conda init <SHELL_NAME>
    
    Currently supported shells are:
      - bash
      - fish
      - tcsh
      - xonsh
      - zsh
      - powershell
    
    See 'conda init --help' for more information and options.
    
    IMPORTANT: You may need to close and restart your shell after running 'conda init'.
    
    
    


```python
!python -m pip install --upgrade pip

# 注意对应机子配置: https://pytorch.org/
!pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

# 歇逼了, 官方没给windows平台的wheel,不装了上云吧...
%pip install mmcv
```

    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mRequirement already satisfied: pip in /opt/python/3.10.4/lib/python3.10/site-packages (22.1.1)
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mLooking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cpu
    Requirement already satisfied: torch in /opt/python/3.10.4/lib/python3.10/site-packages (1.11.0)
    Requirement already satisfied: torchvision in /opt/python/3.10.4/lib/python3.10/site-packages (0.12.0+cpu)
    Requirement already satisfied: torchaudio in /opt/python/3.10.4/lib/python3.10/site-packages (0.11.0+cpu)
    Requirement already satisfied: typing-extensions in /opt/python/3.10.4/lib/python3.10/site-packages (from torch) (4.2.0)
    Requirement already satisfied: requests in /opt/python/3.10.4/lib/python3.10/site-packages (from torchvision) (2.27.1)
    Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /opt/python/3.10.4/lib/python3.10/site-packages (from torchvision) (9.1.0)
    Requirement already satisfied: numpy in /opt/python/3.10.4/lib/python3.10/site-packages (from torchvision) (1.22.3)
    Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->torchvision) (2.0.12)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->torchvision) (2021.10.8)
    Requirement already satisfied: idna<4,>=2.5 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->torchvision) (3.3)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->torchvision) (1.26.9)
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mRequirement already satisfied: mmcv in /opt/python/3.10.4/lib/python3.10/site-packages (1.5.1)
    Requirement already satisfied: yapf in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (0.32.0)
    Requirement already satisfied: pyyaml in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (6.0)
    Requirement already satisfied: packaging in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (21.3)
    Requirement already satisfied: opencv-python>=3 in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (4.5.5.64)
    Requirement already satisfied: numpy in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (1.22.3)
    Requirement already satisfied: addict in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (2.4.0)
    Requirement already satisfied: Pillow in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv) (9.1.0)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /opt/python/3.10.4/lib/python3.10/site-packages (from packaging->mmcv) (3.0.9)
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mNote: you may need to restart the kernel to use updated packages.
    


```python
# 与pip/conda同级的专门给mm-lab用的包管理器
%pip install openmim

# 依赖 mmcv, 此处安装一直有问题, 采用手动安装
!mim install mmdet
```

    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mCollecting openmim
      Downloading openmim-0.1.5.tar.gz (35 kB)
      Preparing metadata (setup.py) ... [?25ldone
    [?25hCollecting Click==7.1.2
      Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m82.8/82.8 kB[0m [31m4.5 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting colorama
      Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
    Requirement already satisfied: requests in /opt/python/3.10.4/lib/python3.10/site-packages (from openmim) (2.27.1)
    Collecting model-index
      Downloading model_index-0.1.11-py3-none-any.whl (34 kB)
    Requirement already satisfied: pandas in /opt/python/3.10.4/lib/python3.10/site-packages (from openmim) (1.4.2)
    Collecting tabulate
      Downloading tabulate-0.8.9-py3-none-any.whl (25 kB)
    Requirement already satisfied: pyyaml in /opt/python/3.10.4/lib/python3.10/site-packages (from model-index->openmim) (6.0)
    Requirement already satisfied: markdown in /opt/python/3.10.4/lib/python3.10/site-packages (from model-index->openmim) (3.3.7)
    Collecting ordered-set
      Downloading ordered_set-4.1.0-py3-none-any.whl (7.6 kB)
    Requirement already satisfied: numpy>=1.21.0 in /opt/python/3.10.4/lib/python3.10/site-packages (from pandas->openmim) (1.22.3)
    Requirement already satisfied: python-dateutil>=2.8.1 in /opt/python/3.10.4/lib/python3.10/site-packages (from pandas->openmim) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /opt/python/3.10.4/lib/python3.10/site-packages (from pandas->openmim) (2022.1)
    Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->openmim) (2.0.12)
    Requirement already satisfied: certifi>=2017.4.17 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->openmim) (2021.10.8)
    Requirement already satisfied: idna<4,>=2.5 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->openmim) (3.3)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/python/3.10.4/lib/python3.10/site-packages (from requests->openmim) (1.26.9)
    Requirement already satisfied: six>=1.5 in /opt/python/3.10.4/lib/python3.10/site-packages (from python-dateutil>=2.8.1->pandas->openmim) (1.16.0)
    Building wheels for collected packages: openmim
      Building wheel for openmim (setup.py) ... [?25ldone
    [?25h  Created wheel for openmim: filename=openmim-0.1.5-py2.py3-none-any.whl size=42497 sha256=1a734c6bfea67878c617ae3d0f7e2604ee6008ed447ff7b05c1900191d0db9a4
      Stored in directory: /home/codespace/.cache/pip/wheels/33/51/69/7d124df565cadec731be86337a2e147e024e8eba8fab493182
    Successfully built openmim
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mInstalling collected packages: tabulate, ordered-set, colorama, Click, model-index, openmim
    [33m  WARNING: The script tabulate is installed in '/opt/python/3.10.4/bin' which is not on PATH.
      Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.[0m[33m
    [0m[33m  WARNING: The script mi is installed in '/opt/python/3.10.4/bin' which is not on PATH.
      Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.[0m[33m
    [0m[33m  WARNING: The script mim is installed in '/opt/python/3.10.4/bin' which is not on PATH.
      Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mSuccessfully installed Click-7.1.2 colorama-0.4.4 model-index-0.1.11 openmim-0.1.5 ordered-set-4.1.0 tabulate-0.8.9
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mNote: you may need to restart the kernel to use updated packages.
    /opt/python/3.10.4/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils.
      warnings.warn("Setuptools is replacing distutils.")
    installing mmdet from https://github.com/open-mmlab/mmdetection.git.
    Cloning into '/tmp/tmpsryfhtxk/mmdetection'...
    remote: Enumerating objects: 24862, done.[K
    remote: Counting objects: 100% (62/62), done.[K
    remote: Compressing objects: 100% (59/59), done.[K
    remote: Total 24862 (delta 13), reused 19 (delta 3), pack-reused 24800[K
    Receiving objects: 100% (24862/24862), 37.75 MiB | 16.56 MiB/s, done.
    Resolving deltas: 100% (17403/17403), done.
    Note: switching to '73b4e65a6a30435ef6a35f405e3474a4d9cfb234'.
    
    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by switching back to a branch.
    
    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -c with the switch command. Example:
    
      git switch -c <new-branch-name>
    
    Or undo this operation with:
    
      git switch -
    
    Turn off this advice by setting config variable advice.detachedHead to false
    
    [32minstalling dependency: mmcv-full[0m
    installing mmcv-full from wheel.
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mLooking in links: https://download.openmmlab.com/mmcv/dist/cpu/torch1.11.0/index.html
    Collecting mmcv-full==1.5.1
      Downloading https://download.openmmlab.com/mmcv/dist/cpu/torch1.11.0/mmcv_full-1.5.1-cp310-cp310-manylinux1_x86_64.whl (21.4 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m21.4/21.4 MB[0m [31m8.3 MB/s[0m eta [36m0:00:00[0m00:01[0mm0:01[0mm
    [?25hRequirement already satisfied: yapf in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (0.32.0)
    Requirement already satisfied: packaging in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (21.3)
    Requirement already satisfied: numpy in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (1.22.3)
    Requirement already satisfied: pyyaml in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (6.0)
    Requirement already satisfied: Pillow in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (9.1.0)
    Requirement already satisfied: addict in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (2.4.0)
    Requirement already satisfied: opencv-python>=3 in /opt/python/3.10.4/lib/python3.10/site-packages (from mmcv-full==1.5.1) (4.5.5.64)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /opt/python/3.10.4/lib/python3.10/site-packages (from packaging->mmcv-full==1.5.1) (3.0.9)
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mInstalling collected packages: mmcv-full
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mSuccessfully installed mmcv-full-1.5.1
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[32mSuccessfully installed mmcv-full.[0m
    [32mSuccessfully installed dependencies.[0m
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mCollecting cython
      Downloading Cython-0.29.30-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (1.9 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.9/1.9 MB[0m [31m39.4 MB/s[0m eta [36m0:00:00[0m:00:01[0m
    [?25hRequirement already satisfied: numpy in /opt/python/3.10.4/lib/python3.10/site-packages (from -r /tmp/tmpsryfhtxk/mmdetection/requirements/build.txt (line 3)) (1.22.3)
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mInstalling collected packages: cython
    [33m  WARNING: The scripts cygdb, cython and cythonize are installed in '/opt/python/3.10.4/bin' which is not on PATH.
      Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0mSuccessfully installed cython-0.29.30
    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m
    Usage:   
      /opt/python/latest/bin/python -m pip install [options] <requirement specifier> [package-index-options] ...
      /opt/python/latest/bin/python -m pip install [options] -r <requirements file> [package-index-options] ...
      /opt/python/latest/bin/python -m pip install [options] [-e] <vcs project url> ...
      /opt/python/latest/bin/python -m pip install [options] [-e] <local project path> ...
      /opt/python/latest/bin/python -m pip install [options] <archive url/path> ...
    
    option --use-feature: invalid choice: 'in-tree-build' (choose from '2020-resolver', 'fast-deps')
    Traceback (most recent call last):
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/utils/utils.py", line 418, in call_command
        subprocess.check_call(cmd)
      File "/opt/python/3.10.4/lib/python3.10/subprocess.py", line 369, in check_call
        raise CalledProcessError(retcode, cmd)
    subprocess.CalledProcessError: Command '['python', '-m', 'pip', 'install', '--use-feature=in-tree-build', '/tmp/tmpsryfhtxk/mmdetection']' returned non-zero exit status 2.
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "/opt/python/latest/bin/mim", line 8, in <module>
        sys.exit(cli())
      File "/opt/python/3.10.4/lib/python3.10/site-packages/click/core.py", line 829, in __call__
        return self.main(*args, **kwargs)
      File "/opt/python/3.10.4/lib/python3.10/site-packages/click/core.py", line 782, in main
        rv = self.invoke(ctx)
      File "/opt/python/3.10.4/lib/python3.10/site-packages/click/core.py", line 1259, in invoke
        return _process_result(sub_ctx.command.invoke(sub_ctx))
      File "/opt/python/3.10.4/lib/python3.10/site-packages/click/core.py", line 1066, in invoke
        return ctx.invoke(self.callback, **ctx.params)
      File "/opt/python/3.10.4/lib/python3.10/site-packages/click/core.py", line 610, in invoke
        return callback(*args, **kwargs)
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/commands/install.py", line 101, in cli
        install(
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/commands/install.py", line 205, in install
        install_from_github(target_pkg, target_version, find_url, timeout,
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/commands/install.py", line 536, in install_from_github
        install_from_repo(
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/commands/install.py", line 493, in install_from_repo
        call_command(install_cmd)
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/utils/utils.py", line 420, in call_command
        raise highlighted_error(e)  # type: ignore
      File "/opt/python/3.10.4/lib/python3.10/site-packages/mim/utils/utils.py", line 392, in highlighted_error
        return click.style(msg, fg='red', bold=True)  # type: ignore
      File "/opt/python/3.10.4/lib/python3.10/site-packages/click/termui.py", line 519, in style
        return "".join(bits)
    TypeError: sequence item 2: expected str instance, CalledProcessError found
    


```python
# 验证
!pip list | grep mmdet

import mmdet
print(mmdet.__version__)
```

    [33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m[33mWARNING: Ignoring invalid distribution -ip (/opt/python/3.10.4/lib/python3.10/site-packages)[0m[33m
    [0m


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    /workspaces/public-post/_DL.ipynb Cell 8' in <cell line: 4>()
          <a href='vscode-notebook-cell://codespaces%2Bweidows-weidows-projects-public-post-5wpprgqjf4q5/workspaces/public-post/_DL.ipynb#ch0000007vscode-remote?line=0'>1</a> # 验证
          <a href='vscode-notebook-cell://codespaces%2Bweidows-weidows-projects-public-post-5wpprgqjf4q5/workspaces/public-post/_DL.ipynb#ch0000007vscode-remote?line=1'>2</a> get_ipython().system('pip list | grep mmdet')
    ----> <a href='vscode-notebook-cell://codespaces%2Bweidows-weidows-projects-public-post-5wpprgqjf4q5/workspaces/public-post/_DL.ipynb#ch0000007vscode-remote?line=3'>4</a> import mmdet
          <a href='vscode-notebook-cell://codespaces%2Bweidows-weidows-projects-public-post-5wpprgqjf4q5/workspaces/public-post/_DL.ipynb#ch0000007vscode-remote?line=4'>5</a> print(mmdet.__version__)
    

    ModuleNotFoundError: No module named 'mmdet'


#### 模型训练

1. 选择,下载模型
2. 准备数据
3. 调用 Python API 构建//训练/推理模型
4. 结果解析,可视化



```python
# mim 也可以用来下载模型,不过这个搜索比较拉
!mim search mmdet --model 'mask r-cnn'

!mim download mmdet --config mask_rcnn_r50_fpn_2x_coco --dest .
```


```python
from mmdet.apis import init_detector, inference_detector, show_result_pyplot

config_file = ""
checkpoint_file = ""
```

<a>![分割线](https://fastly.jsdelivr.net/gh/Weidows/Images/img/divider.png)</a>

## 借物表

<a name='cite_note-1' href='#cite_ref-1'>[1]</a>: https://openbayes.com/console/wrh/containers/t93t3LTXlgU

<a name='cite_note-2' href='#cite_ref-2'>[2]</a>: [MMDetection 2.3 安装教程](https://zhuanlan.zhihu.com/p/163645165)

<a name='cite_note-3' href='#cite_ref-3'>[3]</a>: https://mmdetection.readthedocs.io/en/latest/get_started.html#installation
